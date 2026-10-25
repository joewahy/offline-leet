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
const NODE_PAD = 66;

function nodeHeight(node) {
  return NODE_PAD + (node.label.length - 1) * NODE_LINE;
}

// `stats` maps a category to {solved, total}.
function renderRoadmap(stats) {
  const edges = ROADMAP_EDGES.map(([from, to]) => {
    const a = ROADMAP_NODES[from];
    const b = ROADMAP_NODES[to];
    const y1 = a.y + nodeHeight(a) / 2;
    const y2 = b.y - nodeHeight(b) / 2;
    const mid = (y1 + y2) / 2;
    return `<path class="rm-edge" d="M${a.x},${y1} C${a.x},${mid} ${b.x},${mid} ${b.x},${y2}"/>`;
  }).join("");
  const nodes = Object.entries(ROADMAP_NODES).map(([cat, node]) => {
    const { solved, total } = stats[cat] || { solved: 0, total: 0 };
    const h = nodeHeight(node);
    const left = node.x - NODE_W / 2;
    const top = node.y - h / 2;
    const done = total > 0 && solved === total;
    const barW = NODE_W - 24;
    const lines = node.label
      .map((line, i) => `<text x="${node.x}" y="${top + 31 + i * NODE_LINE}" text-anchor="middle">${esc(line)}</text>`)
      .join("");
    return `<g class="rm-node${done ? " done" : ""}${total ? "" : " empty"}" data-cat="${cat}" role="button" tabindex="0"
        aria-label="${esc(node.label.join(" "))}, ${solved} of ${total} solved">
      <title>${esc(node.label.join(" "))}: ${solved} / ${total} solved</title>
      <rect class="rm-box" x="${left}" y="${top}" width="${NODE_W}" height="${h}" rx="9"/>
      ${lines}
      <rect class="rm-track" x="${left + 12}" y="${top + h - 16}" width="${barW}" height="4" rx="2"/>
      <rect class="rm-fill" x="${left + 12}" y="${top + h - 16}" width="${total ? (barW * solved) / total : 0}" height="4" rx="2"/>
    </g>`;
  }).join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" role="group" aria-label="Roadmap"><g id="rm-viewport">${edges}${nodes}</g></svg>`;
}

const ROADMAP_BOUNDS = { x: 200, y: 20, w: 1340, h: 1310 };
const ROADMAP_ZOOM = { min: 0.2, max: 4 };

// Pan and zoom for the roadmap svg, kept as a translate+scale on #rm-viewport.
// The view survives re-renders; `fit()` recentres it.
function initRoadmapView(container) {
  const view = { scale: 1, x: 0, y: 0, ready: false };
  let drag = null;
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
    apply();
  }

  // Zoom by `factor`, keeping the point (px, py) in container pixels fixed.
  function zoomAt(factor, px, py) {
    const scale = Math.min(ROADMAP_ZOOM.max, Math.max(ROADMAP_ZOOM.min, view.scale * factor));
    const k = scale / view.scale;
    view.x = px - (px - view.x) * k;
    view.y = py - (py - view.y) * k;
    view.scale = scale;
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

  container.addEventListener("pointerdown", (e) => {
    if (e.button !== 0) return;
    drag = { id: e.pointerId, sx: e.clientX, sy: e.clientY, vx: view.x, vy: view.y };
    moved = false;
  });

  container.addEventListener("pointermove", (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    const dx = e.clientX - drag.sx;
    const dy = e.clientY - drag.sy;
    if (!moved) {
      if (Math.hypot(dx, dy) < 4) return;
      moved = true;
      container.setPointerCapture(e.pointerId);
      container.classList.add("panning");
    }
    view.x = drag.vx + dx;
    view.y = drag.vy + dy;
    apply();
  });

  function endDrag(e) {
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
