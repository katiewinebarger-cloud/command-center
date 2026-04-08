# Command Center

A personal AI-powered dashboard built for [Claude Code](https://claude.ai/claude-code). Dark, minimal, and fully configurable.

![Dashboard Preview](https://img.shields.io/badge/status-active-00bcd4?style=flat-square)

## Features

- **Today's Schedule** — Live Google Calendar integration with click-to-expand detail view
- **Slack Pulse** — Channel activity feed with @mention highlighting
- **Energy Intel** — Live commodity pricing (customizable)
- **Weather** — Real-time weather via Open-Meteo API (free, no key needed)
- **Cowork Skills** — AI-powered skill cards that generate content via Claude API
  - Morning Briefing, Meeting Takeaways, Executive Coaching, Customer Intelligence, Slack Digest, Energy Report
  - Expandable Skills Library with Slide Builder, Spreadsheet Builder, PDF Tools, and more
  - Fully configurable via `skills.json`
- **Content Workbench** — Quick-action content templates
- **Actions Panel** — Generate Slack messages, reports, memos, and emails with Claude
- **Task Checklist** — Persistent daily checklist (localStorage)

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_ORG/command-center.git
cd command-center
```

### 2. Set up your config

```bash
cp config.example.js config.js
```

Edit `config.js` with your details:

```javascript
const CONFIG = {
  USER_NAME: 'Your Name',
  COMPANY_NAME: 'Your Company',
  ANTHROPIC_API_KEY: 'sk-ant-...',       // from console.anthropic.com
  MODEL: 'claude-sonnet-4-20250514',
  WEATHER_LAT: 30.2672,                  // your city latitude
  WEATHER_LON: -97.7431,                 // your city longitude
  WEATHER_CITY: 'Austin',
  WEATHER_UNIT: 'fahrenheit',            // or 'celsius'
  WEATHER_TIMEZONE: 'America/Chicago',
  SLACK_MENTION: '@yourname',
};
```

### 3. Set up your data files

```bash
cp calendar.example.json calendar.json
cp slack-pulse.example.json slack-pulse.json
```

These will be populated automatically if you set up the scheduled refresh (see below), or you can edit them manually.

### 4. Start the server

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

## Customizing Skills

Edit `skills.json` to add, remove, or modify skill cards. Each skill has:

```json
{
  "id": "unique-id",
  "name": "Display Name",
  "icon": "emoji",
  "description": "One-line description",
  "system": "System prompt for Claude API",
  "prompt": "Auto-run prompt (optional)",
  "inputLabel": "Input field label",
  "inputPlaceholder": "Placeholder text...",
  "topSkill": true
}
```

Skills in the `"library"` array appear in the collapsible Skills Library section.

## Auto-Refresh with Claude Code

If you use Claude Code with Google Calendar and Slack MCP integrations, you can set up a scheduled task to auto-refresh your dashboard data daily:

```
/schedule Create a daily task at 7am that fetches today's Google Calendar
events and Slack channel updates, then writes them to calendar.json
and slack-pulse.json
```

## File Structure

```
command-center/
  index.html              # The dashboard (all HTML/CSS/JS in one file)
  config.js               # Your personal config (gitignored)
  config.example.js       # Template config for new users
  skills.json             # Skill card definitions
  calendar.json           # Today's calendar events (gitignored)
  calendar.example.json   # Sample calendar data
  slack-pulse.json        # Slack channel feed (gitignored)
  slack-pulse.example.json # Sample Slack data
  history.json            # Skill history from local files (gitignored)
  scan_history.py         # Script to scan local files for history
  .claude/launch.json     # Dev server config for Claude Code
```

## Tech Stack

- **Zero dependencies** — pure HTML, CSS, and vanilla JavaScript
- **Claude API** — powers skill generation and actions (via `anthropic-dangerous-direct-browser-access`)
- **Open-Meteo API** — free weather data (no API key needed)
- **localStorage** — persists task checklist across sessions
- All data loaded from JSON files — easy to integrate with any backend

## Deploying

### GitHub Pages

1. Push to GitHub
2. Go to Settings > Pages > Source: `main` branch
3. Your dashboard is live at `https://yourorg.github.io/command-center/`

> Note: API calls to Anthropic require `config.js` to be present. For shared deployments, each user needs their own API key configured in their browser's localStorage or a server-side proxy.

### Any Static Host

This is a single `index.html` with JSON data files. Deploy to Vercel, Netlify, Cloudflare Pages, or any static file server.

---

Built with [Claude Code](https://claude.ai/claude-code)
