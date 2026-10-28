# Font Loading — Strategy, Metrics, Verification

Everything here assumes the packages are already installed and imported (see the main `SKILL.md`). This file is
about **which bytes hit the wire, when, and how to prove it**.

## 1. Pick the loading strategy by surface

| Surface | Display value | Preload | Notes |
| --- | --- | --- | --- |
| Marketing / landing | `swap` | 1 file (display or body latin) | The brand face must appear on first load |
| Product UI / dashboard | `swap` | 1 file (body latin) | Text must be readable before the font arrives |
| Long-form editorial | `swap` | 1–2 files | Body face first; italic is fetched on demand |
| Decorative display face | `optional` | 0–1 | If it misses the first load, cache serves it next time |
| Docs / admin / internal | system stack | none | Do not ship a webfont at all |

`font-display: block` is never the answer: it hides text for up to 3 s. `fallback` sits between `swap` and
`optional` and is rarely worth the extra state to reason about.

## 2. What actually gets downloaded

Fontsource CSS is a list of `@font-face` rules, one per subset, each with a `unicode-range`. The browser downloads a
file **only when a character on the page falls inside that range**. Real example, `@fontsource-variable/inter`:

```css
/* inter-latin-wght-normal — the one English pages use (value wrapped for readability) */
unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308,
              U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;

/* inter-cyrillic-ext-wght-normal — downloaded only if a Cyrillic glyph renders */
unicode-range: U+0460-052F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
```

Consequences:

- A page with only Latin text on `@fontsource-variable/inter` fetches **one** 47 KB file, not seven.
- A stray Cyrillic character in a testimonial pulls a whole extra subset. Sanitise user content or accept it.
- The build still *contains* every subset file unless you import a subset-specific static file. Bundle size on disk
  is a deployment concern; network size is a `unicode-range` concern.

### Cutting weight deliberately

| Goal | Move |
| --- | --- |
| English-only static site | `@fontsource/inter/latin-400.css` — one subset, one weight, 23 KB |
| English-only with variable | Import the package normally; the browser fetches latin only |
| Drop the optical-size axis | `@fontsource-variable/newsreader` (wght, 56 KB) instead of `opsz.css` (128 KB) |
| Narrow the weight axis | Build-time instancing with `fonttools varLib.instancer`, then self-host the result |
| Fewer weights | Variable package, use `font-weight: 400`/`500`/`600` from one file |

## 3. Framework wiring

### Vite / Astro / SvelteKit

```js
// entry file
import "@fontsource-variable/inter";
import interUrl from "@fontsource-variable/inter/files/inter-latin-wght-normal.woff2?url";
```

```html
<link rel="preload" as="font" type="font/woff2" href="/..." crossorigin="anonymous" />
```

In Astro the `?url` import works in a frontmatter script; in SvelteKit put it in `+layout.svelte` and pass it into
`<svelte:head>`. `crossorigin="anonymous"` is **required** even for same-origin fonts — without it the preload is
discarded and the file is fetched twice.

### Next.js (App Router)

Two valid paths:

```ts
// A. next/font/local — automatic preload + metric-adjusted fallback
import localFont from "next/font/local";
export const inter = localFont({
  src: "../node_modules/@fontsource-variable/inter/files/inter-latin-wght-normal.woff2",
  weight: "100 900",
  display: "swap",
  variable: "--font-sans",
});
```

```ts
// B. plain CSS import — works, but you own the fallback metrics and the preload
import "@fontsource-variable/inter";
```

Prefer A when the family is on the critical path; B is fine for a second family or a mono used below the fold.

### webpack

`css-loader` + `asset/resource` handles the `url()` references inside Fontsource CSS with no extra config. The
`?url` import in the preload example is a **Vite convention** — under webpack resolve the file instead:

```js
const interUrl = new URL("@fontsource-variable/inter/files/inter-latin-wght-normal.woff2", import.meta.url).href;
```

## 4. Metric overrides: the real fix for swap CLS

A swap changes x-height, advance widths and line box height. `size-adjust` rescales the fallback so the line boxes
match; `ascent-override` / `descent-override` / `line-gap-override` correct the vertical metrics.

```css
/* Inter vs Arial — approximate; regenerate for your exact build (see below) */
@font-face {
  font-family: "Inter Fallback";
  src: local("Arial");
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22.4%;
  line-gap-override: 0%;
}
:root { --font-sans: "Inter Variable", "Inter Fallback", Arial, sans-serif; }
```

Do not hand-guess numbers for other families. Generate them (`capsize`, `fontkit` metric extraction, or the Next.js
fallback generator) and re-measure CLS in the field. One fallback face per family is enough; two is a smell.

## 5. CJK and complex scripts

`@fontsource/noto-sans-sc@5.3.x` ships **918 woff2 files**: 97 unicode-range slices × 9 weights, plus the latin
faces, at roughly 2 KB per slice. This is not a bug — it is how CJK has to work on the web.

- The browser fetches only the slices whose characters appear, typically 3–8 per page. That is acceptable.
- Never preload a CJK file; you cannot predict which slices the page needs.
- Always pair with a system CJK fallback and `font-display: swap`; the first paint will be the system face.
- Arabic / Devanagari / Thai need their own families (`noto-naskh-arabic`, `noto-sans-devanagari`,
  `noto-sans-thai`) plus `dir` and `lang`. Do not let a Latin family "fall back" into them.

## 6. Verify what shipped

1. **Network panel**, filter `Font`. Count files and bytes on a cold load with cache disabled. Expect 1–3.
2. **`document.fonts`** in the console:
   ```js
   [...document.fonts].map(f => `${f.family} ${f.weight} ${f.status}`)
   ```
   Anything `unloaded` is declared but unused — fine. Anything `error` is a broken path.
3. **Disable the font in DevTools** (Rendering → "Disable local fonts") to see the fallback. If the layout jumps
   more than a couple of pixels, the metric overrides are wrong or missing.
4. **Lighthouse / Web Vitals**: `CLS` on the font swap shows up as layout shift right after first paint; `LCP`
   regressions usually mean a preload is competing with the hero image.
5. **Build output**: `du -sh dist/assets/*.woff2` — if you see seven subsets for a one-language site, switch to
   `latin-*.css` imports.

## 7. Budgets

| Asset | Target |
| --- | --- |
| Total font bytes, first load | ≤ 110 KB |
| Files preloaded | ≤ 2 |
| Families | ≤ 3 |
| Weights per family | ≤ 3 (variable counts as one) |
| Italic | only if the design actually uses `<em>` |
| Mono | lazy, or one weight only |
