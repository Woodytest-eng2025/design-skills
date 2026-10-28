# shadcn/ui — Component Index

Install with `npx shadcn@latest add <name>`; the registry name is the filename in `components/ui/`. The "use when"
column is the decision, not a description — if no reason fits, a `div` and a utility class are cheaper.

## Layout and structure

| Component | Use when |
| --- | --- |
| `Card` | Grouping related content on a raised surface; the default container for stats and forms |
| `Separator` | Splitting regions where a border would be too heavy |
| `Tabs` | Two to five peer views that must not lose context |
| `Accordion` / `Collapsible` | Long settings or FAQ groups; one panel open at a time |
| `Scroll Area` | Custom scrollbars inside a fixed-height panel or menu |
| `Resizable` | Split panes: editor + preview, list + detail |
| `Sidebar` | App navigation with collapse, mobile sheet and keyboard shortcut |
| `Aspect Ratio`, `Carousel` | Media that must not shift layout; a few visual items, never long lists |

## Forms and input

| Component | Use when |
| --- | --- |
| `Button` | Any action; `variant` for hierarchy, `size="icon"` only with `aria-label` |
| `Input` / `Textarea` | Text entry, always with a `Label htmlFor` — a placeholder is not a label |
| `Field`, `FieldGroup`, `FieldError` | Newer primitives for non-RHF forms and consistent spacing |
| `Form` (+ `FormField`, `FormItem`, `FormMessage`) | react-hook-form + zod; wires `aria-describedby` and `aria-invalid` |
| `Checkbox` / `Switch` | Multi-select vs an immediate on/off setting |
| `Radio Group` / `Select` | Up to five visible exclusive options vs six or more in a menu |
| `Combobox` | Searchable single select built from `Popover` + `Command` |
| `Slider` | Approximate ranges; use `Input` when the exact number matters |
| `Calendar` / `Date Picker` | Date selection; the picker is the input shell around `Calendar` |
| `Input OTP`, `Toggle Group` | One-time codes; persistent formatting or filter state |

## Overlays and menus

| Component | Use when |
| --- | --- |
| `Dialog` | Focused task or form that interrupts; `DialogTitle` is required |
| `Alert Dialog` | Destructive confirmation only — it blocks and ignores outside clicks |
| `Sheet` / `Drawer` | Side panel on any screen; bottom sheet on touch devices |
| `Popover` | Anchored free-form content: filters, pickers, mini forms |
| `Tooltip` / `Hover Card` | One-line clarification of an icon; a richer hover preview |
| `Dropdown Menu` / `Context Menu` | Row and account actions; right-click actions on a row or canvas |
| `Menubar`, `Command`, `Sonner` | Desktop-style menus; command palette; every transient notification |

## Feedback and status

| Component | Use when |
| --- | --- |
| `Alert` | Persistent inline message that must survive a re-render |
| `Badge` | Compact state or count — `variant` carries meaning, not decoration |
| `Progress` / `Spinner` | Determinate work with a known total; indeterminate work inside a button |
| `Skeleton` | Loading placeholder that mirrors the real layout |
| `Empty` | Zero-data screens with an icon, explanation and one action |
| `Toast` | Deprecated — use `Sonner` |

## Data, charts and navigation

| Component | Use when |
| --- | --- |
| `Table` | Static or server-rendered data with no sorting or paging |
| `Data Table` | Sorting, filtering, selection and pagination via `@tanstack/react-table` |
| `Chart` | Any Recharts figure: `ChartContainer` + `ChartConfig`, colours from `--chart-1…5` |
| `Avatar` | People or orgs; always ship an `AvatarFallback` with initials |
| `Breadcrumb` / `Pagination` | Three or more hierarchy levels; paged lists where "load more" loses position |
| `Kbd`, `Item`, `Typography` | Documented shortcuts; list rows with actions; prose blocks for docs and legal |

## Blocks

Installed the same way (`npx shadcn@latest add dashboard-01`) — reference layouts to read, copy and delete from.

| Block | Use when |
| --- | --- |
| `dashboard-01` | Analytics overview: metric cards, chart, recent activity |
| `sidebar-07` | App shell with collapsible sidebar, header and content area |
| `login-01` / `signup-01` | Auth screens with social buttons and field validation |
| `calendar-01` / `chart-01` | Schedulers and booking flows; one well-composed chart card |
| `mail-01` / `tasks-01` | List + detail layouts with keyboard-friendly panes |

## Registry notes

- Components carry `registryDependencies` (`button`, `dialog`) and package `dependencies` (`recharts`, `cmdk`);
  `add` installs both, so never hand-install a primitive's peer package first.
- Team registries live under `registries` in `components.json` (`"@acme": { "url": "…/{name}.json" }`) and
  install as `npx shadcn@latest add @acme/data-grid`.
- `npx shadcn@latest build` turns a local `registry.json` into static JSON; item types are `registry:ui`,
  `registry:component`, `registry:block`, `registry:lib`, `registry:hook`, `registry:page`.
