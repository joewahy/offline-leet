const $ = (sel) => document.querySelector(sel);
const isMac = navigator.platform.includes("Mac");

let problems = [];
let current = null;
let editor = null;
let saveTimer = null;
let loadingCode = false;
let hintCount = 0;
let hintsShown = [];

// Screen readers hear one short status line per run, not the whole results list.
function announce(text) {
  const live = $("#live");
  live.textContent = "";
  setTimeout(() => { live.textContent = text; }, 50);
}

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

let listFilter = "all";
let listQuery = "";

function matchesList(p) {
  if (listFilter === "todo" && p.status === "solved") return false;
  if (listFilter === "due" && !p.due) return false;
  const q = listQuery.trim().toLowerCase();
  return !q || `${p.id} ${p.title}`.toLowerCase().includes(q);
}

// A due review comes first, then the first problem not yet solved, never the one already open.
function nextUp() {
  const other = (p) => !current || p.key !== current.key;
  const due = problems.find((p) => p.due && other(p));
  if (due) return { problem: due, label: "Review" };
  const todo = problems.find((p) => p.status !== "solved" && other(p));
  return todo ? { problem: todo, label: "Next" } : null;
}

function renderList() {
  const solved = problems.filter((p) => p.status === "solved").length;
  $("#progress-count").textContent = `${solved} / ${problems.length} solved`;
  const counts = { all: problems.length, todo: problems.length - solved, due: problems.filter((p) => p.due).length };
  document.querySelectorAll("#problem-filter button").forEach((b) => {
    const name = { all: "All", todo: "To do", due: "Due" }[b.dataset.filter];
    b.textContent = `${name} ${counts[b.dataset.filter]}`;
    b.setAttribute("aria-pressed", String(b.dataset.filter === listFilter));
  });
  const up = nextUp();
  const upBtn = $("#next-up");
  upBtn.hidden = !up;
  if (up) {
    upBtn.textContent = `${up.label}: ${up.problem.id}. ${up.problem.title} \u2192`;
    upBtn.dataset.key = up.problem.key;
  }
  const byCategory = {};
  for (const p of problems.filter(matchesList)) (byCategory[p.category] ||= []).push(p);
  const html = Object.entries(byCategory).map(([cat, items]) => {
    return `<h3>${esc(categoryName(cat))}</h3>${items.map(problemRow).join("")}`;
  }).join("");
  $("#problem-list").innerHTML = html || '<p class="muted empty-list">No problems match.</p>';
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

let notesTimer = null;

function renderNotes(text) {
  $("#notes-text").value = text;
  $("#notes").classList.toggle("has-notes", !!text.trim());
  $("#notes-state").textContent = "";
}

async function flushNotes() {
  if (!notesTimer || !current) return;
  clearTimeout(notesTimer);
  notesTimer = null;
  await api(`/api/problems/${current.key}/notes`, { text: $("#notes-text").value });
  $("#notes-state").textContent = "Saved";
}

function scheduleNotes() {
  $("#notes").classList.toggle("has-notes", !!$("#notes-text").value.trim());
  $("#notes-state").textContent = "Editing\u2026";
  clearTimeout(notesTimer);
  notesTimer = setTimeout(() => {
    flushNotes().catch((err) => { $("#notes-state").textContent = "Save failed: " + err.message; });
  }, 600);
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
function makeResizable(splitter, target, prop, name, measure, min, max, growKey, shrinkKey) {
  const apply = (px) => {
    const size = Math.min(max(), Math.max(min, px));
    target.style[prop] = `${size}px`;
    splitter.setAttribute("aria-valuenow", String(Math.round(size)));
    splitter.setAttribute("aria-valuemin", String(min));
    splitter.setAttribute("aria-valuemax", String(Math.round(max())));
  };
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
  splitter.onkeydown = (e) => {
    const step = e.shiftKey ? 64 : 16;
    const size = target.getBoundingClientRect()[prop];
    if (e.key === growKey) apply(size + step);
    else if (e.key === shrinkKey) apply(size - step);
    else if (e.key === "Home") { target.style[prop] = ""; storeSize(name, 0); }
    else return;
    e.preventDefault();
    if (e.key !== "Home") storeSize(name, target.getBoundingClientRect()[prop]);
  };
}

function setupSplitters() {
  const left = $("#left");
  const work = $("#work");
  const results = $("#results");
  makeResizable($("#split-v"), left, "width", "left", (e) => e.clientX - left.getBoundingClientRect().left,
    300, () => window.innerWidth - 320, "ArrowRight", "ArrowLeft");
  makeResizable($("#split-h"), results, "height", "results", (e) => work.getBoundingClientRect().bottom - e.clientY,
    110, () => work.getBoundingClientRect().height - 140, "ArrowUp", "ArrowDown");
}

let roadmapView;
let roadmapOpen = false;

// Run `update` inside a view transition, or straight away when motion is reduced or unsupported.
function withTransition(update, name) {
  const animated = matchMedia("(prefers-reduced-motion: no-preference)").matches;
  if (!animated || !document.startViewTransition) {
    update();
    return;
  }
  const root = document.documentElement;
  const transition = document.startViewTransition(update);
  if (name) {
    root.classList.add(name);
    transition.finished.finally(() => root.classList.remove(name));
  }
}

function renderRoadmapStats() {
  const counts = {};
  for (const p of problems) {
    const c = (counts[p.difficulty] ||= { solved: 0, total: 0 });
    c.total += 1;
    if (p.status === "solved") c.solved += 1;
  }
  const { legend, ring, label } = renderStats(counts);
  $("#stats-legend").innerHTML = legend;
  const el = $("#stats-ring");
  el.innerHTML = ring;
  el.setAttribute("aria-label", label);
  $("#random-btn").disabled = !problems.some((p) => p.status !== "solved");
  loadActivity().catch(() => {});
}

function showHeatTip(cell) {
  const tip = $("#heat-tip");
  tip.textContent = cell.dataset.tip;
  tip.hidden = false;
  const box = cell.getBoundingClientRect();
  const width = tip.offsetWidth;
  const left = Math.min(Math.max(8, box.left + box.width / 2 - width / 2), window.innerWidth - width - 8);
  const above = box.top - tip.offsetHeight - 6;
  tip.style.left = `${left}px`;
  tip.style.top = `${above >= 8 ? above : box.bottom + 6}px`;
}

function hideHeatTip() {
  $("#heat-tip").hidden = true;
}

async function loadActivity() {
  const activity = await api("/api/activity");
  const box = $("#stats-activity");
  const { html } = renderActivity(activity);
  box.innerHTML = html;
  box.hidden = false;
  const solved = problems.filter((p) => p.status === "solved").length;
  const streak = streakText(activity.current_streak);
  $("#roadmap-count").textContent = `${solved} / ${problems.length} solved${streak ? ` \u00b7 ${streak}` : ""}`;
}

async function openRandomUnsolved() {
  const open = problems.filter((p) => p.status !== "solved");
  const pool = open.filter((p) => !current || p.key !== current.key);
  const choices = pool.length ? pool : open;
  if (!choices.length) return;
  await openProblem(choices[Math.floor(Math.random() * choices.length)].key);
}

async function clearProgress() {
  const go = await confirmDialog({
    title: "Delete all progress?",
    lines: [
      "Every problem goes back to unsolved and the review schedule is cleared.",
      "Your code in each solution.py is not touched, and the old progress file is backed up first.",
    ],
    confirmLabel: "Delete progress",
    danger: true,
    focusCancel: true,
  });
  if (!go) return;
  try {
    await api("/api/progress/reset", {});
    problems = await api("/api/problems");
    renderList();
    openRoadmapContents();
    roadmapView.show();
  } catch (err) {
    $("#roadmap-count").textContent = "Delete failed: " + err.message;
  }
}

function openRoadmapContents() {
  const stats = {};
  for (const p of problems) {
    const s = (stats[p.category] ||= { solved: 0, total: 0, due: 0 });
    s.total += 1;
    if (p.status === "solved") s.solved += 1;
    if (p.due) s.due += 1;
  }
  const here = problems.find((p) => current && p.key === current.key);
  const solved = problems.filter((p) => p.status === "solved").length;
  $("#roadmap-count").textContent = `${solved} / ${problems.length} solved`;
  $("#roadmap-body").innerHTML = renderRoadmap(stats, here && here.category);
  renderRoadmapStats();
  const topic = document.querySelector("#roadmap-topic:not([hidden])");
  if (topic) closeRoadmapTopic();
}

function openRoadmap() {
  roadmapOpen = true;
  withTransition(() => {
    openRoadmapContents();
    $("#roadmap").hidden = false;
    roadmapView.show();
    document.body.classList.add("roadmap-open");
    $("#roadmap-btn").innerHTML = "&larr; Back to problem";
  }, "vt-roadmap-open");
}

function closeRoadmap() {
  if (!roadmapOpen) return;
  roadmapOpen = false;
  hideHeatTip();
  withTransition(() => {
    $("#roadmap").hidden = true;
    $("#roadmap-topic").hidden = true;
    document.body.classList.remove("roadmap-open");
    $("#roadmap-btn").innerHTML = "&#10070; Roadmap";
    if (editor) editor.layout();
  });
}

function selectRoadmapTopic(node, focusPanel = false) {
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
  const list = $("#roadmap-topic-list");
  if (!$("#roadmap-topic").hidden) {
    list.classList.remove("swap");
    void list.offsetWidth;
    list.classList.add("swap");
  }
  $("#roadmap-topic").hidden = false;
  if (focusPanel) $("#roadmap-topic-close").focus();
}

function closeRoadmapTopic(restoreFocus = true) {
  const node = document.querySelector(".rm-node.selected");
  $("#roadmap-topic").hidden = true;
  document.querySelectorAll(".rm-node.selected").forEach((n) => n.classList.remove("selected"));
  if (restoreFocus) node?.focus();
}

// On narrow screens the statement, editor and results share one pane at a time.
function setPane(name) {
  document.body.dataset.pane = name;
  document.querySelectorAll("#tabs [role=tab]").forEach((tab) => {
    const on = tab.dataset.pane === name;
    tab.setAttribute("aria-selected", String(on));
    tab.tabIndex = on ? 0 : -1;
  });
  if (name === "code" && editor) requestAnimationFrame(() => editor.layout());
}

function setMoreMenu(open) {
  $("header").classList.toggle("more-open", open);
  $("#more-btn").setAttribute("aria-expanded", String(open));
}

let drawerTimer;
let drawerOpener = null;
const BEHIND_DRAWER = "header, main, #tabs, #roadmap";

function setDrawer(open) {
  const parts = [$("#drawer"), $("#scrim")];
  clearTimeout(drawerTimer);
  if (open) {
    if (parts[0].hidden) drawerOpener = document.activeElement;
    parts.forEach((el) => { el.classList.remove("closing"); el.hidden = false; });
    document.querySelectorAll(BEHIND_DRAWER).forEach((el) => { el.inert = true; });
    const row = $("#problem-list .problem-row.current");
    row?.scrollIntoView({ block: "center" });
    if (matchMedia("(pointer: fine)").matches) {
      $("#problem-search").focus({ preventScroll: true });
      $("#problem-search").select();
    } else {
      (row || $("#close-drawer")).focus({ preventScroll: true });
    }
    return;
  }
  if (parts[0].hidden) return;
  const animated = matchMedia("(prefers-reduced-motion: no-preference)").matches;
  parts.forEach((el) => el.classList.add("closing"));
  document.querySelectorAll(BEHIND_DRAWER).forEach((el) => { el.inert = false; });
  drawerOpener?.focus();
  drawerOpener = null;
  drawerTimer = setTimeout(() => {
    parts.forEach((el) => { el.hidden = true; el.classList.remove("closing"); });
  }, animated ? 180 : 0);
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
  await flushNotes().catch(() => {});
  await flushTestCases().catch(() => {});
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
  $("#output").innerHTML = '<p class="muted">Run your code to see results here.</p>';
  loadTestCases(data);
  showResultsView("testcase");
  renderNotes(data.notes || "");
  loadHints(data.key, data.hint_count || 0).catch(() => {});
  setPane("problem");
  renderList();
  setDrawer(false);
  closeRoadmap();
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

function nextProblem() {
  const i = problems.findIndex((p) => p.key === current.key);
  const after = [...problems.slice(i + 1), ...problems.slice(0, i)];
  return after.find((p) => p.status !== "solved") || problems[i + 1] || null;
}

function reviewNote(dueOn) {
  if (!dueOn) return "";
  const days = Math.round((new Date(`${dueOn}T00:00:00`) - new Date().setHours(0, 0, 0, 0)) / 86400000);
  if (days <= 0) return "Due for review today";
  return days === 1 ? "Next review tomorrow" : `Next review in ${days} days`;
}

function landingBlock(outcome) {
  const note = reviewNote(outcome.due_on);
  const next = nextProblem();
  if (!note && !next) return "";
  return `<div class="landing">${note ? `<span class="muted">${note}</span>` : ""}${next
    ? `<button id="next-problem" data-key="${next.key}">Next: ${next.id}. ${esc(next.title)} &rarr;</button>` : ""}</div>`;
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
  const verdict = accepted ? { label: "Correct", cls: "pass" } : verdictFor(
    results.find((r) => !r.ok) || (hidden.error ? { error: "Traceback" } : hidden.failure));
  const caseList = accepted
    ? `<details class="cases-fold"><summary>${results.length} test cases</summary><div class="cases">${cases}</div></details>`
    : `<div class="cases">${cases}</div>`;
  return `<div class="verdict-row"><span class="summary ${verdict.cls}">${verdict.label}</span>
    <span class="muted">Passed test cases: ${passed} / ${results.length}</span></div>${customNote()}${hidden ? hiddenBlock(hidden) : ""}${accepted ? landingBlock(outcome) + perfBlock() : ""}${caseList}`;
}

// One line under the verdict about the cases in the Test Case tab, with a way back to them.
function customNote() {
  const checked = tc.results ? tc.results.filter((r) => r && r.ok !== null) : [];
  if (!checked.length) return "";
  const right = checked.filter((r) => r.ok).length;
  return `<p><button type="button" class="goto-testcase">Your test cases: ${right} of ${checked.length} correct</button></p>`;
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
  const dialog = $("#solution");
  if (dialog.open) dialog.close();
}

function confirmDialog({ title, lines, confirmLabel, danger = false, focusCancel = false }) {
  const dialog = $("#confirm");
  $("#confirm-title").textContent = title;
  $("#confirm-message").innerHTML = lines.map((line) => `<p>${esc(line)}</p>`).join("");
  const ok = $("#confirm-ok");
  ok.textContent = confirmLabel;
  ok.classList.toggle("danger", danger);
  dialog.returnValue = "cancel";
  return new Promise((resolve) => {
    dialog.addEventListener("close", () => resolve(dialog.returnValue === "ok"), { once: true });
    dialog.showModal();
    if (focusCancel) dialog.querySelector("[value=cancel]").focus();
  });
}

async function showSolution() {
  if (!current) return;
  let data;
  try {
    try {
      data = await api(`/api/problems/${current.key}/solution`);
    } catch (err) {
      if (err.status !== 403) throw err;
      const go = await confirmDialog({
        title: "Show the solution?",
        lines: ["You have not solved this problem yet.", "Seeing the reference solution will spoil it."],
        confirmLabel: "Show solution",
        focusCancel: true,
      });
      if (!go) return;
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
  $("#solution-body").scrollTop = 0;
  $("#solution").showModal();
}

// Your own test cases live in the results panel. Their expected answers come from the reference solution.
let tc = { cases: [], texts: [], sel: 0, results: null, timer: null };

function showResultsView(view) {
  document.querySelectorAll("#results-tabs [role=tab]").forEach((tab) => {
    const on = tab.dataset.view === view;
    tab.setAttribute("aria-selected", String(on));
    tab.tabIndex = on ? 0 : -1;
  });
  $("#testcases").hidden = view !== "testcase";
  $("#output").hidden = view !== "output";
}

function verdictFor(r) {
  if (r.ok) return { label: "Correct", cls: "pass" };
  const err = r.error || "";
  if (r.ok === null) return { label: "Invalid input", cls: "fail" };
  if (err.startsWith("time limit exceeded")) return { label: "Time Limit Exceeded", cls: "fail" };
  if (err.startsWith("memory limit exceeded")) return { label: "Memory Limit Exceeded", cls: "fail" };
  if (err.includes("Traceback")) return { label: "Runtime Error", cls: "fail" };
  return { label: "Wrong Answer", cls: "fail" };
}

function paramName(i) {
  return (current && current.params && current.params[i]) || `arg ${i + 1}`;
}

function loadTestCases(data) {
  tc = { cases: structuredClone(data.custom || []), texts: [], sel: 0, results: null, timer: null };
  tc.texts = tc.cases.map((c) => c.args.map((a) => JSON.stringify(a)));
  renderTestCases();
}

function renderTestCases() {
  const box = $("#testcases");
  if (current && !current.params) {
    box.innerHTML = '<p class="error-box">The server is running older code than this page, so test cases and notes cannot work yet. Stop it (Ctrl+C in the terminal) and start it again, then reload this page.</p>';
    return;
  }
  const chips = tc.cases.map((c, i) => {
    const r = tc.results && tc.results[i];
    const mark = !r ? "" : r.ok === true ? '<span class="tc-mark ok" aria-hidden="true">&#10003;</span>'
      : r.ok === false ? '<span class="tc-mark bad" aria-hidden="true">&#10007;</span>' : "";
    const state = !r ? "" : r.ok === true ? ", correct" : r.ok === false ? ", wrong" : "";
    return `<button type="button" class="tc-chip${i === tc.sel ? " selected" : ""}" data-i="${i}" aria-pressed="${i === tc.sel}" aria-label="Case ${i + 1}${state}">${mark}Case ${i + 1}</button>`;
  }).join("");
  const add = '<button type="button" class="tc-add ghost" aria-label="Add a test case" title="Add a test case">+</button>';
  const del = tc.cases.length ? '<button type="button" class="tc-del ghost">Delete case</button>' : "";
  if (!tc.cases.length) {
    box.innerHTML = `<div class="tc-chips">${add}</div>
      <p class="muted tc-empty">Add a case to try your own input. The expected answer is worked out by the reference solution, and it runs whenever you press Run.</p>`;
    return;
  }
  const fields = tc.texts[tc.sel].map((text, p) => `<div class="tc-field">
      <label for="tc-arg-${p}">${esc(paramName(p))} =</label>
      <input id="tc-arg-${p}" data-p="${p}" value="${esc(text)}" spellcheck="false" autocomplete="off" aria-describedby="tc-problem-${p}">
      <p class="tc-problem" id="tc-problem-${p}" hidden>Not valid JSON. Use true, false, null and double quotes.</p>
    </div>`).join("");
  box.innerHTML = `<div class="tc-chips">${chips}${add}${del}</div>${fields}${testCaseResult()}`;
}

function testCaseResult() {
  const r = tc.results && tc.results[tc.sel];
  if (!r) return "";
  const v = verdictFor(r);
  const rows = [];
  if (r.ok !== null) rows.push(`<dt>Expected</dt><dd><pre>${esc(short(py(r.expected)))}</pre></dd>`);
  if (r.error) rows.push(`<dt>Error</dt><dd><pre class="error-box">${esc(r.error)}</pre></dd>`);
  else rows.push(`<dt>Your output</dt><dd><pre>${esc(short(py(r.got)))}</pre></dd>`);
  if (r.stdout) rows.push(`<dt>Printed</dt><dd><pre>${esc(r.stdout)}</pre></dd>`);
  return `<div class="tc-result"><div class="summary ${v.cls}">${v.label}</div><dl class="detail">${rows.join("")}</dl></div>`;
}

async function saveTestCases() {
  clearTimeout(tc.timer);
  tc.timer = null;
  await api(`/api/problems/${current.key}/custom`, { cases: tc.cases });
  current.custom = structuredClone(tc.cases);
}

async function flushTestCases() {
  if (tc.timer && current) await saveTestCases();
}

function saveTestCasesSoon() {
  clearTimeout(tc.timer);
  tc.timer = setTimeout(() => { saveTestCases().catch(() => {}); }, 500);
}

function addTestCase() {
  if (tc.cases.length >= 50) return;
  const from = tc.cases[tc.sel] ? tc.cases[tc.sel].args : (current.sample ? current.sample.args : current.params.map(() => null));
  tc.cases.push({ args: structuredClone(from) });
  tc.texts.push(from.map((a) => JSON.stringify(a)));
  tc.results = null;
  tc.sel = tc.cases.length - 1;
  saveTestCasesSoon();
  renderTestCases();
  $("#tc-arg-0")?.focus();
}

function deleteTestCase() {
  tc.cases.splice(tc.sel, 1);
  tc.texts.splice(tc.sel, 1);
  tc.results = null;
  tc.sel = Math.max(0, Math.min(tc.sel, tc.cases.length - 1));
  saveTestCasesSoon();
  renderTestCases();
}

// Keep the typed text, and only accept it as the case once every field parses.
function editTestCase(input) {
  const p = Number(input.dataset.p);
  tc.texts[tc.sel][p] = input.value;
  const parsed = tc.texts[tc.sel].map((t) => { try { return { v: JSON.parse(t) }; } catch (err) { return null; } });
  const ok = parsed[p] !== null;
  input.classList.toggle("invalid", !ok);
  input.setAttribute("aria-invalid", String(!ok));
  $(`#tc-problem-${p}`).hidden = ok;
  if (parsed.every(Boolean)) {
    tc.cases[tc.sel].args = parsed.map((x) => x.v);
    if (tc.results) tc.results[tc.sel] = null;
    saveTestCasesSoon();
  }
}


async function resetCode() {
  if (!current) return;
  const go = await confirmDialog({
    title: "Reset to the starter code?",
    lines: ["Your code in the editor will be replaced.", "A backup of your current code is saved first."],
    confirmLabel: "Reset",
    danger: true,
  });
  if (!go) return;
  clearTimeout(saveTimer);
  saveTimer = null;
  try {
    const data = await api(`/api/problems/${current.key}/reset`, {});
    loadingCode = true;
    editor.setValue(data.code);
    loadingCode = false;
    $("#output").innerHTML = '<p class="muted">Run your code to see results here.</p>';
    tc.results = null;
    renderTestCases();
    $("#save-state").textContent = data.backed_up ? "Reset (backup kept)" : "Reset";
  } catch (err) {
    $("#save-state").textContent = "Reset failed: " + err.message;
  }
}

let celebrateTimer;

function celebrate() {
  const results = $("#results");
  results.classList.remove("celebrate");
  void results.offsetWidth;
  results.classList.add("celebrate");
  clearTimeout(celebrateTimer);
  celebrateTimer = setTimeout(() => results.classList.remove("celebrate"), 1700);
  if (!matchMedia("(prefers-reduced-motion: no-preference)").matches) return;
  confettiBurst(results.querySelector("#output .summary.pass"));
}

function endCelebration() {
  clearTimeout(celebrateTimer);
  $("#results").classList.remove("celebrate");
  document.querySelector("#celebration")?.remove();
}

function confettiBurst(anchor) {
  document.querySelector("#celebration")?.remove();
  const rect = anchor.getBoundingClientRect();
  const layer = document.createElement("div");
  layer.id = "celebration";
  const colors = ["var(--pass)", "var(--accent)", "var(--warn)"];
  for (let i = 0; i < 20; i++) {
    const bit = document.createElement("i");
    const angle = Math.random() * Math.PI - Math.PI;
    const power = 70 + Math.random() * 140;
    bit.style.left = `${rect.left + Math.min(rect.width, 160) / 2}px`;
    bit.style.top = `${rect.top + rect.height / 2}px`;
    bit.style.setProperty("--c", colors[i % colors.length]);
    bit.style.setProperty("--dx", `${Math.cos(angle) * power}px`);
    bit.style.setProperty("--up", `${Math.sin(angle) * power - 40}px`);
    bit.style.setProperty("--fall", `${90 + Math.random() * 110}px`);
    bit.style.setProperty("--rot", `${(Math.random() - 0.5) * 900}deg`);
    bit.style.setProperty("--t", `${0.9 + Math.random() * 0.5}s`);
    layer.append(bit);
  }
  document.body.append(layer);
  setTimeout(() => layer.remove(), 1600);
}

async function run() {
  const btn = $("#run-btn");
  if (btn.disabled) return;
  btn.disabled = true;
  setPane("results");
  showResultsView("output");
  announce("Running…");
  $("#output").innerHTML = '<p class="muted">Running…</p>';
  clearTimeout(saveTimer);
  saveTimer = null;
  try {
    await flushTestCases().catch(() => {});
    const code = editor.getValue();
    const own = tc.cases.length
      ? api(`/api/problems/${current.key}/run-custom`, { code, cases: tc.cases }).catch(() => null)
      : Promise.resolve(null);
    const outcome = await api(`/api/problems/${current.key}/run`, { code });
    const ran = await own;
    tc.results = ran && ran.results && ran.results.length === tc.cases.length ? ran.results : null;
    renderTestCases();
    $("#output").innerHTML = renderResults(outcome);
    announce($("#output .verdict-row")?.textContent.replace(/\s+/g, " ").trim() || "");
    if ($("#output .summary.pass")) celebrate();
    $("#save-state").textContent = "Saved";
    const entry = problems.find((p) => p.key === current.key);
    if (entry && outcome.status) { entry.status = outcome.status; entry.due = outcome.due; renderList(); }
  } catch (err) {
    $("#output").innerHTML = `<pre class="error-box">${esc(err.message)}</pre>`;
    announce("Run failed: " + err.message);
  } finally {
    btn.disabled = false;
  }
}

function isLight() {
  return document.documentElement.dataset.theme === "light";
}

function renderThemeButton() {
  const btn = $("#theme-btn");
  btn.textContent = isLight() ? "☾ Dark" : "☀ Light";
  btn.title = isLight() ? "Switch to dark mode" : "Switch to light mode";
}

let themeLight = isLight();

function applyTheme() {
  if (themeLight) document.documentElement.dataset.theme = "light";
  else delete document.documentElement.dataset.theme;
  renderThemeButton();
  if (editor) monaco.editor.setTheme(themeLight ? "vs" : "vs-dark");
}

function toggleTheme() {
  themeLight = !themeLight;
  try {
    localStorage.setItem("theme", themeLight ? "light" : "dark");
  } catch (err) {
    // the choice still applies, it just resets when the page reloads
  }
  endCelebration();
  const animated = matchMedia("(prefers-reduced-motion: no-preference)").matches;
  if (animated && document.startViewTransition) document.startViewTransition(applyTheme);
  else applyTheme();
}

function initEditor() {
  const base = location.origin + "/vendor/monaco";
  self.MonacoEnvironment = {
    getWorkerUrl() {
      const src = `self.MonacoEnvironment={baseUrl:'${base}/'};importScripts('${base}/vs/base/worker/workerMain.js');`;
      return "data:text/javascript;charset=utf-8," + encodeURIComponent(src);
    },
  };
  editor = monaco.editor.create($("#editor"), {
    language: "python",
    theme: themeLight ? "vs" : "vs-dark",
    automaticLayout: true,
    minimap: { enabled: false },
    fontSize: matchMedia("(pointer: coarse)").matches ? 16 : 14,
    scrollBeyondLastLine: false,
    tabSize: 4,
    insertSpaces: true,
    quickSuggestions: false,
    suggestOnTriggerCharacters: false,
    wordBasedSuggestions: "off",
  });
  editor.onDidChangeModelContent(scheduleSave);
  editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, run);
}

async function start() {
  $("#run-hint").textContent = isMac ? "⌘↵" : "Ctrl+↵";
  renderThemeButton();
  $("#theme-btn").onclick = toggleTheme;
  roadmapView = initRoadmapView($("#roadmap-body"));
  $("#roadmap-zoom-in").onclick = () => roadmapView.zoomIn();
  $("#roadmap-zoom-out").onclick = () => roadmapView.zoomOut();
  $("#roadmap-fit").onclick = () => roadmapView.fit();
  $("#roadmap-btn").onclick = () => (roadmapOpen ? closeRoadmap() : openRoadmap());
  $("#roadmap-body").onclick = (e) => {
    const node = e.target.closest(".rm-node");
    if (node) selectRoadmapTopic(node);
    else closeRoadmapTopic(false);
  };
  $("#roadmap-body").onkeydown = (e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      selectRoadmapTopic(e.target.closest(".rm-node"), true);
    }
  };
  $("#roadmap-topic-close").onclick = () => closeRoadmapTopic();
  $("#stats-activity").onpointerover = (e) => {
    const cell = e.target.closest(".heat");
    if (cell) showHeatTip(cell);
  };
  $("#stats-activity").onpointerout = (e) => {
    if (e.target.closest(".heat")) hideHeatTip();
  };
  $("#random-btn").onclick = openRandomUnsolved;
  $("#clear-progress-btn").onclick = clearProgress;
  $("#roadmap-topic-list").onclick = (e) => {
    const row = e.target.closest(".problem-row");
    if (!row) return;
    openProblem(row.dataset.key);
  };
  $("#more-btn").onclick = () => setMoreMenu(!$("header").classList.contains("more-open"));
  $("#more-actions").addEventListener("click", (e) => {
    if (e.target.closest("button")) setMoreMenu(false);
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest("#more-btn, #more-actions")) setMoreMenu(false);
  });
  $("#tabs").onclick = (e) => {
    const tab = e.target.closest("[role=tab]");
    if (tab) setPane(tab.dataset.pane);
  };
  $("#tabs").onkeydown = (e) => {
    const tabs = [...document.querySelectorAll("#tabs [role=tab]")];
    const i = tabs.findIndex((t) => t.dataset.pane === document.body.dataset.pane);
    const next = e.key === "ArrowRight" ? tabs[(i + 1) % tabs.length] : e.key === "ArrowLeft" ? tabs[(i + tabs.length - 1) % tabs.length] : null;
    if (!next) return;
    e.preventDefault();
    setPane(next.dataset.pane);
    next.focus();
  };
  $("#menu-btn").onclick = () => setDrawer(true);
  $("#close-drawer").onclick = () => setDrawer(false);
  $("#scrim").onclick = () => setDrawer(false);
  $("#prev-btn").onclick = () => step(-1);
  $("#next-btn").onclick = () => step(1);
  $("#run-btn").onclick = run;
  $("#notes-text").oninput = scheduleNotes;
  setupSplitters();
  $("#reset-btn").onclick = resetCode;
  $("#solution-btn").onclick = showSolution;
  $("#confirm").addEventListener("click", (e) => {
    if (e.target === e.currentTarget) e.currentTarget.close("cancel");
  });
  $("#problem-search").oninput = (e) => {
    listQuery = e.target.value;
    renderList();
  };
  $("#problem-search").onkeydown = (e) => {
    if (e.key !== "Enter") return;
    const first = problems.find(matchesList);
    if (first) openProblem(first.key);
  };
  $("#problem-filter").onclick = (e) => {
    const btn = e.target.closest("[data-filter]");
    if (!btn) return;
    listFilter = btn.dataset.filter;
    renderList();
  };
  $("#next-up").onclick = (e) => openProblem(e.currentTarget.dataset.key);
  $("#problem-list").onclick = (e) => {
    const row = e.target.closest(".problem-row");
    if (row) openProblem(row.dataset.key);
  };
  $("#results-tabs").onclick = (e) => {
    const tab = e.target.closest("[data-view]");
    if (tab) showResultsView(tab.dataset.view);
  };
  $("#results-tabs").onkeydown = (e) => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    e.preventDefault();
    const view = e.key === "ArrowLeft" ? "testcase" : "output";
    showResultsView(view);
    $(`#tab-${view}`).focus();
  };
  $("#testcases").oninput = (e) => {
    if (e.target.matches("input[data-p]")) editTestCase(e.target);
  };
  $("#testcases").onclick = (e) => {
    const chip = e.target.closest(".tc-chip");
    if (chip) {
      tc.sel = Number(chip.dataset.i);
      renderTestCases();
    } else if (e.target.closest(".tc-add")) addTestCase();
    else if (e.target.closest(".tc-del")) deleteTestCase();
  };
  $("#results").onclick = (e) => {
    if (e.target.closest(".goto-testcase")) {
      showResultsView("testcase");
      return;
    }
    if (e.target.closest("#perf-btn")) {
      runPerf();
      return;
    }
    const next = e.target.closest("#next-problem");
    if (next) {
      openProblem(next.dataset.key);
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
      setMoreMenu(false);
      setDrawer(false);
      closeRoadmap();
      closeSolution();
    }
    if ((e.metaKey || e.ctrlKey) && e.key === "s") { e.preventDefault(); flushSave(); }
    if ((e.metaKey || e.ctrlKey) && e.key === "Enter" && !e.defaultPrevented && current && $("#roadmap").hidden && !$("#confirm").open && !$("#solution").open) {
      e.preventDefault();
      run();
    }
  });
  window.addEventListener("beforeunload", () => {
    if (tc.timer && current) {
      navigator.sendBeacon(`/api/problems/${current.key}/custom`, new Blob([JSON.stringify({ cases: tc.cases })], { type: "application/json" }));
    }
    if (notesTimer && current) {
      navigator.sendBeacon(`/api/problems/${current.key}/notes`, new Blob([JSON.stringify({ text: $("#notes-text").value })], { type: "application/json" }));
    }
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
