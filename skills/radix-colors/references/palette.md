# Radix Palette Reference

Companion to `SKILL.md`. Every scale below ships light, dark, alpha and P3 values, and every scale uses the
same 12-step contract: **1–2 page and panels, 3–5 surfaces, 6–8 borders, 9–10 solids, 11–12 text.**

## All scales by character

### Character index

| Character | Scales | Practical consequence |
| --- | --- | --- |
| Pastel / bright | mint, sky, lime, yellow, amber, gold | step 9 is light — dark labels only, good for tints and charts |
| Vivid | tomato, red, ruby, pink, orange, cyan, purple, violet, iris, blue, green, grass, jade, teal | the default accents; step 9 usually passes for large/UI text |
| Deep | crimson, plum, indigo, brown, bronze | editorial weight, strong at step 12, calmer at step 3 |
| Low-chroma / neutral | gray, mauve, slate, sage, olive, sand | use for chrome, never as the only colour in the product |

### Neutrals — pick exactly one

| Scale | Undertone | Character | Best for |
| --- | --- | --- | --- |
| `gray` | none | pure, invisible | dashboards, docs, admin, utilities, multi-brand products |
| `mauve` | violet | cool, modern | SaaS, AI tools, creator products, dark-first interfaces |
| `slate` | blue | cool, technical | fintech, infra, security, enterprise |
| `sage` | green | calm, botanical | health, wellness, sustainability |
| `olive` | yellow-green | warm-neutral, editorial | food, outdoor, organic, publishing |
| `sand` | orange-brown | warm, paper-like | commerce, hospitality, lifestyle, long-form reading |

### Warm — reds, oranges, yellows

| Scale | Character | Step 9 with white text | Best for |
| --- | --- | --- | --- |
| `tomato` | vivid red-orange | borderline — large text only | energetic consumer, editorial accents |
| `red` | pure red, warm | borderline — large text only | destructive, errors, alerts |
| `ruby` | cool red | borderline | destructive in cool palettes |
| `crimson` | deep pink-red | usually passes | premium, beauty, bold brand |
| `pink` | vivid magenta | borderline | consumer, social, playful |
| `orange` | vivid orange | borderline | CTAs, food, energy |
| `amber` | warm yellow-orange | fails — use dark ink | warnings, ratings, highlights |
| `yellow` | bright yellow | fails — use dark ink | attention, badges, notes |
| `gold` | metallic yellow | fails — use dark ink | luxury, editorial, trophies |
| `brown` | muted brown | passes | craft, coffee, publishing |
| `bronze` | metallic brown | borderline | luxury, hardware, jewellery |

### Purple and blue — brand workhorses

| Scale | Character | Step 9 with white text | Best for |
| --- | --- | --- | --- |
| `plum` | deep purple-pink | usually passes | creative tools, beauty |
| `purple` | vivid purple | usually passes | product UI, AI, creativity |
| `violet` | blue-violet | usually passes | dev tools, productivity |
| `iris` | vivid blue-purple | usually passes | default "modern SaaS" accent |
| `indigo` | deep blue | passes | enterprise, data, trust |
| `blue` | pure blue | borderline | links, info, the safest accent |
| `sky` | light cyan-blue | fails — use dark ink | weather, freshness, secondary accents |
| `cyan` | vivid cyan | borderline | dashboards, technical, health |

### Green and teal — success, growth, calm

| Scale | Character | Step 9 with white text | Best for |
| --- | --- | --- | --- |
| `teal` | blue-green | borderline | health, finance, calm utility |
| `jade` | restful green | borderline | success, money, wellness |
| `green` | pure green | borderline | success, confirmations |
| `grass` | natural green | borderline | sustainability, outdoors |
| `lime` | bright yellow-green | fails — use dark ink | fresh accents, charts |
| `mint` | light mint green | fails — use dark ink | soft accents, backgrounds |

Read "borderline" as **≈ 3:1 with white** — acceptable for large text, icons and UI fills, not for 14–16px body
copy. Anything marked "fails" needs dark ink or a step-12 label.

## Six ready-made palettes

Each pairing lists the exact steps to consume; the CSS shows the accent slot and the semantic roles. Swap the
grey and the accent, keep the step numbers.

### 1. Indie SaaS — `slate` + `iris` + `jade`

Cool, technical, confident. Iris carries the brand, jade confirms, red destroys.

```css
--page: var(--slate-1);   --panel: var(--slate-2);   --line: var(--slate-6);
--ink: var(--slate-12);   --ink-muted: var(--slate-11);
--accent-surface: var(--iris-3); --accent-border: var(--iris-6); --accent-ring: var(--iris-8);
--accent-solid: var(--iris-9); --accent-solid-hover: var(--iris-10); --accent-text: var(--iris-11);
--success: var(--jade-11); --danger: var(--red-11); --warning: var(--amber-11);
```

### 2. Editorial — `sand` + `tomato` + `gold`

Warm paper, ink-dark text, one hot accent. Reads like a magazine, not a dashboard.

```css
--page: var(--sand-2);    --panel: var(--sand-1);    --line: var(--sand-6);
--ink: var(--sand-12);    --ink-muted: var(--sand-11);
--accent-surface: var(--tomato-3); --accent-border: var(--tomato-6); --accent-ring: var(--tomato-8);
--accent-solid: var(--tomato-9); --accent-solid-hover: var(--tomato-10); --accent-text: var(--tomato-11);
--highlight: var(--gold-3); --highlight-ink: var(--gold-11);
```

### 3. Fintech — `slate` + `blue` + `jade`

Trust without a startup gradient. Blue for action, jade for gains, red for losses, amber for pending.

```css
--page: var(--slate-1);   --panel: var(--slate-2);   --line: var(--slate-6);
--ink: var(--slate-12);   --ink-muted: var(--slate-11);
--accent-surface: var(--blue-3); --accent-border: var(--blue-6); --accent-ring: var(--blue-8);
--accent-solid: var(--blue-9); --accent-solid-hover: var(--blue-10); --accent-text: var(--blue-11);
--positive: var(--jade-11); --negative: var(--red-11); --pending: var(--amber-11);
```

### 4. Health and wellness — `sage` + `teal` + `jade`

Low-arousal palette: green-grey structure, teal action, no pure red anywhere in the primary flow.

```css
--page: var(--sage-1);    --panel: var(--sage-2);    --line: var(--sage-6);
--ink: var(--sage-12);    --ink-muted: var(--sage-11);
--accent-surface: var(--teal-3); --accent-border: var(--teal-6); --accent-ring: var(--teal-8);
--accent-solid: var(--teal-9); --accent-solid-hover: var(--teal-10); --accent-text: var(--teal-11);
--success: var(--jade-11); --danger: var(--red-11);
```

### 5. Consumer app — `mauve` + `plum` + `amber`

Violet-grey chrome with a saturated plum accent; amber keeps the palette from going cold.

```css
--page: var(--mauve-1);   --panel: var(--mauve-2);   --line: var(--mauve-6);
--ink: var(--mauve-12);   --ink-muted: var(--mauve-11);
--accent-surface: var(--plum-3); --accent-border: var(--plum-6); --accent-ring: var(--plum-8);
--accent-solid: var(--plum-9); --accent-solid-hover: var(--plum-10); --accent-text: var(--plum-11);
--badge: var(--amber-3); --badge-ink: var(--amber-11); --badge-solid: var(--amber-9);
```

### 6. Data-heavy dashboard — `gray` + `blue`

Neutral chrome so the data owns the colour; six chart series, two scales apart in hue.

```css
--page: var(--gray-1);    --panel: var(--gray-2);    --line: var(--gray-6);
--ink: var(--gray-12);    --ink-muted: var(--gray-11);
--accent-solid: var(--blue-9); --accent-solid-hover: var(--blue-10); --accent-text: var(--blue-11);
--chart-1: var(--blue-9);  --chart-2: var(--jade-9);  --chart-3: var(--amber-9);
--chart-4: var(--purple-9); --chart-5: var(--cyan-9); --chart-6: var(--tomato-9);
--chart-grid: var(--gray-6); --chart-axis: var(--gray-11);
```

## Verifying contrast

Step 9 is tuned for a 3:1 fill, not for body copy. Run the pair you are about to ship:

```js
const ch = (c) => { const s = c / 255; return s <= 0.03928 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4; };
const lum = (h) => { const n = parseInt(h.slice(1), 16);
  const [r, g, b] = [n >> 16, (n >> 8) & 255, n & 255].map(ch);
  return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
const ratio = (a, b) => { const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05); };
const v = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();

ratio(v("--iris-9"), "#ffffff");          // ≥ 4.5 → white label is safe
ratio(v("--amber-9"), v("--gray-12"));    // dark ink on a bright solid
```

Pass marks: **4.5:1** for body text, **3:1** for large text (≥ 24px, or 19px bold) and for UI borders, icons
and focus rings. If a step-9 pair fails, keep the solid and switch the label to `--{scale}-12`, or pick a deeper
scale from the tables above.
