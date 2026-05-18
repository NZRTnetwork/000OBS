# Vault Schema

Master reference for frontmatter, service codes, role codes, note types, and naming conventions.

---

## Frontmatter Schema

Required on every note:

```yaml
---
tags: [<domain-tag>, <org-tag>, <service-code>, <note-type>]
aliases: [Human readable name, Alternative name]
role: <role-code>
created: YYYY-MM-DD
status: draft|review|active|complete|archived
type: MOC|guide|reference|config|adr|schema
related:
  - "[[path/to/note|Display Name]]"
---
```

### Field Rules

| Field | Required | Values |
|-------|---------|--------|
| `tags` | Yes | Array — include org tag, service code, note type at minimum |
| `aliases` | Yes | Array — human readable names for search |
| `role` | Yes | Single role code — who owns this note |
| `created` | Yes | ISO date YYYY-MM-DD |
| `status` | Yes | See status values below |
| `type` | Yes | See type values below |
| `related` | No | Array of wikilinks to related notes |

### Status Values

| Status | When to use |
|--------|-------------|
| `draft` | Work in progress, not reliable yet |
| `review` | Complete but needs checking |
| `active` | Living document, updated regularly |
| `complete` | Point-in-time reference, won't change |
| `archived` | No longer relevant, kept for history |

### Type Values

| Type | What it is |
|------|-----------|
| `MOC` | Map of Content — folder index, navigation hub |
| `guide` | How-to, step-by-step instructions |
| `reference` | Facts, tables, specs — look things up |
| `config` | Configuration record for a system |
| `adr` | Architecture Decision Record |
| `schema` | Schema definition (like this file) |

---

## Service Codes

One per note. Tag the note to the system it belongs to.

| Code | System | Description |
|------|--------|-------------|
| `000MST` | Master | Vault root, cross-system |
| `000DOL` | Dolibarr | ERP, CRM, invoicing |
| `000GIT` | GitHub | Version control, CI/CD |
| `000LLM` | LLM / AI | AI tooling, prompt patterns |
| `000NCL` | Nextcloud | File sharing, collaboration |
| `000WEB` | WordPress | Website, CMS |
| `000INF` | Infrastructure | Hosting, DNS, SSL, mail |
| `000K8S` | Kubernetes | Containers, orchestration |
| `000BCH` | Blockchain | Web3, smart contracts |
| `000TOG` | TOGAF | Enterprise architecture |

Add your own: 6 characters, uppercase, prefix `000`.

---

## Role Codes

One per note. Marks ownership and maintenance responsibility.

| Code | Role |
|------|------|
| `xc` | Admin / owner |
| `pam` | Marketing |
| `cas` | Sales / CRM |
| `sun` | Procurement |
| `fin` | Finance |
| `han` | HR |
| `ema` | Documents / EDM |
| `dai` | Analytics |
| `dan` | DBA / infrastructure |

Replace with your own team codes. Keep them 2–3 characters, lowercase.

---

## Naming Conventions

### Folders
- `Title Case` for domain folders: `Dolibarr/`, `Nextcloud/`, `NZRT Network/`
- `NN - Title Case` for numbered sections: `01 - Overview/`, `09 - AI Agents/`

### Notes
- `Title Case.md` for most notes: `Agent Account Setup.md`
- `HOME.md` for folder indexes (always)
- `kebab-case.md` acceptable for reference files

### Wikilinks
Always full path from vault root + display text:
```
[[Domain/Subfolder/Note|Display Title]]
```

Never:
```
[[Note]]           ← breaks when files move
[[Note|Title]]     ← missing path, fragile
```

---

## Note Footer Convention

Every note ends with:

```
*Last updated: YYYY-MM-DD*
```

MOC/HOME notes also include a tag cloud as clickable links (optional, useful if using Nextcloud tags).

---

## HOME.md Convention

Every folder gets a `HOME.md`:
- `type: MOC`
- Lists every note in the folder with description
- Links to related HOME.md files in other domains
- Is the entry point — never navigate a folder without HOME.md

---

*Last updated: see file*
