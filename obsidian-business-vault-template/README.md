# Obsidian Business Vault Template

A structured Obsidian knowledge vault for solo operators, micro-businesses, and small remote teams. Built from a real production system — NZRT Network uses this exact structure to run a 9-agent AI virtual organisation.

## What This Solves

Most Obsidian users start with a flat folder of notes and end up with chaos. This template gives you:

- A consistent **frontmatter schema** so every note is queryable and filterable
- A **service code system** that tags notes to the business system they belong to
- A **role code system** that assigns ownership of every note
- A **HOME.md convention** — every folder has an index note
- A **MOC (Map of Content) pattern** so navigation never breaks as the vault grows
- **Wikilink conventions** — full path + display text, always
- **Claude Code ready** — `CLAUDE.md` at root so AI agents understand your vault

## What's Included

```
obsidian-business-vault-template/
├── .gitignore                        # Excludes Obsidian workspace/cache, credentials
├── CLAUDE.md                         # AI agent instructions — fill in your org details
├── HOME.md                           # Master vault index
├── schema.md                         # Frontmatter schema, codes, conventions
├── 00 - Inbox/
│   └── HOME.md                       # Capture zone — process and file regularly
├── 01 - Example Domain/              # Shows the domain + HOME.md + note pattern
│   ├── HOME.md                       # Domain index (MOC)
│   ├── Example Guide.md              # Guide note type example
│   └── Example Reference.md         # Reference note type example
└── Templates/
    ├── New Note.md                   # Default blank note
    ├── Meeting.md                    # Meeting notes with agenda, decisions, actions
    ├── SOP.md                        # Standard operating procedure
    ├── Project.md                    # Project with goal, scope, plan, decisions
    ├── Reference.md                  # Quick reference table + detail
    └── ADR.md                        # Architecture Decision Record
```

## Quick Start

1. Clone or download this repo
2. Open the folder as a new Obsidian vault (`Open folder as vault`)
3. Read `schema.md` — understand the frontmatter conventions before creating notes
4. Rename `01 - Example Domain/` to your first real domain (e.g. `01 - Infrastructure/`)
5. Update `HOME.md` with your vault map
6. Fill in `CLAUDE.md` with your org details if using Claude Code

## The Schema (Frontmatter)

Every note should have this frontmatter:

```yaml
---
tags: [<domain-tag>, <org-tag>, <service-code>, <note-type>]
aliases: [Human readable name]
role: <role-code>        # who owns/maintains this note
created: YYYY-MM-DD
status: draft|review|active|complete|archived
type: MOC|guide|reference|config|adr|schema
related:
  - "[[path/to/related-note|Display Name]]"
---
```

Full spec in `schema.md`.

## Service Code System

One service code per note — tags the note to the system it belongs to:

| Code | System |
|------|--------|
| `000MST` | Master / vault root |
| `000DOL` | Dolibarr ERP |
| `000GIT` | GitHub / version control |
| `000LLM` | AI / LLM tooling |
| `000NCL` | Nextcloud |
| `000WEB` | WordPress / web |
| `000INF` | Infrastructure |
| `000K8S` | Kubernetes |

Add your own — 6 characters, uppercase, prefix `000`.

## Role Code System

Every note has an owner:

| Code | Who |
|------|-----|
| `xc` | Admin / owner |
| `pam` | Marketing |
| `cas` | Sales / CRM |
| `fin` | Finance |
| `dan` | DBA / infra |

Rename to match your team. Pattern matters, not the specific codes.

## Key Conventions

**HOME.md** — every folder gets one. Type: `MOC`. Links to every note in the folder. Navigate by HOME.md, not by search.

**Wikilinks** — always full path from vault root + display text:
```
[[Domain/Subfolder/Note Name|Human Readable Title]]
```
Never bare `[[Note Name]]` — breaks when files move.

**Folder naming** — `Title Case` or `NN - Title Case` for numbered sections.

## Real-World Usage

This template is extracted from [NZRT Network](https://nzrtnetwork.com)'s production vault — a 9-agent AI virtual organisation running Dolibarr ERP, Nextcloud, and WordPress, documented in this structure. See also: [claude-code-multi-agent-setup](https://github.com/NZRTnetwork/claude-code-multi-agent-setup).

## License

MIT — use freely, adapt for your business.

---

*Built by NZRT Network · [nzrtnetwork.com](https://nzrtnetwork.com)*
