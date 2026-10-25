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
  if (!res.ok) {
    const err = new Error(data.error || res.statusText);
    err.status = res.status;
    throw err;
  }
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

function problemRow(p) {
  const mark = p.due ? "&#8635;" : p.status === "solved" ? "&#10003;" : p.status === "attempted" ? "&#9679;" : "";
  return `<button class="problem-row${current && current.key === p.key ? " current" : ""}" data-key="${p.key}">
    <span class="status ${p.status}${p.due ? " due" : ""}" ${p.due ? 'title="Due for review"' : ""}>${mark}</span>
    <span class="num">${p.id}</span>
    <span class="name">${esc(p.title)}</span>
    <span class="pill ${p.difficulty}">${p.difficulty}</span>
  </button>`;
}

function renderList() {
  const solved = problems.filter((p) => p.status === "solved").length;
  $("#progress-count").textContent = `${solved} / ${problems.length} solved`;
  const byCategory = {};
  for (const p of problems) (byCategory[p.category] ||= []).push(p);
  const html = Object.entries(byCategory).map(([cat, items]) => {
    return `<h3>${esc(categoryName(cat))}</h3>${items.map(problemRow).join("")}`;
  }).join("");
  $("#problem-list").innerHTML = html;
}

function renderHints() {
  $("#hints").hidden = hintCount === 0;
  if (!hintCount) return;
  $("#hint-label").textContent = `${hintCount} hints, collapsed until you open them`;
  $("#hint-list").innerHTML = hintsShown
    .map((h, i) => `<details class="hint"><summary>Hint ${i + 1} of ${hintCount}</summary><p>${inline(h)}</p></details>`)
    .join("");
}

async function loadHints(key, count) {
  hintCount = count;
  hintsShown = [];
  renderHints();
  if (!count) return;
  const loaded = await Promise.all(Array.from({ length: count }, (_, i) => api(`/api/problems/${key}/hint/${i + 1}`)));
  if (current && current.key === key) {
    hintsShown = loaded.map((r) => r.hint);
    renderHints();
  }
}

function storedSize(name) {
  try {
    return Number(localStorage.getItem("size:" + name)) || 0;
  } catch (err) {
    return 0;
  }
}

function storeSize(name, px) {
  try {
    localStorage.setItem("size:" + name, String(Math.round(px)));
  } catch (err) {
    // sizes still work, they just reset when the page reloads
  }
}

// Drag a splitter to resize `target`; `measure` maps the pointer position to a size in px.
function makeResizable(splitter, target, prop, name, measure, min, max) {
  const apply = (px) => { target.style[prop] = `${Math.min(max(), Math.max(min, px))}px`; };
  const saved = storedSize(name);
  if (saved) apply(saved);
  splitter.onpointerdown = (e) => {
    e.preventDefault();
    splitter.setPointerCapture(e.pointerId);
    splitter.classList.add("dragging");
    document.body.classList.add("resizing", prop === "width" ? "col" : "row");
  };
  splitter.onpointermove = (e) => {
    if (splitter.hasPointerCapture(e.pointerId)) apply(measure(e));
  };
  splitter.onpointerup = () => {
    splitter.classList.remove("dragging");
    document.body.classList.remove("resizing", "col", "row");
    storeSize(name, target.getBoundingClientRect()[prop]);
  };
  splitter.ondblclick = () => {
    target.style[prop] = "";
    storeSize(name, 0);
  };
}

function setupSplitters() {
  const left = $("#left");
  const work = $("#work");
  const results = $("#results");
  makeResizable($("#split-v"), left, "width", "left", (e) => e.clientX - left.getBoundingClientRect().left,
    300, () => window.innerWidth - 320);
  makeResizable($("#split-h"), results, "height", "results", (e) => work.getBoundingClientRect().bottom - e.clientY,
    110, () => work.getBoundingClientRect().height - 140);
}

function openRoadmap() {
  const stats = {};
  for (const p of problems) {
    const s = (stats[p.category] ||= { solved: 0, total: 0 });
    s.total += 1;
    if (p.status === "solved") s.solved += 1;
  }
  const solved = problems.filter((p) => p.status === "solved").length;
  $("#roadmap-count").textContent = `${solved} / ${problems.length} solved`;
  $("#roadmap-body").innerHTML = renderRoadmap(stats);
  $("#roadmap").hidden = false;
}

function closeRoadmap() {
  $("#roadmap").hidden = true;
  $("#roadmap-topic").hidden = true;
}

function selectRoadmapTopic(node) {
  if (!node) return;
  const cat = node.dataset.cat;
  const items = problems.filter((p) => p.category === cat);
  if (!items.length) return;
  document.querySelectorAll(".rm-node.selected").forEach((n) => n.classList.remove("selected"));
  node.classList.add("selected");
  const solved = items.filter((p) => p.status === "solved").length;
  $("#roadmap-topic-name").textContent = ROADMAP_NODES[cat].label.join(" ");
  $("#roadmap-topic-count").textContent = `${solved} / ${items.length} solved`;
  $("#roadmap-topic-list").innerHTML = items.map(problemRow).join("");
  $("#roadmap-topic").hidden = false;
}

function closeRoadmapTopic() {
  $("#roadmap-topic").hidden = true;
  document.querySelectorAll(".rm-node.selected").forEach((n) => n.classList.remove("selected"));
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

function fmtSeconds(seconds) {
  if (seconds < 0.001) return `${Math.round(seconds * 1e6)} \u00b5s`;
  if (seconds < 1) return `${(seconds * 1000).toFixed(1)} ms`;
  return `${seconds.toFixed(2)} s`;
}

function fmtBytes(count) {
  if (count < 1024) return `${count} B`;
  if (count < 1024 * 1024) return `${Math.round(count / 1024)} KB`;
  return `${(count / 1024 / 1024).toFixed(1)} MB`;
}

const VERDICT_CLASS = {
  faster: "good", similar: "good", less: "good",
  slower: "warn", more: "warn",
  much_slower: "bad", much_more: "bad", timeout: "bad",
};

function renderPerf(report) {
  if (report.error) return `<p class="muted">${esc(report.error)}</p>`;
  const ratio = (r) => (r ? ` (${r < 10 ? r.toFixed(1) : Math.round(r)}x the reference)` : "");
  const line = (label, v, extra) =>
    `<p class="verdict ${VERDICT_CLASS[v.verdict] || "muted"}"><strong>${label}:</strong> ${esc(v.message)}${extra}</p>`;
  const rows = report.cases.map((c) => `<tr>
      <td>Case ${c.case}</td>
      <td>${fmtBytes(c.input_bytes)}</td>
      <td>${c.timed_out ? "timed out" : fmtSeconds(c.time)} <span class="muted">vs ${fmtSeconds(c.ref_time)}</span></td>
      <td>${c.memory === null ? "" : `${fmtBytes(c.memory)} <span class="muted">vs ${fmtBytes(c.ref_memory)}</span>`}</td>
    </tr>`).join("");
  return `${line("Time", report.time, ratio(report.time.ratio))}
    ${line("Memory", report.memory, "")}
    <table class="perf-table">
      <thead><tr><th></th><th>Input</th><th>Time (yours vs reference)</th><th>Extra memory</th></tr></thead>
      <tbody>${rows}</tbody>
    </table>
    <p class="muted small">An estimate, not a proof: it compares your timing with the reference solution on this machine, using the heaviest test inputs. A large ratio usually means a worse complexity class.</p>`;
}

function perfBlock() {
  const target = current && current.complexity
    ? `<span class="muted">Target: ${esc(current.complexity.time)} time, ${esc(current.complexity.space)} space</span>`
    : "";
  return `<div class="perf">
    <div class="perf-head"><strong>Performance</strong>${target}
      <button id="perf-btn" class="ghost">Compare with reference</button></div>
    <div id="perf-body"></div>
  </div>`;
}

async function runPerf() {
  const btn = $("#perf-btn");
  const body = $("#perf-body");
  btn.disabled = true;
  body.innerHTML = '<p class="muted">Measuring against the reference solution\u2026</p>';
  clearTimeout(saveTimer);
  saveTimer = null;
  try {
    const report = await api(`/api/problems/${current.key}/perf`, { code: editor.getValue() });
    body.innerHTML = renderPerf(report);
    $("#save-state").textContent = "Saved";
  } catch (err) {
    body.innerHTML = `<pre class="error-box">${esc(err.message)}</pre>`;
  } finally {
    btn.disabled = false;
    btn.textContent = "Measure again";
  }
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
  const hidden = outcome.hidden && !outcome.hidden.skipped ? outcome.hidden : null;
  const hiddenOk = !hidden || !(hidden.error || hidden.failure);
  const accepted = allPass && hiddenOk;
  const visible = `${passed}/${results.length}`;
  const label = accepted ? `Accepted: ${visible} passed`
    : allPass ? `${visible} visible tests passed, but a hidden test failed`
    : `${visible} passed`;
  const summaryClass = accepted ? "pass" : "fail";
  return `<div class="summary ${summaryClass}">${label}</div>${hidden ? hiddenBlock(hidden) : ""}<div class="cases">${cases}</div>${accepted ? perfBlock() : ""}`;
}

function hiddenBlock(hidden) {
  if (hidden.error) {
    return `<div class="hidden-tests bad"><strong>Hidden tests could not run</strong><pre class="error-box">${esc(hidden.error)}</pre></div>`;
  }
  const f = hidden.failure;
  if (!f) {
    return `<div class="hidden-tests ok"><strong>Hidden tests: ${hidden.passed}/${hidden.total} passed</strong></div>`;
  }
  const slow = f.error === "time limit exceeded";
  const detail = slow
    ? `<p>Your solution passes the visible tests but ran out of time on a large input (about ${f.input_size.toLocaleString()} characters). It is probably too slow, so look for a better time complexity.</p>`
    : f.error
      ? `<pre class="error-box">${esc(f.error)}</pre>`
      : `<dl class="detail"><dt>Expected</dt><dd><pre>${esc(f.expected)}</pre></dd><dt>Your output</dt><dd><pre>${esc(f.got)}</pre></dd></dl>`;
  return `<div class="hidden-tests bad"><strong>Failed hidden test ${f.case} of ${hidden.total}</strong>
    <p class="muted">Large inputs are not shown.</p>${detail}${f.stdout ? `<pre>${esc(f.stdout)}</pre>` : ""}</div>`;
}

function closeSolution() {
  $("#solution").hidden = true;
  $("#solution-scrim").hidden = true;
}

async function showSolution() {
  if (!current) return;
  let data;
  try {
    try {
      data = await api(`/api/problems/${current.key}/solution`);
    } catch (err) {
      if (err.status !== 403) throw err;
      if (!confirm("You have not solved this problem yet.\n\nShow the reference solution anyway? It will spoil the problem.")) return;
      data = await api(`/api/problems/${current.key}/solution?force=1`);
    }
  } catch (err) {
    $("#save-state").textContent = "Could not load the solution: " + err.message;
    return;
  }
  let code;
  try {
    code = await monaco.editor.colorize(data.reference, "python", { tabSize: 4 });
  } catch (err) {
    code = esc(data.reference);
  }
  const target = data.complexity
    ? `<p class="muted">Target: ${esc(data.complexity.time)} time, ${esc(data.complexity.space)} space.</p>`
    : "";
  const explanation = data.explanation ? `<div class="explanation">${renderMarkdown(data.explanation)}</div>` : "";
  $("#solution-body").innerHTML = `${target}${explanation}<pre class="solution-code">${code}</pre>
    <p class="muted small">This is one valid solution. Yours can differ and still be right, so compare the approach and the complexity rather than the exact code.</p>`;
  $("#solution").hidden = false;
  $("#solution-scrim").hidden = false;
}

async function resetCode() {
  if (!current) return;
  if (!confirm("Replace your code with the starter code?\n\nYour current code is saved to a backup first.")) return;
  clearTimeout(saveTimer);
  saveTimer = null;
  try {
    const data = await api(`/api/problems/${current.key}/reset`, {});
    loadingCode = true;
    editor.setValue(data.code);
    loadingCode = false;
    $("#results").innerHTML = '<p class="muted">Run your code to see results here.</p>';
    $("#save-state").textContent = data.backed_up ? "Reset (backup kept)" : "Reset";
  } catch (err) {
    $("#save-state").textContent = "Reset failed: " + err.message;
  }
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
    if (entry && outcome.status) { entry.status = outcome.status; entry.due = outcome.due; renderList(); }
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
  $("#roadmap-btn").onclick = openRoadmap;
  $("#roadmap-close").onclick = closeRoadmap;
  $("#roadmap-body").onclick = (e) => selectRoadmapTopic(e.target.closest(".rm-node"));
  $("#roadmap-body").onkeydown = (e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      selectRoadmapTopic(e.target.closest(".rm-node"));
    }
  };
  $("#roadmap-topic-close").onclick = closeRoadmapTopic;
  $("#roadmap-topic-list").onclick = (e) => {
    const row = e.target.closest(".problem-row");
    if (!row) return;
    closeRoadmap();
    openProblem(row.dataset.key);
  };
  $("#menu-btn").onclick = () => setDrawer(true);
  $("#close-drawer").onclick = () => setDrawer(false);
  $("#scrim").onclick = () => setDrawer(false);
  $("#prev-btn").onclick = () => step(-1);
  $("#next-btn").onclick = () => step(1);
  $("#run-btn").onclick = run;
  setupSplitters();
  $("#reset-btn").onclick = resetCode;
  $("#solution-btn").onclick = showSolution;
  $("#solution-close").onclick = closeSolution;
  $("#solution-scrim").onclick = closeSolution;
  $("#problem-list").onclick = (e) => {
    const row = e.target.closest(".problem-row");
    if (row) openProblem(row.dataset.key);
  };
  $("#results").onclick = (e) => {
    if (e.target.closest("#perf-btn")) {
      runPerf();
      return;
    }
    const btn = e.target.closest(".case > button");
    if (!btn) return;
    const detail = btn.nextElementSibling;
    detail.hidden = !detail.hidden;
    btn.setAttribute("aria-expanded", String(!detail.hidden));
  };
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      setDrawer(false);
      closeRoadmap();
      closeSolution();
    }
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
