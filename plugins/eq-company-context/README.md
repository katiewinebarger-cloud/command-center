# EQ Company Context Plugin

Grounds Claude in Equilibrium Energy's internal knowledge by connecting to the **AI-CONTEXT-COMPANY** Google Drive vault.

## What It Does

When you're working on internal tasks, this plugin helps Claude draw on EQ's actual strategy, product thinking, brand voice, culture, and more — rather than generic answers. It knows where each type of context lives in the Drive and searches the right folder automatically.

## Components

| Component | Type | Purpose |
|-----------|------|---------|
| `company-context` | Skill | Discovers and searches the AI-CONTEXT-COMPANY Drive vault for relevant internal context |
| `eq-slides` | Skill | Creates EQ-branded PowerPoint presentations using the bundled EQ template |

## Requirements

- Google Drive connector must be enabled in Cowork (for `company-context` and brand guidance in `eq-slides`)

## Usage

The skill triggers automatically when you ask things like:
- "Help me write this using our company context"
- "What's EQ's approach to..."
- "Use our internal docs to..."
- "How do we talk about PowerOS?"

You can also explicitly invoke it by mentioning "company context" or "EQ context" in your request.

## Context Domains

The vault is organized into 9 domains — strategy, product, brand, culture, people, gtm, ops, finance, and program_management. Claude will search the relevant domain(s) based on your task.

## Confidentiality

All content in the vault is **internal only**. Claude will never incorporate this context into external-facing outputs.

## Iteration Notes

This is v0.1.0 — the starting point. Future versions may add:
- Commands for specific context-retrieval workflows
- Additional domain-specific skills
- Richer reference documents baked into the plugin itself
