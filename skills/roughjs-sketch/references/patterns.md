# Rough.js patterns

Copy-paste recipes for the situations that actually come up in product UI. All snippets assume
`import rough from "roughjs"` (or the CDN ESM build). Every shape uses a fixed `seed`.

---

## 1. Sketched frame around a section (SVG, responsive)

A single thin rectangle around a content block, drawn behind the content and stretched with a
`viewBox` + `preserveAspectRatio="none"`.

```tsx
"use client";
import { useEffect, useRef } from "react";
import rough from "roughjs";

export function SketchFrame({ children }: { children: React.ReactNode }) {
  const ref = useRef<SVGSVGElement>(null);

  useEffect(() => {
    const svg = ref.current!;
    svg.replaceChildren();
    const rc = rough.svg(svg);
    svg.appendChild(
      rc.rectangle(2, 2, 96, 96, {
        seed: 12,
        roughness: 1.1,
        bowing: 0.8,
        stroke: "currentColor",
        strokeWidth: 0.35,
        fill: "none",
      })
    );
  }, []);

  return (
    <div className="relative rounded-sm p-6">
      <svg
        ref={ref}
        viewBox="0 0 100 100"
        preserveAspectRatio="none"
        aria-hidden="true"
        className="pointer-events-none absolute inset-0 h-full w-full text-slate-400"
      >
        {/* paths injected here */}
      </svg>
      <div className="relative">{children}</div>
    </div>
  );
}
```

Because the viewBox is 100×100 and stretched, a `strokeWidth` of `0.35` renders as roughly 1px at any
size (width-relative). Use `vector-effect="non-scaling-stroke"` on the injected paths if you want a
constant pixel stroke instead.

---

## 2. Annotation layer over a screenshot

```tsx
function AnnotationLayer() {
  const ref = useRef<SVGSVGElement>(null);

  useEffect(() => {
    const svg = ref.current!;
    svg.replaceChildren();
    const rc = rough.svg(svg);

    // circle a UI control at (62%, 18%)
    svg.appendChild(
      rc.ellipse(310, 90, 120, 56, {
        seed: 21, roughness: 1.6, stroke: "#f97316", strokeWidth: 2,
        fill: "none", disableMultiStroke: true,
      })
    );

    // arrow from the label to the circle
    svg.appendChild(
      rc.linearPath([[440, 210], [380, 130], [372, 118]], {
        seed: 22, roughness: 1.2, stroke: "#f97316", strokeWidth: 2,
      })
    );
    svg.appendChild(rc.line(372, 118, 386, 126, { seed: 23, stroke: "#f97316", strokeWidth: 2 }));
    svg.appendChild(rc.line(372, 118, 384, 108, { seed: 24, stroke: "#f97316", strokeWidth: 2 }));
  }, []);

  return (
    <svg ref={ref} viewBox="0 0 800 450" aria-hidden="true"
         className="pointer-events-none absolute inset-0 h-full w-full" />
  );
}
```

Keep annotations `pointer-events-none` so they never eat clicks, and give them one accent colour only.

---

## 3. Wobbly underline for a heading

```css
.heading {
  position: relative;
  display: inline-block;
}
```

```ts
const rc = rough.svg(svgEl);
svgEl.appendChild(
  rc.line(4, 14, 236, 12, {
    seed: 5,
    roughness: 1.9,
    bowing: 1.4,
    strokeWidth: 4,
    stroke: "#f59e0b",
    disableMultiStroke: false,
  })
);
```

Size the `<svg>` to the text width with `viewBox="0 0 240 18"` and `preserveAspectRatio="none"`.
Draw it *under* the text with `z-index: -1` and `bottom: -2px`.

---

## 4. Hand-drawn empty state illustration

```ts
const gen = rough.generator();
const shapes = [
  gen.rectangle(20, 60, 120, 80, { seed: 101, fill: "#e2e8f0", fillStyle: "hachure", hachureGap: 9 }),
  gen.circle(160, 100, 44, { seed: 102, fill: "#c7d2fe", fillStyle: "cross-hatch" }),
  gen.line(10, 160, 210, 158, { seed: 103, roughness: 2, strokeWidth: 2 }),
];
svgEl.innerHTML = shapes.map((s) => gen.toSVG(s)).join("");
```

Static SVG output also means you can pre-generate it at build time and drop it in `/public`.

---

## 5. Deterministic sketch card (React, canvas-free)

```tsx
"use client";
import { useMemo } from "react";
import rough from "roughjs";

export function SketchCard({
  width = 300, height = 160, seed = 7, title, body,
}: { width?: number; height?: number; seed?: number; title: string; body: string }) {
  const html = useMemo(() => {
    const gen = rough.generator();
    const frame = gen.rectangle(6, 6, width - 12, height - 12, {
      seed,
      roughness: 1.2,
      stroke: "currentColor",
      strokeWidth: 1.5,
      fill: "var(--sketch-fill, #fef9c3)",
      fillStyle: "zigzag",
      zigzagOffset: 4,
    });
    return gen.toSVG(frame);
  }, [width, height, seed]);

  return (
    <div className="relative max-w-full text-slate-700" style={{ width }}>
      <svg
        viewBox={`0 0 ${width} ${height}`}
        className="absolute inset-0 h-full w-full"
        aria-hidden="true"
        dangerouslySetInnerHTML={{ __html: html }}
      />
      <div className="relative p-6">
        <h3 className="text-lg font-semibold">{title}</h3>
        <p className="mt-2 text-sm text-slate-600">{body}</p>
      </div>
    </div>
  );
}
```

`useMemo` here is the cheap alternative to `useEffect` + manual DOM work: the SVG is generated during
render on the client, and because the generator needs no DOM it is safe in any client component.

---

## 6. Bar chart accent

```ts
// real chart stays clean; sketch only marks the highlighted bar
const rc = rough.svg(svgEl);
svgEl.appendChild(
  rc.rectangle(barX - 4, barY - 4, barW + 8, barH + 8, {
    seed: 31, roughness: 1.4, stroke: "#6366f1", strokeWidth: 1.5,
    fill: "#c7d2fe", fillStyle: "dots", hachureGap: 5,
  })
);
```

---

## 7. Dark-mode aware tokens

```css
.sketch {
  --sketch-stroke: #1f2937;
  --sketch-fill: #fde68a;
  --sketch-accent: #f97316;
}
.dark .sketch {
  --sketch-stroke: #e2e8f0;
  --sketch-fill: color-mix(in oklab, #fde68a 60%, transparent);
  --sketch-accent: #fb923c;
}
```

Then pass `stroke: "var(--sketch-stroke)"` in SVG mode. Canvas mode cannot read CSS variables —
resolve them with `getComputedStyle(el).getPropertyValue("--sketch-stroke")` and redraw on theme change
(`new MutationObserver` on `document.documentElement.classList`).

---

## 8. Draw-in animation (respecting reduced motion)

```css
.sketch path {
  stroke-dasharray: 1200;
  stroke-dashoffset: 1200;
  animation: sketch-draw 1.1s ease-out forwards;
}
@keyframes sketch-draw {
  to { stroke-dashoffset: 0; }
}
@media (prefers-reduced-motion: reduce) {
  .sketch path { stroke-dasharray: none; animation: none; }
}
```

The dash length must exceed the longest path; when in doubt set a large value (e.g. `3000`).

---

## 9. Resize handling

```ts
let raf = 0;
const redraw = () => {
  cancelAnimationFrame(raf);
  raf = requestAnimationFrame(() => draw(width, height));
};
const ro = new ResizeObserver(redraw);
ro.observe(container);
```

Canvas needs an explicit DPR-aware resize; SVG with a `viewBox` mostly does not — but redraw anyway if
you compute geometry from measured text.

---

## 10. When the sketch is the background

For texture-heavy backgrounds (dot paper, hachure blocks), generate **one** large SVG with a repeated
`<pattern>` rather than hundreds of shapes:

```html
<svg width="100%" height="100%" aria-hidden="true">
  <defs>
    <pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="currentColor" opacity="0.25" />
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#dots)" />
</svg>
```
