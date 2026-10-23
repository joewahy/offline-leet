const $ = (sel) => document.querySelector(sel);
const isMac = navigator.platform.includes("Mac");

let problems = [];
let current = null;
let editor = null;
let saveTimer = null;
let loadingCode = false;
let hintCount = 0;
let hintsShown = [];

function esc(s) {
  return String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}

function py(v) {
  if (v === null || v === undefined) return "None";
  if (v === true) return "True";
  if (v === false) return "False";
  if (Array.isArray(v)) return "[" + v.map(py).join(", ") + "]";
  if (typeof v === "object") return "{" + Object.entries(v).map(([k, x]) => `${JSON.stringify(k)}: ${py(x)}`).join(", ") + "}";
  return JSON.stringify(v);
}

function short(s, n = 600) {
  return s.length > n ? s.slice(0, n) + `… (${s.length - n} more characters)` : s;
}

function inline(text) {
  return esc(text).replace(/`([^`]+)`/g, "<code>$1</code>");
}

function renderMarkdown(md) {
  const out = [];
  let list = false;
  let fence = null;
  const closeList = () => { if (list) { out.push("</ul>"); list = false; } };
  for (const line of md.split("\n")) {
    if (fence !== null) {
      if (line.startsWith("```")) { out.push(`<pre><code>${esc(fence.join("\n"))}</code></pre>`); fence = null; }
      else fence.push(line);
      continue;
    }
    if (line.startsWith("```")) { closeList(); fence = []; continue; }
    const heading = line.match(/^(#{1,3})\s+(.*)/);
    if (heading) { closeList(); out.push(`<h${heading[1].length}>${inline(heading[2])}</h${heading[1].length}>`); continue; }
    const item = line.match(/^[-*]\s+(.*)/);
    if (item) { if (!list) { out.push("<ul>"); list = true; } out.push(`<li>${inline(item[1])}</li>`); continue; }
    closeList();
    if (line.trim()) out.push(`<p>${inline(line)}</p>`);
  }
  closeList();
  return out.join("\n");
}

async function api(path, body) {
  const res = await fetch(path, body === undefined ? {} : {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || res.statusText);
  return data;
}

const CATEGORY_NAMES = {
  "arrays-hashing": "Arrays & Hashing",
  "heap-priority-queue": "Heap / Priority Queue",
  "1d-dp": "1-D DP",
  "2d-dp": "2-D DP",
  "math-geometry": "Math & Geometry",
};

function categoryName(cat) {
  return CATEGORY_NAMES[cat] || cat.replace(/-/g, " ");
}

function renderList() {
  const solved = problems.filter((p) => p.status === "solved").length;
  $("#progress-count").textContent = `${solved} / ${problems.length} solved`;
  const byCategory = {};
  for (const p of problems) (byCategory[p.category] ||= []).push(p);
  const html = Object.entries(byCategory).map(([cat, items]) => {
    const rows = items.map((p) => {
      const mark = p.status === "solved" ? "&#10003;" : p.status === "attempted" ? "&#9679;" : "";
      return `<button class="problem-row${current && current.key === p.key ? " current" : ""}" data-key="${p.key}">
        <span class="status ${p.status}">${mark}</span>
        <span class="num">${p.id}</span>
        <span class="name">${esc(p.title)}</span>
        <span class="pill ${p.difficulty}">${p.difficulty}</span>
      </button>`;
    }).join("");
    return `<h3>${esc(categoryName(cat))}</h3>${rows}`;
  }).join("");
  $("#problem-list").innerHTML = html;
}

function storedHints(key) {
  try {
    return Number(localStorage.getItem("hints:" + key)) || 0;
  } catch (err) {
    return 0;
  }
}

function storeHints(key, n) {
  try {
    localStorage.setItem("hints:" + key, String(n));
  } catch (err) {
    // hints still work, they just reset when the page reloads
  }
}

function renderHints() {
  $("#hints").hidden = hintCount === 0;
  if (!hintCount) return;
  const shown = hintsShown.length;
  $("#hint-list").innerHTML = hintsShown
    .map((h, i) => `<div class="hint"><strong>Hint ${i + 1} of ${hintCount}</strong><p>${inline(h)}</p></div>`)
    .join("");
  $("#hint-label").textContent = shown ? `${shown} of ${hintCount} hints shown` : "Stuck? Hints stay hidden until you ask.";
  const btn = $("#hint-btn");
  btn.hidden = shown >= hintCount;
  btn.textContent = `Show hint ${shown + 1}`;
  $("#hint-list").scrollTop = $("#hint-list").scrollHeight;
}

async function loadHints(key, count) {
  hintCount = count;
  hintsShown = [];
  renderHints();
  const n = Math.min(storedHints(key), count);
  if (!n) return;
  const loaded = await Promise.all(Array.from({ length: n }, (_, i) => api(`/api/problems/${key}/hint/${i + 1}`)));
  if (current && current.key === key) {
    hintsShown = loaded.map((r) => r.hint);
    renderHints();
  }
}

async function showNextHint() {
  const key = current.key;
  const next = hintsShown.length + 1;
  const res = await api(`/api/problems/${key}/hint/${next}`);
  if (current.key !== key) return;
  hintsShown.push(res.hint);
  storeHints(key, next);
  renderHints();
}

function setDrawer(open) {
  $("#drawer").hidden = !open;
  $("#scrim").hidden = !open;
}

async function flushSave() {
  if (!saveTimer || !current) return;
  clearTimeout(saveTimer);
  saveTimer = null;
  await api(`/api/problems/${current.key}/save`, { code: editor.getValue() });
  $("#save-state").textContent = "Saved";
}

function scheduleSave() {
  if (loadingCode) return;
  $("#save-state").textContent = "Editing…";
  clearTimeout(saveTimer);
  saveTimer = setTimeout(async () => {
    saveTimer = null;
    try {
      await api(`/api/problems/${current.key}/save`, { code: editor.getValue() });
      $("#save-state").textContent = "Saved";
    } catch (err) {
      $("#save-state").textContent = "Save failed: " + err.message;
    }
  }, 600);
}

async function openProblem(key) {
  await flushSave();
  const data = await api(`/api/problems/${key}`);
  current = data;
  history.replaceState(null, "", "#" + key);
  document.title = `${data.title} · offline-leet`;
  $("#title-text").textContent = `${data.id}. ${data.title}`;
  const pill = $("#difficulty");
  pill.textContent = data.difficulty;
  pill.className = `pill ${data.difficulty}`;
  $("#statement").innerHTML = renderMarkdown(data.readme);
  $("#statement").scrollTop = 0;
  loadingCode = true;
  editor.setValue(data.code);
  loadingCode = false;
  $("#save-state").textContent = "";
  $("#results").innerHTML = '<p class="muted">Run your code to see results here.</p>';
  loadHints(data.key, data.hint_count || 0).catch(() => {});
  renderList();
  setDrawer(false);
}

function step(delta) {
  const i = problems.findIndex((p) => p.key === current.key);
  const next = problems[i + delta];
  if (next) openProblem(next.key);
}

function renderResults(outcome) {
  if (outcome.load_error) {
    return `<div class="summary fail">Could not run your code</div><pre class="error-box">${esc(outcome.load_error)}</pre>`;
  }
  const results = outcome.results;
  const passed = results.filter((r) => r.ok).length;
  const allPass = passed === results.length;
  const firstBad = results.findIndex((r) => !r.ok);
  const cases = results.map((r, i) => {
    const detail = [
      `<dt>Input</dt><dd><pre>${esc(short(r.args.map(py).join(", ")))}</pre></dd>`,
      `<dt>Expected</dt><dd><pre>${esc(short(py(r.expected)))}</pre></dd>`,
      r.error ? `<dt>Error</dt><dd><pre class="error-box">${esc(r.error)}</pre></dd>` : `<dt>Your output</dt><dd><pre>${esc(short(py(r.got)))}</pre></dd>`,
      r.stdout ? `<dt>Printed</dt><dd><pre>${esc(r.stdout)}</pre></dd>` : "",
    ].join("");
    return `<div class="case ${r.ok ? "ok" : "bad"}">
      <button aria-expanded="${i === firstBad}"><span class="mark">${r.ok ? "&#10003;" : "&#10007;"}</span>Case ${i + 1}
        <span class="preview">${esc(short(r.args.map(py).join(", "), 120))}</span></button>
      <dl class="detail" ${i === firstBad ? "" : "hidden"}>${detail}</dl>
    </div>`;
  }).join("");
  const label = allPass ? `Accepted: ${passed}/${results.length} passed` : `${passed}/${results.length} passed`;
  return `<div class="summary ${allPass ? "pass" : "fail"}">${label}</div><div class="cases">${cases}</div>`;
}

async function run() {
  const btn = $("#run-btn");
  btn.disabled = true;
  $("#results").innerHTML = '<p class="muted">Running…</p>';
  clearTimeout(saveTimer);
  saveTimer = null;
  try {
    const outcome = await api(`/api/problems/${current.key}/run`, { code: editor.getValue() });
    $("#results").innerHTML = renderResults(outcome);
    $("#save-state").textContent = "Saved";
    const entry = problems.find((p) => p.key === current.key);
    if (entry && outcome.status) { entry.status = outcome.status; renderList(); }
  } catch (err) {
    $("#results").innerHTML = `<pre class="error-box">${esc(err.message)}</pre>`;
  } finally {
    btn.disabled = false;
  }
}

function initEditor() {
  const base = location.origin + "/vendor/monaco";
  self.MonacoEnvironment = {
    getWorkerUrl() {
      const src = `self.MonacoEnvironment={baseUrl:'${base}/'};importScripts('${base}/vs/base/worker/workerMain.js');`;
      return "data:text/javascript;charset=utf-8," + encodeURIComponent(src);
    },
  };
  const dark = matchMedia("(prefers-color-scheme: dark)");
  editor = monaco.editor.create($("#editor"), {
    language: "python",
    theme: dark.matches ? "vs-dark" : "vs",
    automaticLayout: true,
    minimap: { enabled: false },
    fontSize: 14,
    scrollBeyondLastLine: false,
    tabSize: 4,
    insertSpaces: true,
    quickSuggestions: false,
    suggestOnTriggerCharacters: false,
    wordBasedSuggestions: "off",
  });
  dark.addEventListener("change", (e) => monaco.editor.setTheme(e.matches ? "vs-dark" : "vs"));
  editor.onDidChangeModelContent(scheduleSave);
  editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, run);
}

async function start() {
  $("#run-hint").textContent = isMac ? "⌘↵" : "Ctrl+↵";
  $("#menu-btn").onclick = () => setDrawer(true);
  $("#close-drawer").onclick = () => setDrawer(false);
  $("#scrim").onclick = () => setDrawer(false);
  $("#prev-btn").onclick = () => step(-1);
  $("#next-btn").onclick = () => step(1);
  $("#run-btn").onclick = run;
  $("#hint-btn").onclick = () => showNextHint().catch((err) => { $("#hint-label").textContent = err.message; });
  $("#problem-list").onclick = (e) => {
    const row = e.target.closest(".problem-row");
    if (row) openProblem(row.dataset.key);
  };
  $("#results").onclick = (e) => {
    const btn = e.target.closest(".case > button");
    if (!btn) return;
    const detail = btn.nextElementSibling;
    detail.hidden = !detail.hidden;
    btn.setAttribute("aria-expanded", String(!detail.hidden));
  };
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") setDrawer(false);
    if ((e.metaKey || e.ctrlKey) && e.key === "s") { e.preventDefault(); flushSave(); }
  });
  window.addEventListener("beforeunload", () => {
    if (saveTimer && current) {
      navigator.sendBeacon(`/api/problems/${current.key}/save`, new Blob([JSON.stringify({ code: editor.getValue() })], { type: "application/json" }));
    }
  });

  problems = await api("/api/problems");
  const wanted = location.hash.slice(1);
  const first = problems.find((p) => p.key === wanted) || problems.find((p) => p.status !== "solved") || problems[0];
  await openProblem(first.key);
}

require.config({ paths: { vs: "/vendor/monaco/vs" } });
require(["vs/editor/editor.main"], () => {
  initEditor();
  start().catch((err) => { $("#statement").textContent = "Failed to load: " + err.message; });
});
