// The NeetCode roadmap: which topics unlock which. Positions are node centres in SVG units.
const ROADMAP_NODES = {
  "arrays-hashing": { label: ["Arrays & Hashing"], x: 932, y: 89 },
  "two-pointers": { label: ["Two Pointers"], x: 788, y: 252 },
  "stack": { label: ["Stack"], x: 1019, y: 232 },
  "binary-search": { label: ["Binary Search"], x: 574, y: 417 },
  "sliding-window": { label: ["Sliding Window"], x: 819, y: 418 },
  "linked-list": { label: ["Linked List"], x: 1080, y: 425 },
  "trees": { label: ["Trees"], x: 810, y: 578 },
  "tries": { label: ["Tries"], x: 593, y: 737 },
  "backtracking": { label: ["Backtracking"], x: 1023, y: 730 },
  "heap-priority-queue": { label: ["Heap / Priority", "Queue"], x: 738, y: 872 },
  "graphs": { label: ["Graphs"], x: 1013, y: 908 },
  "1d-dp": { label: ["1-D Dynamic", "Programming"], x: 1286, y: 906 },
  "intervals": { label: ["Intervals"], x: 335, y: 1035 },
  "greedy": { label: ["Greedy"], x: 602, y: 1099 },
  "advanced-graphs": { label: ["Advanced Graphs"], x: 835, y: 1065 },
  "2d-dp": { label: ["2-D Dynamic", "Programming"], x: 1117, y: 1112 },
  "bit-manipulation": { label: ["Bit Manipulation"], x: 1399, y: 1092 },
  "math-geometry": { label: ["Math & Geometry"], x: 1302, y: 1268 },
};

const ROADMAP_EDGES = [
  ["arrays-hashing", "two-pointers"],
  ["arrays-hashing", "stack"],
  ["two-pointers", "binary-search"],
  ["two-pointers", "sliding-window"],
  ["two-pointers", "linked-list"],
  ["binary-search", "trees"],
  ["linked-list", "trees"],
  ["trees", "tries"],
  ["trees", "heap-priority-queue"],
  ["trees", "backtracking"],
  ["heap-priority-queue", "intervals"],
  ["heap-priority-queue", "greedy"],
  ["heap-priority-queue", "advanced-graphs"],
  ["backtracking", "graphs"],
  ["backtracking", "1d-dp"],
  ["graphs", "advanced-graphs"],
  ["graphs", "2d-dp"],
  ["1d-dp", "2d-dp"],
  ["1d-dp", "bit-manipulation"],
  ["2d-dp", "math-geometry"],
  ["bit-manipulation", "math-geometry"],
];

const NODE_W = 210;
const NODE_LINE = 28;
const NODE_PAD = 76;

function nodeHeight(node) {
  return NODE_PAD + (node.label.length - 1) * NODE_LINE;
}

// `stats` maps a category to {solved, total, due}; `currentCat` is the topic of the open problem.
function renderRoadmap(stats, currentCat) {
  const edges = ROADMAP_EDGES.map(([from, to]) => {
    const a = ROADMAP_NODES[from];
    const b = ROADMAP_NODES[to];
    const y1 = a.y + nodeHeight(a) / 2;
    const y2 = b.y - nodeHeight(b) / 2;
    const mid = (y1 + y2) / 2;
    return `<path class="rm-edge" d="M${a.x},${y1} C${a.x},${mid} ${b.x},${mid} ${b.x},${y2}"/>`;
  }).join("");
  const nodes = Object.entries(ROADMAP_NODES).map(([cat, node]) => {
    const { solved, total, due = 0 } = stats[cat] || { solved: 0, total: 0 };
    const h = nodeHeight(node);
    const left = node.x - NODE_W / 2;
    const top = node.y - h / 2;
    const done = total > 0 && solved === total;
    const barW = NODE_W - 86;
    const here = cat === currentCat;
    const notes = [`${solved} of ${total} solved`, due ? `${due} due for review` : "", here ? "current topic" : ""].filter(Boolean).join(", ");
    const lines = node.label
      .map((line, i) => `<text x="${node.x}" y="${top + 31 + i * NODE_LINE}" text-anchor="middle">${esc(line)}</text>`)
      .join("");
    return `<g class="rm-node${done ? " done" : ""}${total ? "" : " empty"}${here ? " here" : ""}" data-cat="${cat}" role="button" tabindex="0"
        aria-label="${esc(node.label.join(" "))}, ${notes}">
      <title>${esc(node.label.join(" "))}: ${notes}</title>
      ${here ? `<rect class="rm-here" x="${left - 7}" y="${top - 7}" width="${NODE_W + 14}" height="${h + 14}" rx="15"/>` : ""}
      <rect class="rm-box" x="${left}" y="${top}" width="${NODE_W}" height="${h}" rx="9"/>
      ${lines}
      <rect class="rm-track" x="${left + 12}" y="${top + h - 22}" width="${barW}" height="8" rx="4"/>
      <rect class="rm-fill" x="${left + 12}" y="${top + h - 22}" width="${total ? (barW * solved) / total : 0}" height="8" rx="4"/>
      <text class="rm-count" x="${left + NODE_W - 12}" y="${top + h - 13}" text-anchor="end">${solved}/${total}</text>
      ${due ? `<circle class="rm-due" cx="${left + NODE_W - 4}" cy="${top + 4}" r="11"/>` : ""}
    </g>`;
  }).join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" role="group" aria-label="Roadmap"><g id="rm-viewport">${edges}${nodes}</g></svg>`;
}

const ROADMAP_BOUNDS = { x: 200, y: 20, w: 1340, h: 1310 };
const ROADMAP_ZOOM = { min: 0.2, max: 4 };

// Pan and zoom for the roadmap svg, kept as a translate+scale on #rm-viewport.
// The view survives re-renders; `fit()` recentres it.
function initRoadmapView(container) {
  const view = { scale: 1, x: 0, y: 0, ready: false, touched: false };
  const pointers = new Map();
  let drag = null;
  let pinch = null;
  let moved = false;

  const viewport = () => container.querySelector("#rm-viewport");

  function apply() {
    const g = viewport();
    if (g) g.setAttribute("transform", `translate(${view.x} ${view.y}) scale(${view.scale})`);
  }

  function fit() {
    const b = ROADMAP_BOUNDS;
    const { width, height } = container.getBoundingClientRect();
    if (!width || !height) return;
    view.scale = Math.min(width / b.w, height / b.h);
    view.x = (width - b.w * view.scale) / 2 - b.x * view.scale;
    view.y = (height - b.h * view.scale) / 2 - b.y * view.scale;
    view.ready = true;
    view.touched = false;
    apply();
  }

  // Zoom by `factor`, keeping the point (px, py) in container pixels fixed.
  function zoomAt(factor, px, py) {
    const scale = Math.min(ROADMAP_ZOOM.max, Math.max(ROADMAP_ZOOM.min, view.scale * factor));
    const k = scale / view.scale;
    view.x = px - (px - view.x) * k;
    view.y = py - (py - view.y) * k;
    view.scale = scale;
    view.touched = true;
    apply();
  }

  function zoomCentre(factor) {
    const { width, height } = container.getBoundingClientRect();
    zoomAt(factor, width / 2, height / 2);
  }

  container.addEventListener("wheel", (e) => {
    e.preventDefault();
    const rect = container.getBoundingClientRect();
    const speed = e.ctrlKey ? 0.01 : 0.0015;
    zoomAt(Math.exp(-e.deltaY * speed), e.clientX - rect.left, e.clientY - rect.top);
  }, { passive: false });

  const spread = () => {
    const [a, b] = [...pointers.values()];
    return { dist: Math.hypot(a.x - b.x, a.y - b.y), x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
  };

  container.addEventListener("pointerdown", (e) => {
    if (e.button !== 0) return;
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pointers.size === 2) {
      drag = null;
      moved = true;
      container.classList.add("panning");
      pinch = spread();
      return;
    }
    drag = { id: e.pointerId, sx: e.clientX, sy: e.clientY, vx: view.x, vy: view.y };
    moved = false;
  });

  container.addEventListener("pointermove", (e) => {
    if (pointers.has(e.pointerId)) pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pinch && pointers.size === 2) {
      const now = spread();
      const rect = container.getBoundingClientRect();
      zoomAt(now.dist / pinch.dist, pinch.x - rect.left, pinch.y - rect.top);
      view.x += now.x - pinch.x;
      view.y += now.y - pinch.y;
      apply();
      pinch = now;
      return;
    }
    if (!drag || e.pointerId !== drag.id) return;
    const dx = e.clientX - drag.sx;
    const dy = e.clientY - drag.sy;
    if (!moved) {
      if (Math.hypot(dx, dy) < 4) return;
      moved = true;
      container.setPointerCapture(e.pointerId);
      container.classList.add("panning");
    }
    view.touched = true;
    view.x = drag.vx + dx;
    view.y = drag.vy + dy;
    apply();
  });

  function endDrag(e) {
    pointers.delete(e.pointerId);
    if (pinch) {
      pinch = null;
      drag = null;
      if (pointers.size === 1) {
        const [id, at] = [...pointers.entries()][0];
        drag = { id, sx: at.x, sy: at.y, vx: view.x, vy: view.y };
      } else {
        container.classList.remove("panning");
      }
      return;
    }
    if (!drag || e.pointerId !== drag.id) return;
    drag = null;
    container.classList.remove("panning");
  }
  container.addEventListener("pointerup", endDrag);
  container.addEventListener("pointercancel", endDrag);

  // A drag that ends over a node must not count as a click on it.
  container.addEventListener("click", (e) => {
    if (!moved) return;
    moved = false;
    e.stopImmediatePropagation();
  }, true);

  // Keep the whole map in view when the window or orientation changes, unless the user has moved it.
  new ResizeObserver(() => {
    if (!view.touched) fit();
  }).observe(container);

  return {
    show() {
      if (view.ready) apply();
      else fit();
    },
    fit,
    zoomIn: () => zoomCentre(1.25),
    zoomOut: () => zoomCentre(0.8),
  };
}

const RING = { size: 190, r: 80, stroke: 11, gap: 16, start: 195 };
const RING_TIERS = [
  { name: "Easy", cls: "easy" },
  { name: "Medium", cls: "medium" },
  { name: "Hard", cls: "hard" },
];

function ringPoint(deg) {
  const rad = ((deg - 90) * Math.PI) / 180;
  const c = RING.size / 2;
  return `${(c + RING.r * Math.cos(rad)).toFixed(2)},${(c + RING.r * Math.sin(rad)).toFixed(2)}`;
}

function ringArc(from, to) {
  const large = to - from > 180 ? 1 : 0;
  return `M${ringPoint(from)} A${RING.r},${RING.r} 0 ${large} 1 ${ringPoint(to)}`;
}

// `counts` maps a difficulty to {solved, total}. Each difficulty gets an arc as long as its share of all problems.
function renderStats(counts) {
  const all = RING_TIERS.reduce((n, t) => n + (counts[t.name]?.total || 0), 0);
  const solved = RING_TIERS.reduce((n, t) => n + (counts[t.name]?.solved || 0), 0);
  const room = 360 - RING.gap * RING_TIERS.length;
  let at = RING.start;
  const arcs = RING_TIERS.map((t) => {
    const { solved: s = 0, total = 0 } = counts[t.name] || {};
    if (!total) return "";
    const span = (room * total) / all;
    const from = at;
    at += span + RING.gap;
    return `<path class="ring-track ${t.cls}" d="${ringArc(from, from + span)}"/>` +
      (s ? `<path class="ring-fill ${t.cls}" d="${ringArc(from, from + (span * s) / total)}"/>` : "");
  }).join("");
  const legend = RING_TIERS.map((t) => {
    const { solved: s = 0, total = 0 } = counts[t.name] || {};
    return `<div class="${t.cls}"><dt>${t.name}</dt><dd>${s}/${total}</dd></div>`;
  }).join("");
  const ring = `<svg viewBox="0 0 ${RING.size} ${RING.size}" aria-hidden="true" fill="none" stroke-linecap="round" stroke-width="${RING.stroke}">${arcs}</svg>
    <div class="ring-label"><strong>${solved}</strong><span>/${all}</span><span>Solved</span></div>`;
  return { legend, ring, label: `${solved} of ${all} solved: ${RING_TIERS.map((t) => `${counts[t.name]?.solved || 0} of ${counts[t.name]?.total || 0} ${t.name}`).join(", ")}` };
}

const HEAT_WEEKS = 22;
const HEAT_LEVELS = [1, 3, 6, 10];  // runs in a day needed for each shade after the first

function heatLevel(runs) {
  return runs ? 1 + HEAT_LEVELS.slice(1).filter((n) => runs >= n).length : 0;
}

const utcDay = (iso) => new Date(`${iso}T00:00:00Z`);

// Weeks run left to right, Sunday on top, and the last column ends on today.
function renderActivity(activity) {
  const today = utcDay(activity.today);
  const first = new Date(today);
  first.setUTCDate(first.getUTCDate() - today.getUTCDay() - (HEAT_WEEKS - 1) * 7);
  let cells = "";
  let active = 0;
  for (let i = 0; i < HEAT_WEEKS * 7; i++) {
    const day = new Date(first);
    day.setUTCDate(first.getUTCDate() + i);
    if (day > today) break;
    const iso = day.toISOString().slice(0, 10);
    const runs = activity.days[iso] || 0;
    if (runs) active += 1;
    const when = day.toLocaleDateString(undefined, { weekday: "short", month: "short", day: "numeric", year: "numeric", timeZone: "UTC" });
    cells += `<i class="heat l${heatLevel(runs)}" data-tip="${when}: ${runs ? `${runs} ${runs === 1 ? "run" : "runs"}` : "no runs"}"></i>`;
  }
  const streak = activity.current_streak;
  const label = `${active} active ${active === 1 ? "day" : "days"} in the last ${HEAT_WEEKS} weeks, `
    + `current streak ${streak} ${streak === 1 ? "day" : "days"}, longest ${activity.longest_streak}`;
  const best = activity.longest_streak;
  const captions = `<div class="heat-caption muted">Best streak: ${best} ${best === 1 ? "day" : "days"}</div>`
    + `<div class="heat-caption muted">Last ${HEAT_WEEKS} weeks</div>`;
  return { html: `${captions}<div class="heat-grid" role="img" aria-label="${label}">${cells}</div>`, label };
}

function streakText(streak) {
  return streak ? `${streak} day streak` : "";
}
