// ══════════════════════════════════════════════════════════════
//  Command Center — Configuration
//  Copy this file to config.js and fill in your details.
//  config.js is gitignored so your API key stays private.
// ══════════════════════════════════════════════════════════════

const CONFIG = {
  // ── Your Info ──
  USER_NAME: 'Katie',                    // First name for greeting
  COMPANY_NAME: 'Equilibrium Energy',    // Your company (used in skill prompts)

  // ── Anthropic API ──
  ANTHROPIC_API_KEY: 'YOUR_API_KEY_HERE', // Get one at console.anthropic.com
  MODEL: 'claude-sonnet-4-20250514',      // Or 'claude-opus-4-20250514'

  // ── Weather ──
  WEATHER_LAT: 37.7749,                  // Your latitude
  WEATHER_LON: -122.4194,                // Your longitude
  WEATHER_CITY: 'San Francisco',         // Display name
  WEATHER_UNIT: 'fahrenheit',            // 'fahrenheit' or 'celsius'
  WEATHER_TIMEZONE: 'America/Los_Angeles',

  // ── Slack Highlight ──
  SLACK_MENTION: '@katie',               // Your @mention to highlight
};
