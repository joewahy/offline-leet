---
name: offline-leet
description: A calm, editor-native workbench for practicing the NeetCode 150 offline.
colors:
  bench: "#14171c"
  panel: "#1b1f26"
  hairline: "#2d333c"
  ink: "#e6e8eb"
  muted-ink: "#8b95a3"
  code-well: "#242a33"
  signal-blue: "#4c8dff"
  signal-blue-ink: "#0b0d10"
  pass-green: "#3fb950"
  fail-coral: "#ff7b72"
  warn-amber: "#d29922"
  bench-light: "#ffffff"
  panel-light: "#f6f7f9"
  hairline-light: "#dfe2e7"
  ink-light: "#1b1f24"
  muted-ink-light: "#5f6b7d"
  code-well-light: "#eef0f3"
  signal-blue-light: "#1a64d8"
  signal-blue-ink-light: "#ffffff"
  pass-green-light: "#1a7f37"
  fail-coral-light: "#cf222e"
  warn-amber-light: "#9a6700"
typography:
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.5
  header-title:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.5
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "0.04em"
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.5
  code:
    fontFamily: "ui-monospace, \"SF Mono\", Menlo, monospace"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  xs: "2px"
  sm: "4px"
  md: "6px"
  lg: "10px"
  xl: "12px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "22px"
components:
  button-default:
    backgroundColor: "{colors.bench}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "5px 12px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "5px 12px"
  button-primary:
    backgroundColor: "{colors.signal-blue}"
    textColor: "{colors.signal-blue-ink}"
    rounded: "{rounded.md}"
    padding: "5px 12px"
  button-danger:
    backgroundColor: "{colors.fail-coral}"
    textColor: "{colors.signal-blue-ink}"
    rounded: "{rounded.md}"
    padding: "5px 12px"
  pill-easy:
    textColor: "{colors.pass-green}"
    rounded: "{rounded.pill}"
    padding: "1px 8px"
  pill-medium:
    textColor: "{colors.warn-amber}"
    rounded: "{rounded.pill}"
    padding: "1px 8px"
  pill-hard:
    textColor: "{colors.fail-coral}"
    rounded: "{rounded.pill}"
    padding: "1px 8px"
  search-input:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "6px 10px"
  case-row:
    backgroundColor: "{colors.bench}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "6px 10px"
  hint-card:
    backgroundColor: "{colors.bench}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "8px 10px"
  problem-row:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "6px 8px"
  problem-row-current:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  dialog:
    backgroundColor: "{colors.bench}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: "22px 24px 18px"
  code-block:
    backgroundColor: "{colors.code-well}"
    textColor: "{colors.ink}"
    typography: "{typography.code}"
    rounded: "{rounded.md}"
    padding: "10px 12px"
---

# Design System: offline-leet

## Overview

**Creative North Star: "The Quiet Workbench"**

offline-leet is a bench where the work sits in plain view: a statement on the left, an editor on the right, results underneath. The surfaces are calm, tonal and editor-native, close enough to a code editor that nothing has to be learned. Chrome stays out of the way so the problem, the code and the verdict carry the screen. Because the same person returns daily, the interface is predictable first and expressive only at one moment: a solve.

The system is utilitarian by conviction. Panels differ from the page by a small tonal step and a one-pixel hairline, not by shadow or color. A single blue signal marks the thing to act on or where you are. Green, amber and coral are reserved for meaning (pass, due or medium, fail or hard); they are never decoration. Everything works with the network off, so type is the system font stack and the editor is vendored.

The system rejects gamified streak, XP and badge dashboards: celebration is brief, tied to a solve, and never accumulates into a score. It also rejects any remote asset, including web fonts and CDNs.

**Key Characteristics:**
- Dark by default, with a full light theme that mirrors it token for token.
- Tonal layering with hairline borders; shadows only on things that float.
- One blue accent used for action, focus and "you are here".
- Semantic color carries state (solved, due, failed, difficulty), nothing else.
- System sans and system mono; no downloaded type.
- One expressive moment (the solve glow and confetti), switched off under reduced motion.
- Phone layout reorganizes into tabs with 44px touch targets rather than shrinking the desktop.

## Colors

A cool blue-gray ladder with one saturated blue and three semantic signals. Values below are the dark theme; light counterparts are the `-light` tokens in the frontmatter and are chosen to clear AA on their panels.

### Primary
- **Signal Blue** (#4c8dff, light #1a64d8): the only accent. Primary buttons, focus rings, active splitter, current-topic ring on the roadmap, hint summaries, the "next up" outline, selected tab. Text on it is Signal Blue Ink (#0b0d10 dark, #ffffff light).

### Semantic
- **Pass Green** (#3fb950, light #1a7f37): solved marks, passing summaries, Easy pill, hidden-tests-passed rule, roadmap progress fill and completed topics.
- **Warn Amber** (#d29922, light #9a6700): review due marks and dots, Medium pill, slower-than-reference verdicts.
- **Fail Coral** (#ff7b72, light #cf222e): failing summaries, error text, Hard pill, destructive confirm button.

### Neutral
- **Bench** (#14171c, light #ffffff): page background and the inside of cards, cases and dialogs.
- **Panel** (#1b1f26, light #f6f7f9): header, results, hints, drawer tools; one tonal step from Bench.
- **Hairline** (#2d333c, light #dfe2e7): every border and divider, and the idle splitter.
- **Code Well** (#242a33, light #eef0f3): inline code and code blocks.
- **Ink** (#e6e8eb, light #1b1f24): primary text.
- **Muted Ink** (#8b95a3, light #5f6b7d): labels, counts, secondary text. Light value is tuned for AA on Panel and Code Well.

### Named Rules
**The One Signal Rule.** Blue appears only where the user can act or where they are. Never as a surface fill for large areas and never for status.

**The Meaning-Only Rule.** Green, amber and coral state something true (passed, due, failed, difficulty). A color that would only decorate is replaced by Ink or Muted Ink.

**The Mirror Rule.** Every dark token has a light twin with the same role. New colors are added to both themes together.

## Typography

**Display Font:** none; the system stack is used throughout (`-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`).
**Body Font:** the same system sans.
**Label/Mono Font:** `ui-monospace, "SF Mono", Menlo, monospace` for code, test values and keyboard hints.

**Character:** Native and unassuming. The sans reads like the host operating system; the mono is the editor's, so statement code, results and the Monaco editor feel like one voice.

### Hierarchy
- **Title** (600, 20px, 1.5): the problem name at the top of the statement.
- **Header title** (600, 15px, 1.5): the current problem in the app bar.
- **Body** (400, 14px, 1.5): statements, hints, results. Statement text is not width-capped; the panel width bounds it.
- **Label** (600, 11 to 14px, +0.04 to 0.05em, uppercase): statement section headings and drawer category headings, in Muted Ink.
- **Caption** (400, 12px): counts, save state, performance table, notes.
- **Code** (400, 13px, mono): inline code on Code Well with 4px radius, blocks with 6px radius. Editor text is 14px (16px on coarse pointers).

### Named Rules
**The System Voice Rule.** No web fonts, ever. Hierarchy comes from weight (400 and 600 only), size and Muted Ink, not from a second family.

**The Tabular Rule.** Numbers that update in place (roadmap solved counts today; ratios and timings as they are added) use tabular figures so they do not jitter.

## Layout

Two-pane workbench under a single app bar. The statement column is 38% wide (min 300px) with hints pinned beneath it; the work column holds the editor above the results (38% tall, min 110px). Both dividers are draggable, double-click resets, and they are keyboard focusable with arrow keys. The page is full-viewport with no outer scroll; each pane scrolls itself.

Spacing is a compact 4/8/12/16 rhythm with 22px statement gutters and 14px bar gutters. Density is deliberate: a tool for long sessions, not a marketing page.

The Problems list is a 340px drawer from the left over a scrim; the Roadmap replaces the main area entirely and brings a topic panel in from the right (340px, max 50%). Both are modal-feeling surfaces over the same workbench.

At 800px and below the panes stack. At 700px and below the layout becomes tabs: Problem, Code and Results along the bottom, with Run floating at the bottom right, and Solution, Reset and Theme folded under a More menu. Touch devices get 44px minimum targets and 16px inputs. The roadmap panel becomes a bottom sheet and supports pinch zoom.

### Named Rules
**The Pane Memory Rule.** Sizes the user sets are remembered per browser; layout never resets itself on navigation.

**The Reflow Rule.** Phones get a different arrangement (tabs, More menu), not a scaled-down desktop.

## Elevation & Depth

The system is tonal and flat at rest. Depth is one step from Bench to Panel plus a one-pixel Hairline. Shadows exist only on elements that float over the work, and they are soft and wide: the Problems drawer (`4px 0 24px rgba(0,0,0,.18)`), the roadmap topic panel (`-4px 0 24px rgba(0,0,0,.18)`), the mobile More menu (`0 8px 24px rgba(0,0,0,.25)`), the topic bottom sheet (`0 -8px 24px rgba(0,0,0,.18)`), and dialogs (`0 12px 40px rgba(0,0,0,.3)` for the solution, `0 16px 48px rgba(0,0,0,.4)` for confirm). Dialog backdrops are 50% black with a 2px blur. Roadmap boxes carry a small drop shadow (`0 3px 4px rgba(0,0,0,.25)`).

### Named Rules
**The Float-Only Rule.** A shadow means "this sits above the workbench". Panels, cards and rows that live in the page never get one.

## Shapes

Gently rounded and consistent: 6px is the working radius (buttons, inputs, cases, hints, rows, code blocks, drawer rows), 4px for inline code, 2px for confetti pieces, 10 to 12px for dialogs and the mobile menu, and a full pill for difficulty badges. Borders are 1px Hairline. The only dashed lines are deliberate: the "you are here" ring on the roadmap and the divider above the performance check. The pass and fail callouts use a 3px left rule instead of a box.

## Components

### Buttons
- **Shape:** 6px radius, 1px Hairline border, 5px by 12px padding, inherited font.
- **Default:** Bench fill, Ink text. Hover swaps the border to Muted Ink.
- **Ghost:** transparent fill; the standard for header actions, filters and close buttons.
- **Primary:** Signal Blue fill and border, Signal Blue Ink text, weight 600. Used for Run and confirm.
- **Danger:** primary shape in Fail Coral, for destructive confirmation.
- **Focus:** 2px Signal Blue outline with 1px offset. Disabled sits at 60% opacity.
- **Touch:** 44px minimum height on coarse pointers and under 700px.

### Pills
- Difficulty only: 11px, 600, 1px currentColor border, full radius, colored Pass Green (Easy), Warn Amber (Medium) or Fail Coral (Hard). In list rows the border and padding are dropped to plain colored text.

### Inputs / Fields
- **Style:** Panel fill, 1px Hairline, 6px radius, 6px by 10px padding, Ink text. The search field is the only text input.
- **Focus:** 2px Signal Blue outline, 1px offset.
- **Touch:** 16px text to avoid zoom on iOS.

### Filter Segment
- Three ghost buttons in a row with transparent borders; the active one gets Panel fill, Hairline border and weight 600, announced with `aria-pressed`.

### Problem Rows
- Single-line rows: status glyph, right-aligned number, name, difficulty. Hover and current both use Panel fill; current is also 600 weight. Solved glyph is Pass Green and bold, due is Warn Amber.

### Test Cases
- Collapsed rows on Bench with a Hairline border and 6px radius: a bold mark (Pass Green or Fail Coral), then a one-line mono preview in Muted Ink that ellipsizes. Expanding reveals a two-column definition list (input, expected, output, error, printed) in `pre` wells. Passed cases fold into a single summary line.

### Hints
- Each hint is its own collapsed card with a Signal Blue summary; nothing is revealed until opened. The hints region sits in Panel under the statement and scrolls independently.

### Dialogs
- Solution and Confirm: Bench fill, Hairline border, 10 to 12px radius, 50% blurred backdrop, entrance of 8px rise and 0.97 scale over 0.2s. The confirm dialog focuses its primary button on open; Cancel is a ghost button beside it.

### Drawer and Scrim
- The Problems drawer slides in over a 35% scrim in 0.28s and out in 0.18s; reduced motion removes the animation entirely.

### Roadmap Node (signature)
- A rounded SVG box on a dotted-grid canvas (24px dots in Hairline). Fill is a 45% mix of Signal Blue into Bench; completed topics mix Pass Green instead. Inside: the topic name (600), a solved count in tabular figures, and a progress bar (track at 22% Ink, fill Pass Green). A Warn Amber dot marks a review due; a dashed Signal Blue ring marks the current topic; hover, focus and selection add a Signal Blue stroke. Edges are 3px Muted Ink lines at 55% opacity. Panning is by drag, zoom by pinch or buttons.

### Solve Celebration (signature)
- On a first full pass, a fixed layer pulses an inset Pass Green edge and a soft green interior glow for 1.8s, and 20 small confetti pieces (Pass Green, Signal Blue, Warn Amber) burst from the summary. It is removed after 1.6s and absent under reduced motion. It is the only expressive animation in the product.

### Navigation
- The app bar is Panel with a Hairline bottom: Roadmap and Problems ghost buttons at left, the problem title with difficulty pill, save state, Solution, Reset, Theme, previous and next arrows, and Run last. Under 700px, secondary actions fold into More, Run floats bottom right, and a three-tab bar takes the bottom edge.

## Do's and Don'ts

### Do:
- **Do** build new surfaces from Bench and Panel plus 1px Hairline borders; use 6px radius by default.
- **Do** pair every new color with a light-theme twin and check AA (4.5:1 for text) in both themes.
- **Do** reserve Signal Blue for actions, focus and current location; use green, amber and coral only for pass, due or medium, and fail or hard.
- **Do** use the system font stacks and the vendored Monaco editor; keep all assets local.
- **Do** keep touch targets at 44px minimum on coarse pointers and under 700px.
- **Do** wrap any new motion in `prefers-reduced-motion: no-preference`, with entrances around 0.2 to 0.3s on ease-out and exits shorter.
- **Do** keep the solve moment short, tied to a result, and never cumulative.

### Don't:
- **Don't** add streak counters, XP, levels, badges or any gamified score dashboard.
- **Don't** load web fonts, CDN scripts or styles, analytics, or any remote asset.
- **Don't** put shadows on panels, rows, cards or cases that sit inside the page; shadows are for floating layers.
- **Don't** use Signal Blue as a large surface fill or to express status.
- **Don't** hard-code off-palette hues; derive tints with `color-mix` from the existing tokens.
- **Don't** reveal solutions, hints or spoilers by default; reveals are always an explicit action.
- **Don't** shrink the desktop layout for phones; reorganize it into tabs instead.
