# Rough.js option reference

All shapes accept the same `Options` object. Values below are the library defaults (Rough.js 4.6.6).

## Geometry-first options

| Option | Type | Default | What it does |
| --- | --- | --- | --- |
| `roughness` | number | `1` | How much the line deviates from perfect. `0` = straight, `1` = natural pencil, `2` = loose marker, `3+` = chaotic. |
| `bowing` | number | `1` | Curvature of "straight" segments. Technical diagrams want `0.2–0.6`; illustrations `1`. |
| `maxRandomnessOffset` | number | `2` | Raw jitter of individual points. Rarely set directly |
| `seed` | number | random | Deterministic randomness. **Always set it** in UI code. |
| `preserveVertices` | boolean | `false` | Keeps `linearPath`/`polygon` corners exactly on the given coordinates. |

## Stroke options

| Option | Default | Notes |
| --- | --- | --- |
| `stroke` | `#000` | Any CSS colour; `currentColor` works for SVG output. |
| `strokeWidth` | `1` | In px. Above `4` the roughness reads as a marker; below `1` it reads as a hairline pen. |
| `disableMultiStroke` | `false` | `true` = single pass. Use for small icons and dense diagrams — double stroke muddies at small sizes. |
| `disableMultiStrokeFill` | `false` | Same, for the fill outline. |
| `dashOffset` | `0` | Shift the dash pattern. |
| `dashGap` | `0` | Gap length for dashed strokes (also drives `fillStyle: "dashed"`). |
| `zigzagOffset` | `0` | Amplitude for `zigzag`/`zigzag-line` fills. |

## Fill options

| Option | Default | Notes |
| --- | --- | --- |
| `fill` | none | Any CSS colour. |
| `fillStyle` | `hachure` | See table below. |
| `fillWeight` | `strokeWidth / 2` | Thickness of hachure lines. Too thick at small sizes → solid blob. |
| `hachureAngle` | `-41` | Degrees, `-90`…`90`. Vary per region to distinguish areas. |
| `hachureGap` | `-1` | `-1` means `4 × strokeWidth`. `4–8` for dense texture, `10–16` for airy. |
| `solidFill` | — | Alias behaviour of `fillStyle: "solid"`. |

### Fill styles and their character

| `fillStyle` | Look | Best for |
| --- | --- | --- |
| `hachure` | Parallel pencil lines | Default, most "sketchbook" |
| `solid` | Flat colour with a rough edge | Colour blocks that still need the wobble |
| `zigzag` | Tight zigzag strokes | Loud emphasis, warning callouts |
| `cross-hatch` | Two crossing line sets | Shadow / depth, "filled in with pen" |
| `dots` | Dotted texture | Charts, backgrounds, light fills |
| `dashed` | Dashed lines | Secondary/disabled regions |
| `zigzag-line` | Single zigzag line fill | Retro / print texture |

## Curve & path options

| Option | Default | Notes |
| --- | --- | --- |
| `curveStepCount` | `9` | Samples per curve. Raise to `20–30` for large smooth curves. |
| `curveFitting` | `0.95` | Curve-fitting tolerance for `curve()`. |
| `simplification` | — | Path simplification tolerance passed to `path()`. Higher = fewer, smoother segments. |

## API surface

```js
import rough from "roughjs";

rough.canvas(el, config?)      // → RoughCanvas
rough.svg(el, config?)         // → RoughSVG
rough.generator(config?)       // → RoughGenerator
```

### `RoughCanvas`

```js
const rc = rough.canvas(canvasEl);
rc.rectangle(x, y, w, h, options)   // returns the canvas (chainable)
rc.circle(cx, cy, diameter, options)
rc.ellipse(cx, cy, width, height, options)
rc.line(x1, y1, x2, y2, options)
rc.polygon([[x, y], …], options)
rc.linearPath([[x, y], …], options)
rc.arc(cx, cy, w, h, startAngle, stopAngle, closed, options)
rc.curve([[x, y], …], options)
rc.path(d, options)
rc.draw(drawable)                   // replay a generator drawable
```

### `RoughSVG`

Same methods, each returning an SVG `<g>`/`<path>` node that you append yourself:

```js
const rc = rough.svg(svgEl);
const node = rc.rectangle(10, 10, 100, 60, { fill: "#fecaca" });
svgEl.appendChild(node);
// or draw into a group:
const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
svgEl.appendChild(g);
rc.rectangle(10, 10, 100, 60, { fill: "#fecaca" }, g); // optional 3rd arg = parent
```

### `RoughGenerator` (no DOM)

```js
const gen = rough.generator();
const d = gen.rectangle(0, 0, 120, 80, { seed: 11, fill: "#bfdbfe" });

gen.toPaths(d)   // [{ d: "M…", stroke, strokeWidth, fill, fillStyle, … }]
gen.toSVG(d)     // "<g><path …/></g>" string
gen.toPaths(d)   // draw into canvas with ctx manually, or serialize for SSR
```

`toPaths` output maps 1:1 onto SVG `<path>` attributes, which is how you can render Rough.js
illustrations in React Server Components or at build time without a browser.

## Config object

`rough.canvas(el, { options: {...} })` and `rough.svg(el, { options: {...} })` accept a default option set
that individual shapes inherit — useful for setting a single brand stroke width and seed base.

## Determinism notes

- The `seed` is fed through a small xorshift PRNG; the same seed + same geometry + same options always
  produce the same path.
- Derive seeds per shape (`seed: baseSeed + index`) so a group keeps internal relationships but differs
  from its neighbours.
- Because the PRNG is seeded per draw call, changing only `stroke` re-randomises nothing — the geometry
  stays identical, so recolouring does not cause a visual jump.
