# Type Pairings — Fontsource

Six pairings, each one **display + text + mono**, every package verified to exist on npm as of Fontsource v5.3.x.
File sizes are the `latin` woff2 of the normal `wght` face as shipped; italics cost roughly the same again.

Rule that keeps the page coherent: the display face carries the brand, the text face carries the reading, the mono
carries the numbers. If you cannot name the job of all three, drop one.

## The six at a glance

| # | Pairing | Display | Text | Mono | Latin KB | Signals |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Editorial | `newsreader` | `inter` | `jetbrains-mono` | 142 | Authored, edited, calm authority |
| 2 | Institutional | `source-serif-4` | `public-sans` | `ibm-plex-mono` | 89 | Trustworthy, plain-spoken, durable |
| 3 | Friendly consumer | `manrope` | `figtree` | `jetbrains-mono` | 82 | Approachable, rounded, modern |
| 4 | Technical | `instrument-sans` | `inter` | `geist-mono` | 98 | Precise, product-not-landing-page |
| 5 | Luxury | `playfair-display` | `lora` | `ibm-plex-mono` | 87 | High-contrast heritage, expensive |
| 6 | Swiss startup | `space-grotesk` | `inter` | `jetbrains-mono` | 107 | Confident, typographic, of-the-moment |

## 1. Editorial / opinion

Magazines, newsletters, essay-driven marketing, a blog that wants a voice. Serif headline over a grotesque body is
the oldest readable contrast there is, and it survives small screens because the body stays a sans.

```bash
npm install @fontsource-variable/newsreader @fontsource-variable/inter @fontsource-variable/jetbrains-mono
```

```css
:root {
  --font-display: "Newsreader Variable", Newsreader, Georgia, "Times New Roman", serif;
  --font-text:    "Inter Variable", Inter, system-ui, sans-serif;
  --font-mono:    "JetBrains Mono Variable", "JetBrains Mono", ui-monospace, monospace;
}
```

| Role | Size / line-height | Weight | Tracking |
| --- | --- | --- | --- |
| h1 | 46px / 1.1 | 500 | `-0.02em` |
| h2 | 30px / 1.2 | 500 | `-0.015em` |
| body | 18px / 1.65 | 400 | `0` |
| byline | 13px / 1.4 | 500 | `+0.02em` |

- Newsreader: 200–800, italic, optional `opsz`. Its `wght` latin file is **56 KB**; the `opsz` file is **128 KB**, so
  import `@fontsource-variable/newsreader` (wght) unless you genuinely vary optical size per breakpoint.
- Inter: 100–900, italic, **47 KB**. Set `font-optical-sizing: auto` only if you imported an `opsz` file.
- Use `text-wrap: balance` on h1–h2 and `pretty` on paragraphs; editorial pages live or die on ragged line endings.

**Avoid** for dashboards, dense tables, or any surface where the reader scans instead of reads.

## 2. Institutional / docs / reports

Government, legal, healthcare, annual reports, documentation portals. The pairing has to look like it will still be
correct in five years — no trend signals, no quirks.

```bash
npm install @fontsource-variable/source-serif-4 @fontsource-variable/public-sans @fontsource/ibm-plex-mono
```

```css
:root {
  --font-display: "Source Serif 4 Variable", "Source Serif 4", Georgia, serif;
  --font-text:    "Public Sans Variable", "Public Sans", system-ui, sans-serif;
  --font-mono:    "IBM Plex Mono", ui-monospace, monospace;
}
```

| Role | Size / line-height | Weight | Tracking |
| --- | --- | --- | --- |
| h1 | 38px / 1.15 | 600 | `-0.015em` |
| h2 | 26px / 1.25 | 600 | `-0.01em` |
| body | 17px / 1.65 | 400 | `0` |
| table figures | 13px / 1.4 | 400 | `0`, `tabular-nums` |

- Source Serif 4: 200–900, italic, `opsz`. `wght` **49 KB**, `opsz` **119 KB** — import the plain package.
- Public Sans: 100–900, italic, **26 KB**. A neutral, slightly wide grotesque that reads well at 15–17px.
- IBM Plex Mono has **no variable package**; import static faces only for weights you use (`400.css`, `500.css`),
  **14 KB** each.

**Avoid** for consumer apps and anything playful; the register is deliberately institutional.

## 3. Friendly consumer / geometric

Consumer apps, marketplaces, education, fintech-lite. Rounded geometric letterforms, open counters, a display face
that can shout without looking aggressive.

```bash
npm install @fontsource-variable/manrope @fontsource-variable/figtree @fontsource-variable/jetbrains-mono
```

```css
:root {
  --font-display: "Manrope Variable", Manrope, system-ui, sans-serif;
  --font-text:    "Figtree Variable", Figtree, system-ui, sans-serif;
  --font-mono:    "JetBrains Mono Variable", "JetBrains Mono", ui-monospace, monospace;
}
```

| Role | Size / line-height | Weight | Tracking |
| --- | --- | --- | --- |
| h1 | 40px / 1.1 | 700 | `-0.03em` |
| h2 | 26px / 1.25 | 700 | `-0.02em` |
| body | 16px / 1.6 | 400 | `0` |
| button | 15px / 1 | 600 | `-0.005em` |

- Manrope: 200–800, **no italic** (verified — `wght-italic.css` is a 404), **24 KB**. Never use `<em>` in it; use
  weight 700 or a colour shift for emphasis.
- Figtree: 300–900, italic available, **19 KB**. The cheaper, friendlier body; keeps forms and prices legible.
- Manrope's tight apertures get muddy below 15px — do not use it for body copy.

**Avoid** for luxury and serious B2B; rounded geometric reads young.

## 4. Technical / dev tool / SaaS

Developer tools, API consoles, infra dashboards, AI products. Slightly condensed grotesque display, neutral text,
a mono that looks engineered rather than cute.

```bash
npm install @fontsource-variable/instrument-sans @fontsource-variable/inter @fontsource-variable/geist-mono
```

```css
:root {
  --font-display: "Instrument Sans Variable", "Instrument Sans", system-ui, sans-serif;
  --font-text:    "Inter Variable", Inter, system-ui, sans-serif;
  --font-mono:    "Geist Mono Variable", "Geist Mono", ui-monospace, monospace;
}
```

| Role | Size / line-height | Weight | Tracking |
| --- | --- | --- | --- |
| h1 | 44px / 1.05 | 600 | `-0.03em` |
| h2 | 28px / 1.2 | 600 | `-0.02em` |
| body | 15px / 1.55 | 400 | `0` |
| code | 13.5px / 1.6 | 400 | `0` |

- Instrument Sans: 400–700, italic, **29 KB** — too narrow for every role. If the design needs 800, use Inter.
- Inter: 100–900, italic, **47 KB**. Body at 15px still needs 400, not 300.
- Geist Mono: 100–900, italic, **22 KB**. Tabular figures are the whole point; verify `font-variant-numeric`.

**Avoid** for editorial and luxury; the register is engineered, not authored.

## 5. Luxury / fashion / hotel

Fashion, hospitality, jewellery, private clients. High-contrast Didone display over a quiet serif body — the oldest
premium signal in typography, and still the most reliable.

```bash
npm install @fontsource-variable/playfair-display @fontsource-variable/lora @fontsource/ibm-plex-mono
```

```css
:root {
  --font-display: "Playfair Display Variable", "Playfair Display", Georgia, serif;
  --font-text:    "Lora Variable", Lora, Georgia, serif;
  --font-mono:    "IBM Plex Mono", ui-monospace, monospace;
}
```

| Role | Size / line-height | Weight | Tracking |
| --- | --- | --- | --- |
| h1 | 56px / 1.0 | 500 | `-0.01em` |
| eyebrow | 11px / 1.2 | 500 | `+0.14em`, uppercase |
| body | 17px / 1.7 | 400 | `0` |
| price | 14px / 1.4 | 400 | `+0.02em` |

- Playfair Display: 400–900, italic, **37 KB**. High contrast means thin hairlines — never below 24px.
- Lora: 400–700, italic, **36 KB**. Warm, slightly calligraphic text face that does not compete with the Didone.
- Keep tracking *loose* on small caps and eyebrow labels, tight only on the h1. Do not tighten a Didone like a grotesque.

**Avoid** where tabular data density matters; two serifs plus a mono is already three voices.

## 6. Swiss / design-led startup

Agencies, portfolios, design tools, seed-stage marketing. Quirky grotesque display, neutral body, mono for detail.

```bash
npm install @fontsource-variable/space-grotesk @fontsource-variable/inter @fontsource-variable/jetbrains-mono
```

```css
:root {
  --font-display: "Space Grotesk Variable", "Space Grotesk", system-ui, sans-serif;
  --font-text:    "Inter Variable", Inter, system-ui, sans-serif;
  --font-mono:    "JetBrains Mono Variable", "JetBrains Mono", ui-monospace, monospace;
}
```

| Role | Size / line-height | Weight | Tracking |
| --- | --- | --- | --- |
| h1 | 48px / 1.08 | 500 | `-0.025em` |
| h2 | 30px / 1.2 | 500 | `-0.02em` |
| body | 16px / 1.6 | 400 | `0` |
| label | 12px / 1.3 | 500 | `+0.01em` |

- Space Grotesk: 300–700, **no italic**, **21 KB**. Display only — its quirky `a` and `g` fatigue in long body copy.
- Inter: 100–900, italic, **47 KB**.
- JetBrains Mono: 100–800, italic, **39 KB**. Slightly tall x-height; good for small labels and inline code.

**Avoid** for editorial long-form and for regulated industries; the quirk reads startup, not institution.

## Swaps by tone

| If you want | Swap in | Notes |
| --- | --- | --- |
| Warmth instead of geometry | `fraunces` + `figtree` | Fraunces 100–900, italic, `opsz` / `SOFT` / `WONK` axes; `wght` **35 KB**, `opsz` **65 KB**, `full.css` for everything |
| Monochrome technical | `geist` + `geist-mono` | Geist 100–900, italic, **28 KB**; one superfamily, zero contrast |
| Long-form non-fiction | `literata` + `public-sans` | Literata 200–900, italic, `opsz`, **51 KB**; built for reading on screen |
| Magazine luxury | `bodoni-moda` + `cormorant-garamond` | Bodoni Moda 400–900 (**25 KB**), Cormorant Garamond 300–700 (**36 KB**) — both very high contrast, large sizes only |
| Enterprise neutral | `ibm-plex-sans` / `ibm-plex-mono` | Plex Sans is variable (100–700 + `wdth`); Plex Mono is static-only |
| Friendlier body, same tone | `nunito-sans` / `figtree` | Nunito Sans variable is 200–1000 and much rounder |

## Mono options

| Package | Range | Italic | Latin KB | Use for |
| --- | --- | --- | --- | --- |
| `@fontsource-variable/jetbrains-mono` | 100–800 | yes | 39 | general code, labels, numbers |
| `@fontsource-variable/geist-mono` | 100–900 | yes | 22 | product UI, compact tables |
| `@fontsource-variable/roboto-mono` | 100–700 | yes | 32 | Android-adjacent, very neutral |
| `@fontsource-variable/source-code-pro` | 200–900 | yes | 21 | docs, terminals, small sizes |
| `@fontsource-variable/fira-code` | 300–700 | yes | 35 | code with ligatures |
| `@fontsource/ibm-plex-mono` | 100–700 static | yes | 14 per weight | institutional, print-adjacent |

## Picking under pressure

1. **B2B / technical?** Pairing 4. **B2C / friendly?** Pairing 3. **Words are the product?** Pairing 1.
   **Trust is the product?** Pairing 2. **Price is the product?** Pairing 5. **Taste is the product?** Pairing 6.
2. Ship **two families** if the budget is tight: text + mono, with the text family doing display duty at 600–700.
3. If the display face has no italic, the whole page has no italic. Decide that before you commit.
4. Total budget target: **≤ 110 KB** of latin woff2 for the first paint (display + text), mono lazy or subset later.
