"""Draw a diagram of each visual problem's first example (trees, linked lists, grids).

For every problem that has one this writes diagram.svg next to its README and links it from the
Examples section with `![...](diagram.svg)`. The picture is drawn from the first case in tests.json, so it
always matches the example. Colours come from the app's CSS variables, so the diagram follows the theme.

    python tools/diagrams.py        (re-)draw every diagram; build.py runs this after the READMEs are written
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from leet.problems import all_problems  # noqa: E402
from leet.structures import list_from, list_cycle_from, tree_from  # noqa: E402

LINK = "![Diagram of example 1](diagram.svg)"
LINK_LINE = re.compile(r"^!\[[^\]]*\]\(diagram\.svg\)\n\n?", re.MULTILINE)
INF = 2147483647

TEXT = "fill:var(--text,#1b1f24)"
MUTED = "fill:var(--muted,#5f6b7d)"
LINE = "stroke:var(--muted,#5f6b7d);stroke-width:1.5;fill:none"
SHAPE = "fill:var(--code-bg,#eef0f3);stroke:var(--muted,#5f6b7d);stroke-width:1.5"
LABEL_H = 22
GAP = 14
PAD = 12


def esc(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, value, style=TEXT, size=13, anchor="middle", weight=None):
    bold = f' font-weight="{weight}"' if weight else ""
    return (f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" dominant-baseline="central" '
            f'font-size="{size}"{bold} style="{style}">{esc(value)}</text>')


def label(name):
    return text(0, LABEL_H / 2, name, MUTED, 12, "start", 600)


# Each drawer returns (width, height, svg markup) for one structure, with the origin at its top-left.

def draw_tree(values):
    root = tree_from(values)
    if root is None:
        return 60, 26, text(30, 13, "empty", MUTED, 12)
    dx, dy, r = 38, 50, 16
    pos, counter = {}, [0]

    def place(node, depth):
        if node.left:
            place(node.left, depth + 1)
        pos[id(node)] = (counter[0] * dx + r, depth * dy + r)
        counter[0] += 1
        if node.right:
            place(node.right, depth + 1)

    place(root, 0)
    edges, nodes, stack = [], [], [root]
    while stack:
        node = stack.pop()
        x, y = pos[id(node)]
        for child in (node.left, node.right):
            if child:
                cx, cy = pos[id(child)]
                edges.append(f'<line x1="{x}" y1="{y}" x2="{cx}" y2="{cy}" style="{LINE}"/>')
                stack.append(child)
        nodes.append(f'<circle cx="{x}" cy="{y}" r="{r}" style="{SHAPE}"/>' + text(x, y, node.val))
    width = counter[0] * dx - dx + 2 * r
    height = max(y for _, y in pos.values()) + r
    return width, height, "".join(edges + nodes)


def draw_list(values, cycle_to=-1):
    if not values:
        return 60, 26, text(30, 13, "empty", MUTED, 12)
    w, h, gap = 38, 28, 26
    top = 22 if cycle_to >= 0 else 0
    parts, xs = [], []
    x = 0
    for v in values:
        xs.append(x)
        parts.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="5" style="{SHAPE}"/>'
                     + text(x + w / 2, top + h / 2, v))
        x += w + gap
    mid = top + h / 2
    for a, b in zip(xs, xs[1:]):
        parts.append(f'<path d="M{a + w + 2} {mid} H{b - 6}" style="{LINE}"/>'
                     f'<path d="M{b - 11} {mid - 4} L{b - 3} {mid} L{b - 11} {mid + 4}" style="{LINE}"/>')
    end = xs[-1] + w
    if cycle_to >= 0:
        back = xs[cycle_to] + w / 2
        last = xs[-1] + w / 2
        parts.append(f'<path d="M{last} {top} C{last} 0 {back} 0 {back} {top - 6}" style="{LINE}"/>'
                     f'<path d="M{back - 4} {top - 12} L{back} {top - 4} L{back + 4} {top - 12}" style="{LINE}"/>')
        return end, top + h, "".join(parts)
    parts.append(f'<path d="M{end + 2} {mid} H{end + gap - 6}" style="{LINE}"/>'
                 + text(end + gap + 12, mid, "null", MUTED, 12))
    return end + gap + 28, top + h, "".join(parts)


def grid_fill(problem_id, value):
    """(fill style, shown text) for one cell; the cell colours say what each value means."""
    soft = "fill-opacity:.35"
    if problem_id in (80, 81):
        land = str(value) == "1"
        return (f"fill:var(--accent,#1a64d8);{soft}" if land else "fill:none"), value
    if problem_id == 84:
        return {1: (f"fill:var(--pass,#1a7f37);{soft}", value),
                2: (f"fill:var(--fail,#cf222e);{soft}", value)}.get(value, ("fill:none", value))
    if problem_id == 83:
        if value == -1:
            return "fill:var(--muted,#5f6b7d);fill-opacity:.5", "wall"
        if value == 0:
            return f"fill:var(--accent,#1a64d8);{soft}", "gate"
        return "fill:none", "∞" if value == INF else value
    if problem_id == 86:
        return (f"fill:var(--muted,#5f6b7d);fill-opacity:.5" if value == "X" else "fill:none"), value
    return "fill:none", value


def draw_grid(problem_id, rows):
    size = 38 if problem_id == 83 else 30
    parts = []
    for r, row in enumerate(rows):
        for c, value in enumerate(row):
            fill, shown = grid_fill(problem_id, value)
            parts.append(f'<rect x="{c * size}" y="{r * size}" width="{size}" height="{size}" '
                         f'style="stroke:var(--muted,#5f6b7d);stroke-width:1;{fill}"/>'
                         + text(c * size + size / 2, r * size + size / 2, shown, TEXT, 11 if len(str(shown)) > 2 else 13))
    return len(rows[0]) * size, len(rows) * size, "".join(parts)


GRID_PROBLEMS = {80, 81, 83, 84, 86}


def blocks(problem):
    """[(label, (width, height, markup))] for the first example, or [] when there is nothing to draw."""
    case = problem.load_cases()[0]
    args, expected = case["args"], case["expected"]
    names = problem.param_names()
    kinds = problem.arg_types or (["tree"] if (problem.roundtrip or {}).get("type") == "tree" else [])
    out = []
    if problem.id in GRID_PROBLEMS:
        out.append((names[0], draw_grid(problem.id, args[0])))
        if problem.inplace is not None:
            out.append(("after", draw_grid(problem.id, expected)))
        return out
    for name, kind, value in zip(names, kinds, args):
        if kind == "tree":
            out.append((name, draw_tree(value)))
        elif kind == "list_node":
            out.append((name, draw_list(value)))
        elif kind == "list_cycle":
            out.append((name, draw_list(value[0], value[1])))
        elif kind == "list_of_list_node":
            out.extend((f"{name}[{i}]", draw_list(v)) for i, v in enumerate(value))
    if problem.return_type == "tree":
        out.append(("output", draw_tree(expected)))
    elif problem.return_type == "list_node" or (problem.inplace is not None and "list_node" in kinds):
        out.append(("output", draw_list(expected)))
    return out


def render(items, title):
    width = max(w for _, (w, _, _) in items) + 2 * PAD
    y = PAD
    body = []
    for name, (w, h, markup) in items:
        body.append(f'<g transform="translate({PAD},{y})">{label(name)}'
                    f'<g transform="translate(0,{LABEL_H})">{markup}</g></g>')
        y += LABEL_H + h + GAP
    height = y - GAP + PAD
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:g} {height:g}" width="{width:g}" '
            f'height="{height:g}" role="img" aria-label="{esc(title)}" '
            f'font-family="ui-sans-serif, system-ui, sans-serif">{"".join(body)}</svg>\n')


def link(readme):
    """README text with the diagram line placed after the first code block of the Examples section."""
    text_ = LINK_LINE.sub("", readme)
    start = text_.find("## Examples")
    if start == -1:
        return text_
    opening = text_.find("```", start)
    closing = text_.find("```", opening + 3) if opening != -1 else -1
    if closing == -1:
        return text_
    end = text_.find("\n", closing) + 1
    return text_[:end] + f"\n{LINK}\n" + text_[end:]


def apply(problem):
    svg_path = problem.dir / "diagram.svg"
    items = blocks(problem)
    readme = problem.readme_path
    if not items:
        svg_path.unlink(missing_ok=True)
        readme.write_text(LINK_LINE.sub("", readme.read_text()))
        return False
    svg_path.write_text(render(items, f"Diagram of example 1 of {problem.title}"))
    readme.write_text(link(readme.read_text()))
    return True


def apply_all():
    return sum(apply(p) for p in all_problems())


if __name__ == "__main__":
    print(f"drew diagrams for {apply_all()} problems")
