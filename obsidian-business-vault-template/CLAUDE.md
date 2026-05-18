# [Your Org Name] Obsidian Vault — Claude Instructions

I am in [Your Country/Region].

---

## What This Vault Is

This is the [Your Org Name] knowledge vault — the master wiki, architecture reference, and operational documentation for [your org].

**Primary use**: Writing, editing, and maintaining wiki documentation across all business domains.

---

## Organisation Overview

[Describe your organisation here — what you do, what systems you run.]

**Core systems:**
| System | URL / Location |
|--------|---------------|
| [System 1] | [URL] |
| [System 2] | [URL] |

---

## Vault Conventions

### Frontmatter (required on all notes)
```yaml
---
tags: [<domain-tag>, <org-tag>, <service-code>, <note-type>]
aliases: [<human readable names>]
role: <role-code>
created: YYYY-MM-DD
status: draft|review|complete|active|archived
type: MOC|guide|reference|config|adr|schema
related:
  - "[[path/to/related-note|Display Name]]"
---
```

Full schema: `schema.md`

### Service Codes
`000MST` `000DOL` `000GIT` `000LLM` `000NCL` `000WEB` `000INF` `000K8S`

### Role Codes
[Your role codes here]

### Wikilinks
Always use full path from vault root with display text:
`[[Domain/Subfolder/Note|Display Title]]`

### File Naming
- Folders: `Title Case` or `NN - Title Case`
- Notes: `Title Case.md`
- HOME.md = folder index (MOC type)

---

## Writing Guidelines

- Follow frontmatter schema exactly
- Use Obsidian wikilinks for internal links
- `Last updated: YYYY-MM-DD` footer on every doc
- No duplication: link to existing docs rather than repeating content
- `active` status for living docs, `complete` for point-in-time references
