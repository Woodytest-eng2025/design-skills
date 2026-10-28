# Mermaid syntax cheatsheet

Every block below is copy-pasteable into [mermaid.live](https://mermaid.live) or a ` ```mermaid ` fence.
Paired with `SKILL.md`, which carries the judgement; this file carries the vocabulary.

## Flowchart

```mermaid
flowchart TB
  A["Start"] --> B{"Ready?"}
  B -- yes --> C["Ship"]
  B -- no --> D["Wait"]
  C --> E(["Done"])
  D -.-> A
```

Chained edges (`a --> b --> c`), `linkStyle 0 stroke:#f97316`, and `classDef` / `class` / `A:::name` all work.
`click A "https://..."` needs `securityLevel: "loose"` — leave it out of docs you do not control.

## Sequence

```mermaid
sequenceDiagram
  autonumber
  actor U as User
  participant S as Service
  U->>S: request
  activate S
  par cache hit
    S-->>U: cached
  and cache miss
    S->>S: compute
    S-->>U: fresh
  end
  deactivate S
  Note right of S: metrics
```

Blocks: `alt/else`, `opt`, `loop`, `par/and`, `critical`, `break`; every one closes with `end`. `rect rgb(...)`
tints a region, `box` groups participants.

## Class

```mermaid
classDiagram
  class Order {
    +UUID id
    +Money total
    +submit() bool
  }
  class LineItem {
    +int qty
  }
  Order "1" *-- "1..*" LineItem : contains
  Order ..> Payment : uses
```

Relations: `<|--` inheritance, `*--` composition, `o--` aggregation, `-->` association, `..>` dependency,
`..|>` realisation. Multiplicities sit in quotes next to each end.

## State

```mermaid
stateDiagram-v2
  state fork_state <<fork>>
  state join_state <<join>>
  [*] --> fork_state
  fork_state --> A
  fork_state --> B
  A --> join_state
  B --> join_state
  join_state --> [*]
```

`<<choice>>` for branching, `state Name { … }` for composites, `direction LR` inside a composite.

## ER

```mermaid
erDiagram
  CUSTOMER ||--o{ ORDER : places
  ORDER ||--|{ LINE_ITEM : contains
  CUSTOMER {
    uuid id PK
    string email UK
  }
  ORDER {
    uuid id PK
    int total_cents
  }
```

Attribute keys: `PK`, `FK`, `UK`, optionally combined (`PK, FK`). Comments go in quotes after the key.

## Gantt

```mermaid
gantt
  title Launch
  dateFormat YYYY-MM-DD
  axisFormat %b %d
  excludes weekends
  section Build
  API  :active, a1, 2026-01-06, 10d
  Beta :crit, b1, after a1, 7d
  Ship :milestone, m1, after b1, 0d
```

Tags: `done`, `active`, `crit`, `milestone`. Durations are `10d`, `4h`, `2w`, or an end date.

## gitGraph

```mermaid
gitGraph
  commit id: "init"
  branch feature/auth
  checkout feature/auth
  commit id: "schema"
  commit id: "api"
  checkout main
  merge feature/auth tag: "v1.2.0"
  commit id: "notes" type: HIGHLIGHT
```

`type:` is `NORMAL`, `REVERSE` or `HIGHLIGHT`; `cherry-pick id: "schema"` replays a commit.

## Mindmap

```mermaid
mindmap
  root((release))
    Scope
      Auth
      Billing
    Risks
      Migration
```

Indentation is the whole grammar. Optional shapes: `[square]`, `(rounded)`, `((circle))`, `))bang((`,
`)cloud(`, `{{hexagon}}`.

## Timeline

```mermaid
timeline
  title Auth history
  section 2023
    Q1 : Password only
    Q3 : Add TOTP
  section 2025
    Q2 : Passkeys
```

Multiple events on one period: `Q3 : Add TOTP : Add recovery codes`.

## Quadrant

```mermaid
quadrantChart
  title Backlog bets
  x-axis Low effort --> High effort
  y-axis Low impact --> High impact
  quadrant-1 Do now
  quadrant-2 Schedule
  quadrant-3 Drop
  quadrant-4 Delegate
  SSO: [0.3, 0.8]
  Mobile app: [0.8, 0.4]
```

Coordinates are 0–1, `[x, y]`, and the point label is whatever precedes the colon.

## Sankey

```mermaid
sankey-beta
Visit,Signup,1200
Visit,Bounce,3400
Signup,Activated,780
Activated,Paid,190
```

Config: `sankey: { linkColor: "gradient", nodeAlignment: "justify", showValues: true }`.

## XY chart

```mermaid
xychart-beta
  title "Weekly active users"
  x-axis [W1, W2, W3, W4]
  y-axis "Users" 0 --> 600
  bar [180, 240, 310, 420]
  line [180, 240, 310, 420]
```

`x-axis` also accepts a range (`x-axis 0 --> 100`) or categorical labels in brackets — not both.

## Block

```mermaid
block-beta
  columns 3
  api["API"] db[("DB")] cache["Redis"]
  api --> db
  api --> cache
```

`space` and `space:N` leave gaps; `blockArrowId<["label"]>(right)` draws arrowing containers.

## Kanban

```mermaid
kanban
  backlog[Backlog]
    rfc[Draft RFC]
  doing[In progress]
    api[Ship API]
  done[Done]
    sso[SSO]
```

Cards can carry metadata (`ticket`, `assigned`, `priority`) through the `@{ … }` suffix; the exact shape has
shifted between minors, so check it in the Live Editor against your pinned version before committing.

## Architecture

```mermaid
architecture-beta
  group api(cloud)[API]
  service gateway(server)[Gateway] in api
  service db(database)[Postgres] in api
  gateway:R -- L:db
```

Endpoints are `service:{L,R,T,B}`; built-in icons include `cloud`, `server`, `database`, `disk`, `internet`.

## Packet

```mermaid
packet-beta
  0-15: "Source Port"
  16-31: "Destination Port"
  32-63: "Sequence Number"
```

Bit ranges are inclusive and must not overlap; each line is one field of the frame.

## Treemap

```mermaid
treemap-beta
"Revenue"
    "Subscriptions": 62
    "Services": 28
"Cost"
    "Infra": 19
```

Quoted sections contain quoted leaves with a numeric value; nesting deeper adds another level.

## Radar

```mermaid
radar-beta
  axis speed["Speed"], price["Price"], ux["UX"]
  curve us["Us"]{4, 3, 5}
  max 5
  min 0
```

`ticks 4` and `graticule circle` change the grid; curve values map to the axes in declaration order.

## Theme variables that matter

| Variable | Controls |
| --- | --- |
| `primaryColor` | node / actor fill |
| `primaryTextColor` | text inside nodes |
| `primaryBorderColor` | node borders |
| `lineColor` | edges and connectors |
| `secondaryColor` / `tertiaryColor` | alternate cluster shades |
| `background` | diagram background |
| `mainBkg` / `nodeBorder` | per-node overrides |
| `clusterBkg` / `clusterBorder` | subgraph fill and border |
| `edgeLabelBackground` | plate behind edge labels |
| `fontFamily` / `fontSize` | all diagram text |
| `titleColor` | titles and `accTitle` |
| `actorBkg` / `actorBorder` / `actorTextColor` | sequence actors |
| `signalColor` / `signalTextColor` | sequence arrows and their labels |
| `noteBkgColor` / `noteBorderColor` / `noteTextColor` | notes |
| `activationBkgColor` | activation bars |
| `sectionBkgColor` / `altSectionBkgColor` | gantt sections |
| `taskBkgColor` / `taskTextColor` | gantt bars |
| `gridColor` / `todayLineColor` | gantt grid and today marker |
| `pie1` … `pie12` | pie slices |
| `git0` … `git7` | git branch colours |
| `quadrant1Fill` … `quadrant4Fill` | quadrant background fills |
| `cScale0` … `cScale11` | colour scale used by mindmap and friends |

`themeVariables` are most predictable on `theme: "base"`; the packaged themes (`default`, `neutral`, `dark`,
`forest`) already set many of the same keys, so overrides can lose to the theme.

## Config keys worth knowing

| Key | Values | Note |
| --- | --- | --- |
| `theme` | `default`, `neutral`, `dark`, `forest`, `base`, `null` | `base` for custom variables, `null` for raw CSS |
| `look` | `classic`, `handDrawn` | `handDrawn` is v11.3+; pair with `handDrawnSeed` |
| `layout` | `dagre`, `elk` | `elk` requires `registerLayoutLoaders` |
| `securityLevel` | `strict`, `loose`, `antiscript`, `sandbox` | `strict` sanitises HTML labels |
| `fontFamily` | CSS stack | applied to every diagram type |
| `themeCSS` | CSS string | last resort; survives upgrades poorly |
| `flowchart.htmlLabels` | boolean | `false` → SVG `<text>`, predictable exports |
| `flowchart.curve` | `basis`, `linear`, `step`, `stepBefore`, `stepAfter` | edge smoothing |
| `flowchart.padding` / `nodeSpacing` / `rankSpacing` | number | layout breathing room |
| `deterministicIds` | boolean | stable SVG ids for snapshot tests |
| `maxTextSize` / `maxEdges` | number | guard rails, defaults 50000 / 500 |

## `mmdc` flags

| Flag | Use |
| --- | --- |
| `-i` / `-o` | input `.mmd`, output `.svg` / `.png` / `.pdf` |
| `-t` | theme override (`neutral`, `dark`, …) |
| `-b` | background (`transparent` or `#0b1020`) |
| `-c` | JSON config file (same shape as `initialize`) |
| `-C` | extra CSS file |
| `-s` | scale factor; `2` for retina PNG |
| `-w` / `-H` | width / height in pixels |
| `-f` | fit the diagram to the PDF page |
| `-p` | puppeteer config (CI `--no-sandbox`) |

## Characters that break labels

| Character | Handling |
| --- | --- |
| `;` | statement separator in flowcharts — avoid it, or quote the label |
| `(` `)` `[` `]` `{` `}` | wrap the label in quotes: `A["Deploy (canary)"]` |
| `#` | `#35;` |
| `"` inside a quoted label | `#quot;` |
| newline | `<br/>` (requires `htmlLabels: true`, the default) |
| `%%` at line start | comment; the rest of the line is ignored |
| bare `end` as a node id | closes a subgraph — quote it or rename |

## Beta types

`sankey-beta`, `xychart-beta`, `block-beta`, `packet-beta`, `architecture-beta`, `treemap-beta`, `radar-beta`
render fine but their grammar can still change between minors, and `kanban` has changed more than once in the
11.x line. Pin the Mermaid version in any CI that renders them.
