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
  return `<svg viewBox="200 20 1340 1310" xmlns="http://www.w3.org/2000/svg" role="group" aria-label="Roadmap">${edges}${nodes}</svg>`;
}
