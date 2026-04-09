---
name: company-context
description: >
  Use this skill whenever the user asks Claude to help with internal Equilibrium
  Energy work that would benefit from company context — including tasks involving
  EQ's strategy, product direction, brand voice, company culture, people and HR
  topics, go-to-market, operations, finance, or program management.

  Trigger phrases include: "use our company context", "check the context drive",
  "what does EQ say about", "using our internal docs", "grounded in EQ context",
  "what's our approach to", "how do we talk about", "our strategy around",
  "EQ brand voice", "company background", "internal context".

  Always use this skill for tasks where EQ-specific framing, terminology, or
  positioning matters. Never apply this context to external-facing outputs.
version: 0.1.0
---

# EQ Company Context Skill

Pull from the **AI-CONTEXT-COMPANY** Google Drive vault (root folder ID: `0AFTdyEVSGGNJUk9PVA`) to ground responses in EQ's actual internal knowledge.

## Process

1. **Discover** — list the root folder's children to find available domains and their folder IDs
2. **Orient** — read the `_README.md` in relevant subfolders to understand what each contains
3. **Search** — query the relevant subfolder(s) for documents pertaining to the task
4. **Ground** — use EQ's actual language and framing in the response

## Rules

- **Internal only** — never incorporate this context into external-facing outputs
- **Discover, don't assume** — always check the live folder structure rather than relying on prior knowledge of what folders exist

## If Something Goes Wrong

**Drive connector not available**: Stop and tell the user that this skill requires the Google Drive connector to be enabled in Cowork. Do not attempt to proceed without it.

**Permission error or empty results on the root folder**: Stop and tell the user clearly that they may not have been granted access to the AI-CONTEXT-COMPANY vault yet, and that they will likely be granted access in the coming weeks. Do not silently continue or guess at context.
