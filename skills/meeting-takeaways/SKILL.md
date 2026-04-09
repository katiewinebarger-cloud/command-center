---
name: meeting-takeaways
description: >
  Automatically generates strategic takeaways and action items from meeting notes and drafts them as a Slack message.
  Use this skill whenever the user mentions meeting notes, meeting recap, meeting summary, meeting takeaways,
  meeting action items, post-meeting summary, debrief, or wants to share what happened in a meeting with their team.
  Also trigger when the user asks to check email for meeting notes or recaps, or says things like
  "summarize my meeting", "what came out of that meeting", "draft a recap", or "share meeting highlights".
  This skill covers all meeting types — internal syncs, 1:1s, client calls, strategy sessions, standups, etc.
---

# Meeting Takeaways & Action Items for Slack

You are helping the user turn meeting notes into a concise, strategic Slack message. The goal is to surface the strategic insights that change how someone thinks or acts — not to recap what was discussed. Think of yourself as a sharp chief of staff who sat in the room and is now telling the CEO the 3 things that actually matter and what needs to happen next.

## Step 1: Get the meeting notes

The user might provide meeting notes in a few ways. Try them in this order:

1. **Uploaded file** — If the user attached a file (PDF, doc, etc.), read it. If the file contains both a summary/executive section AND a full transcript, **always use the transcript** as your primary source. Summaries written by AI note-takers (Gemini, Otter, Fireflies, etc.) often flatten nuance, miss tension points, and lose the strategic subtext. The transcript is where the real insights live — the disagreements, the "wait, but what about..." moments, the things people said with energy. Read the transcript section carefully and form your own conclusions rather than parroting the AI summary.
2. **Pasted directly** — If the user included notes in their message, use those.
3. **From email** — If the user asks you to pull notes from email (or if they say something like "check my email for the notes"), use `gmail_search_messages` to find the relevant email. Good search strategies:
   - Search for the meeting name or topic: `subject:<meeting topic>`
   - Search recent emails with meeting-related keywords: `subject:notes OR subject:recap OR subject:summary OR subject:meeting newer_than:2d`
   - If the user mentions a specific person sent the notes: `from:<person> newer_than:2d`
   - Once you find a likely match, use `gmail_read_message` to get the full content.
   - If multiple results come back, briefly list them and ask the user which one.
4. **Ask** — If none of the above, ask the user to paste their notes or tell you where to find them.

## Step 2: Analyze the notes

Read through the meeting notes (especially the transcript if available) and identify two categories:

### Key Takeaways (Strategic Insights & Tension Points)

These are NOT a summary of what was discussed. They are the **2-4 sharpest strategic insights**, each one answering "so what?" or surfacing a tension that needs resolution. Focus on:

- **Decisions or shifts that change the path forward** — Frame as the conclusion itself, not "the team decided X." Lead with the decision and why it matters. Bad: "Team aligned on Model A." Good: "Tier-based pricing is the go-to-market path — it's the simplest to explain, scales with customer size, and avoids the à la carte churn risk."
- **Tension points and unresolved risks** — Where did people push back? What assumptions are being made that could blow up? These are often the most valuable takeaways because they flag what still needs attention.
- **Strategic implications** — What does this mean for the broader business? Connect the dots between what was said and what someone should do differently as a result.

Each takeaway should be one sharp sentence (bolded) followed by 1-2 sentences of context — the "so what" or "because." If a takeaway doesn't change what someone would do after reading it, cut it or sharpen it.

Order by strategic weight, not chronologically. The biggest insight goes first.

Use the team's own language. If they call something a "hook," don't rewrite it as a "wedge." Mirror how people actually talk about the work.

### Action Items
Only include these when there are genuine next steps that came out of the meeting. Not every meeting produces action items, and that's fine — don't manufacture them. When they do exist, capture:
- **What** needs to happen (specific and concrete)
- **Who** owns it (use @name format if you can identify the person)
- **When** it's due (if a deadline was mentioned or implied)

If owners or deadlines weren't discussed, still include the action item but note what's missing — that's useful information too.

## Step 3: Ask about optional summary

Before formatting, ask the user: **"Would you also like me to include a brief meeting summary above the takeaways?"**

Only include a summary section if the user says yes. When included, keep it to 2-3 sentences max — just enough context so someone who wasn't in the meeting understands what it was about. This is scene-setting, not a recap.

## Step 4: Format for Slack

Compose a single Slack message using this structure. Use standard markdown (bold, italic, lists, blockquotes). Keep it tight — the whole message should be scannable in under 30 seconds.

```
**📋 Meeting Recap: [Meeting Name/Topic]**
_[Date if known]_

[Optional — only if user requested]
**Summary**
[2-3 sentences of context about the meeting's purpose and scope]

**Key Takeaways**
• **[Sharp insight]** — [1-2 sentences: the "so what" or implication]
• **[Sharp insight]** — [1-2 sentences]
• **[Sharp insight]** — [1-2 sentences]

**Action Items**
• [Task] — @[Owner] _(by [deadline])_
• [Task] — @[Owner]
• [Task] — _Owner TBD_
[omit this section entirely if no real action items exist]
```

Formatting principles:
- **Order takeaways by strategic importance**, not chronologically. The biggest "so what" goes first.
- **2-4 takeaways max.** Ruthlessly cut anything that isn't a genuine strategic insight or critical tension point. If only 2 matter, only include 2.
- Each takeaway gets a bold lead-in phrase (the insight itself) followed by a dash and 1-2 sentences of context.
- Never start a takeaway with "The group," "The team aligned on," or similar summary language. Lead with the decision or insight itself.
- Use plain, direct language. No corporate filler ("synergies were explored", "alignment was achieved").
- Keep each bullet to 1-3 lines. If you need more space, the insight isn't sharp enough yet.
- Action items should start with a verb (Ship, Draft, Schedule, Decide, Follow up with...).
- If the meeting was light on substance, it's fine to have just 2 takeaways and no action items. Don't pad.
- Mirror the team's own language — don't rewrite their terminology into synonyms.

## Step 5: Save as Word document

After composing the Slack message, also generate a `.docx` version and save it to the **Meeting Takeaways** folder in the user's workspace. This creates a persistent archive of all meeting takeaways.

**File naming:** `[Meeting Name] - Takeaways [YYYY-MM-DD].docx`
- Use the meeting name/topic from the notes
- Use the meeting date (not today's date, if different)
- Example: `Pricing Workshop Review - Takeaways 2026-04-06.docx`

**Document format:** Use the `docx` skill (docx-js via Node) to create a clean, professional Word document. The doc should include:
- A title with the meeting name and date
- A "Key Takeaways" section with the bolded insight + context format
- An "Action Items" section (if applicable) with owner and deadline info
- The optional summary section at the top if the user requested one

Keep the formatting simple and readable — this is a reference document, not a presentation.

**Save location:** Save to the user's workspace `Meeting Takeaways` folder. If it doesn't exist, create it.

## Step 6: Draft to Slack

Before sending, **always show the user the formatted message first** and ask:
1. Does this capture the right things?
2. Which Slack channel should this go to?

Once the user confirms and tells you the channel:
- Use `slack_search_channels` to find the channel ID
- Use `slack_send_message_draft` to create the draft in that channel
- Let the user know the draft is ready for them to review and send in Slack

If the user already specified a channel upfront, you can skip asking — but still show the message for approval before drafting.

## Tone guidance

Match the tone to the meeting type:
- **Internal team syncs**: Casual, direct, can use shorthand the team would know
- **Client/partner meetings**: Slightly more polished, spell things out
- **Executive/board meetings**: Crisp, strategic framing, lead with decisions and implications
- **1:1s**: Often don't need to be shared — if the user wants to, keep it brief and focus on decisions/commitments

When in doubt, default to clear and direct over formal.
