---
name: eq-slides
description: >
  Use this skill when the user wants to create or edit PowerPoint presentations
  for Equilibrium Energy — including pitch decks, internal presentations,
  customer slides, team updates, or any EQ-branded slide content.

  Trigger phrases include: "make slides", "create a deck", "build a presentation",
  "EQ slides", "EQ deck", "make a PowerPoint", "create slides for", "put together
  a deck", "EQ-branded presentation", "EQ template".

  Always use this skill alongside the pptx skill for EQ presentation work.
version: 0.1.0
---

# EQ Slides Skill

Create EQ-branded PowerPoint presentations using the official template.

## Template

The EQ template is bundled with this plugin:

```
${CLAUDE_PLUGIN_ROOT}/skills/eq-slides/assets/eq-template.pptx
```

Always start from this template — it has EQ's brand (colors, fonts, layouts) built in. Copy it to a working location before modifying.

## Process

1. **Also load the `pptx` skill** — it handles all technical creation and editing mechanics
2. **Copy the template** to your working directory before making any changes
3. **Build the deck** using the template as the base, following the pptx skill's editing workflow
4. **For brand voice or messaging guidance**, discover and search the `brand` domain in the AI-CONTEXT-COMPANY vault (root folder ID: `0AFTdyEVSGGNJUk9PVA`) — find the brand subfolder by listing the root

## Rules

- Always start from the template — never create EQ slides from scratch without it
- Preserve EQ's brand elements (colors, fonts, logo placement) from the template
- For internal decks, company context from the Drive is fair game
- For external-facing decks, do not pull from the internal context vault

## If Something Goes Wrong

**Drive connector not available or permission error when fetching brand guidance**: This is non-fatal — the template is bundled locally and slides can still be created without it. Proceed with the template, and let the user know that brand voice guidance from the Drive wasn't available so they may want to review messaging themselves.
