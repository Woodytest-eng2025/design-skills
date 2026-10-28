# Simple Icons — Slug and Colour Reference

Fifty-three marks that cover most product pages, grouped by where they usually appear. Slugs were checked against the
Simple Icons **16.28.0** data set (3,453 current icons) on 2026-10-28; the hex column is the package's `hex` field,
which ships **without** a leading `#`.

Treat the hex column as a starting point, not a source of truth. Brands rebrand — Node.js, LinkedIn and Facebook have
all changed their official values in recent years, and Simple Icons follows them between minor releases. Read
`siX.hex` at build time whenever the exact value matters.

## Frontend

| Mark | Slug | Hex |
| --- | --- | --- |
| React | `react` | `61DAFB` |
| TypeScript | `typescript` | `3178C6` |
| JavaScript | `javascript` | `F7DF1E` |
| Next.js | `nextdotjs` | `000000` |
| Vue.js | `vuedotjs` | `4FC08D` |
| Svelte | `svelte` | `FF3E00` |
| Vite | `vite` | `646CFF` |
| Tailwind CSS | `tailwindcss` | `06B6D4` |
| npm | `npm` | `CB3837` |

## Backend and data

| Mark | Slug | Hex |
| --- | --- | --- |
| Node.js | `nodedotjs` | `5FA04E` |
| Python | `python` | `3776AB` |
| Go | `go` | `00ADD8` |
| Rust | `rust` | `000000` |
| PHP | `php` | `777BB4` |
| Django | `django` | `092E20` |
| FastAPI | `fastapi` | `009688` |
| PostgreSQL | `postgresql` | `4169E1` |
| MongoDB | `mongodb` | `47A248` |

## Cloud and infrastructure

| Mark | Slug | Hex |
| --- | --- | --- |
| Vercel | `vercel` | `000000` |
| Netlify | `netlify` | `00C7B7` |
| Cloudflare | `cloudflare` | `F38020` |
| Amazon Web Services | `amazonwebservices` | `FF9900` |
| Google Cloud | `googlecloud` | `4285F4` |
| Docker | `docker` | `2496ED` |
| Kubernetes | `kubernetes` | `326CE5` |
| Terraform | `terraform` | `7B42BC` |

## AI

| Mark | Slug | Hex |
| --- | --- | --- |
| OpenAI | `openai` | `412991` |
| Claude | `claude` | `D97757` |
| Hugging Face | `huggingface` | `FFD21E` |
| Google Gemini | `googlegemini` | `8E75B2` |

## Design tools

| Mark | Slug | Hex |
| --- | --- | --- |
| Figma | `figma` | `F24E1E` |
| Framer | `framer` | `0055FF` |
| Canva | `canva` | `00C4CC` |
| Sketch | `sketch` | `F7B500` |
| Adobe Photoshop | `adobephotoshop` | `31A8FF` |

## Social

| Mark | Slug | Hex |
| --- | --- | --- |
| GitHub | `github` | `181717` |
| X | `x` | `000000` |
| LinkedIn | `linkedin` | `0A66C2` |
| YouTube | `youtube` | `FF0000` |
| Instagram | `instagram` | `E4405F` |
| Discord | `discord` | `5865F2` |
| Slack | `slack` | `4A154B` |
| Reddit | `reddit` | `FF4500` |
| TikTok | `tiktok` | `000000` |

## Payments and commerce

| Mark | Slug | Hex |
| --- | --- | --- |
| Stripe | `stripe` | `635BFF` |
| PayPal | `paypal` | `003087` |
| Visa | `visa` | `1A1F71` |
| Mastercard | `mastercard` | `EB001B` |
| Shopify | `shopify` | `7AB55C` |
| Klarna | `klarna` | `FFB3C7` |

## Analytics

| Mark | Slug | Hex |
| --- | --- | --- |
| Google Analytics | `googleanalytics` | `E37400` |
| Hotjar | `hotjar` | `FF3C00` |
| Matomo | `matomo` | `3152A0` |

## Rename and removal traps

Checked against the same snapshot. The left column is what people type; the right column is what actually exists.

| You might type | Correct slug | Status |
| --- | --- | --- |
| `next` / `nextjs` | `nextdotjs` | Current — dots in a product name become `dot` |
| `node` | `nodedotjs` | Current |
| `vue` | `vuedotjs` | Current |
| `twitter` | `x` | The old mark was removed, not aliased |
| `aws` / `amazonaws` | `amazonwebservices` | Current |
| `rails` | `rubyonrails` | Current |
| `java` | — | Removed; `openjdk` exists but is a different mark, not a replacement |
| `zeit` | `vercel` | Old company mark removed |
| `reactnative` | — | No icon in 16.28.0; use `react` or a wordmark |
| `sveltekit` | — | Not in the set; only `svelte` |

Two naming rules cover most surprises: **dots are spelled out** (`nextdotjs`, `nodedotjs`, `vuedotjs`) and **a brand
rename usually replaces the old slug** rather than keeping an alias. A missing icon is not a bug you can fix with a close
match — check simpleicons.org, then fall back to a wordmark.

## Checking a slug

From a project that has the package installed:

```bash
node -e "import('simple-icons').then(m => console.log(Object.keys(m).filter(k => k.includes('vue'))))"
```

Or inside a module, print what the export actually contains:

```js
import { siVuedotjs } from "simple-icons";
console.log(siVuedotjs.title, siVuedotjs.slug, siVuedotjs.hex); // "Vue.js" "vuedotjs" "4FC08D"
```

`slugs.md` in the upstream repository is the complete title → slug index; the website search at simpleicons.org is
faster for a single brand.

## Colour caveats

- `hex` never includes `#`. `fill={"#" + icon.hex}` or a CSS custom property, never `fill={icon.hex}`.
- Some marks are officially black (`000000`): Vercel, Next.js, X, TikTok, Apple, Rust. Black is a brand colour, not a
  missing value, and it disappears on dark surfaces.
- Low-contrast brand colours (JavaScript yellow, Hugging Face yellow, Klarna pink) fail 3:1 on white even though they
  are correct. Keep the brand value for the mark's fill and fix contrast with a darker container, a light chip, or a
  colour-mixed token — do not silently repaint the logo.
- If a brand publishes guidelines, `siX.guidelines` links them. Many forbid recolouring or effects entirely; black or
  white is usually the permitted fallback.
