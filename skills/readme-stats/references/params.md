# Parameter reference — GitHub Readme Stats

Compiled from the project's `readme.md` option tables (`anuraghazra/github-readme-stats`). The live tables are
the source of truth: if a parameter below is silently ignored, check the current README before assuming it
exists. Colours are **hex without `#`** (`&title_color=2f81f7`); a literal `#` truncates the URL fragment.

Base URL for all examples: `https://github-readme-stats.vercel.app` (replace with your own deployment).

URL encoding cheat-sheet: `&` between parameters, `&amp;` inside an HTML attribute, `,` in a list is safe but
`%2C` is safer, spaces are never valid (use `+` or `%20`), a trailing `/` before `?` is accepted on `/api/pin/`
and `/api/top-langs/`.

## `/api` — stats card

`/api?username=…`

| Parameter | Type / values | Default | Notes |
| --- | --- | --- | --- |
| `username` | string | — | Required. The handle, not the display name. |
| `show_icons` | `true` | `false` | Icons next to each metric. The single biggest "designed" switch. |
| `theme` | theme name | `default` | Preset palette; any colour param overrides it. |
| `hide` | `commits,prs,issues,contribs,stars,prs_merged` | — | Drops rows. Fewer rows = shorter card. |
| `hide_title` | `true` | `false` | |
| `hide_border` | `true` | `false` | |
| `hide_rank` | `true` | `false` | Hides the rank ring. Prefer `rank_icon` for styling. |
| `rank_icon` | `default`, `github`, `percent` | `default` | `github` = octocat in the ring; `percent` = percentile. |
| `show` | `reviews,prs_merged,prs_merged_percentage,discussions_started,discussions_answered` | — | Extra rows for maintainers. |
| `include_all_commits` | `true` | `false` | All-time commit count instead of the current year. |
| `count_private` | `true` | `false` | Needs a token that can see private repos. |
| `commits_year` | `2024` | current year | Restrict the commit count to one year. |
| `number_format` | `short`, `none`, `long` | `short` | `1.3k` / `1,345` / `1.3 thousand`. |
| `card_width` | number | ~495 | Width in px. |
| `border_radius` | number | theme | Corner radius in px. |
| `locale` | language code | `en` | Translations live in `src/translations.js` (`en`, `de`, `es`, `fr`, `ja`, `pt-br`, `ru`, …). |
| `custom_title` | string | "GitHub Stats" | |
| `disable_animations` | `true` | `false` | Removes the fade-in; use for screenshots. |
| `text_bold` | `true`/`false` | `true` | |
| `line_height` | number | 25 | Tighten to 22–24 for a denser card. |
| `ring_color` | hex | theme | Progress ring colour. |
| `title_color`, `text_color`, `icon_color`, `bg_color`, `border_color` | hex | theme | Per-card overrides. `bg_color=00000000` is transparent. |
| `cache_seconds` | number | — | Cache TTL hint for the instance (bounded by its config). |

## `/api/top-langs/` — languages card

`/api/top-langs/?username=…`

| Parameter | Type / values | Default | Notes |
| --- | --- | --- | --- |
| `username` | string | — | Required. |
| `layout` | `default`, `compact`, `donut`, `donut-vertical`, `pie` | `default` | `compact` = horizontal bar, best in a two-card row. |
| `langs_count` | number | `5` | `8`–`10` is the sweet spot; more just makes a long tail. |
| `exclude_repo` | comma list | — | `exclude_repo=courses,dotfiles` — removes repos from the calculation entirely. |
| `size_weight` | float | `1` | Weight of bytes when ranking. |
| `count_weight` | float | `0` | Weight of repo count. `size_weight=0.5&count_weight=0.5` is the usual fix for notebook repos. |
| `hide` | comma list of language names | — | Hide specific languages (`hide=html,css`). |
| `hide_title`, `hide_border`, `card_width`, `border_radius`, `locale` | as stats | | |
| `theme` + colour params | as stats | | |

**How the weights work:** percentages are ranked by `size_weight × bytes + count_weight × repos`. With
`count_weight=0` (default) one huge vendored/notebook repo can own the whole card. Raising `count_weight`
favours languages you reach for in many repos, which reads more honestly on a profile.

## `/api/pin/` — repo card

`/api/pin/?username=…&repo=…`

| Parameter | Type | Notes |
| --- | --- | --- |
| `username`, `repo` | string | Required. `repo` is the repo name only, not `owner/name`. |
| `show_owner` | `true` | Adds the owner prefix — useful on org-profile pins. |
| `description_lines_count` | `1`–`3` | Clip the description instead of letting it run. |
| `theme`, colour params, `hide_border`, `border_radius`, `card_width` | | Same semantics as the stats card. |

## `/api/gist` — gist card

`/api/gist?id=<gist-id>`

| Parameter | Type | Notes |
| --- | --- | --- |
| `id` | string | The gist hash from `gist.github.com/<user>/<id>`. |
| `theme`, colour params, `hide_border`, `border_radius`, `card_width` | | Same semantics as the stats card. |

## `/api/wakatime` — coding-time card

`/api/wakatime/?username=…`

| Parameter | Type | Notes |
| --- | --- | --- |
| `username` | string | Wakatime username; the profile must be public. |
| `layout` | `default`, `compact` | `compact` for a horizontal strip. |
| `langs_count` | number | How many languages to list. |
| `hide` | comma list | Hide languages or editors (`hide=Other,Markdown`). |
| `custom_title` | string | |
| `theme`, colour params, `hide_border`, `border_radius`, `card_width` | | Same semantics as the stats card. |

## Six colour presets (custom hex, safe on transparent)

These are **our palettes**, not shipped theme names — paste the hex values. All are tuned for
`theme=transparent&hide_border=true` and tested against GitHub's light (`#ffffff`) and dark (`#0d1117`)
surfaces. Keep `title_color` = `icon_color`; that equality is what makes the pair look intentional.

| Preset | `title_color` / `icon_color` | `text_color` | Reads as | Best on |
| --- | --- | --- | --- | --- |
| Graphite Blue | `2f81f7` | `57606a` | GitHub-native, calm, safe for any profile | Light |
| Graphite Blue (dark) | `58a6ff` | `c9d1d9` | Same personality after sunset | Dark |
| Terminal Amber | `f59e0b` | `8b949e` | Vintage terminal, indie hacker | Both |
| Violet | `a78bfa` | `9ca3af` | Design/creative profile | Both |
| Teal | `2dd4bf` | `94a3b8` | Data/infra, low-key technical | Dark |
| Rose | `fb7185` | `94a3b8` | Product/frontend, warmer than blue | Light |

Usage:

```md
<img src="https://github-readme-stats.vercel.app/api?username=YOUR_HANDLE&show_icons=true&theme=transparent&hide_border=true&title_color=2f81f7&icon_color=2f81f7&text_color=57606a&border_radius=10&card_width=420" alt="GitHub stats" />
```

For a hard-coded surface instead of transparency, set `bg_color` to the exact page colour (`0d1117` dark,
`ffffff` light) — but that card will break the moment GitHub changes its background. Transparent is the
durable choice.

## Shipped themes worth knowing

`default`, `default_repocard`, `transparent`, `dark`, `radical`, `tokyonight`, `onedark`, `gruvbox`,
`gruvbox_light`, `nord`, `dracula`, `synthwave`, `highcontrast`, `merko`, `cobalt`, `prussian`, `monokai`,
`vue`, `vue-dark`, `shades-of-purple`, `nightowl`, `buefy`, `blue-green`, `algolia`, `great-gatsby`,
`darcula`, `bear`, `solarized-dark`, `solarized-light`, `chartreuse-dark`, `gotham`, `material-palenight`,
`graywhite`, `vision-friendly-dark`, `ayu-mirage`, `midnight-purple`, `calm`, `omni`, `react`, `jolly`,
`maroongold`, `yeblu`, `blueberry`, `slateorange`, `kacho_ga`, `outrun`, `ocean_dark`, `city_lights`,
`github_dark`, `github_dark_dimmed`, `discord_old_blurple`, `aura_dark`, `panda`, `noctis_minimus`, `cobalt2`,
`swift`, `aura`, `apprentice`, `moltack`, `codeSTACKr`, `rose_pine`, `catppuccin_latte`, `catppuccin_mocha`,
`date_night`, `shadow_red`, `shadow_green`, `shadow_blue`.

Previews live in `themes/README.md` in the repo. For a profile that must survive GitHub's redesigns, prefer
`transparent` plus your own accent over any named theme.

## Caching, limits and errors

- Every card is an SVG fetched through GitHub's image proxy (camo), so GitHub caches it independently of the
  instance. Editing the URL (`&v=2`) is the only reliable way to force a refresh.
- The public instance caches upstream responses so one popular profile does not hammer the GitHub API; that also
  means **your latest commit may not appear for a while**.
- Unauthenticated GitHub API quota is 60 requests/hour; a self-hosted instance with `PAT_1` gets 5,000/hour per
  token. The public instance is shared by everyone, hence the 503s.
- Error states render as an SVG containing text such as "Something went wrong", "Maximum retry limit reached" or
  a rate-limit message. That text is what visitors see — check the card in a private window before shipping.
- If you only need one card and cannot self-host, the `pin` card is the least rate-limit-sensitive choice.

## Self-hosting env vars

| Variable | Purpose |
| --- | --- |
| `PAT_1` … `PAT_n` | GitHub tokens, rotated to multiply quota. `repo` scope enables private counts. |
| `CACHE_SECONDS` | Edge cache TTL in seconds; higher = fewer API calls, staler numbers. |
| `WHITELIST` | Comma-separated usernames allowed to use the deployment. |

The repo's `.env.example` is authoritative; Vercel picks the variables up on redeploy.

## Known-uncertain details

Verify these against the live docs if they matter to your output: the exact default value of `langs_count`,
whether `rank_icon=none` is still a valid value (use `hide_rank=true` instead), the supported range of
`description_lines_count`, the locale code for Chinese (`src/translations.js` is authoritative), and the default
`CACHE_SECONDS` on Vercel. None of them change the design guidance in `SKILL.md`.
