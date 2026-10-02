# System Flow

START
→ Open PocketSmart AI
→ Choose Budget Planner or AI Recommendation
→ Enter budget and requirement
→ Validate input
→ Build structured Gemini prompt
→ Send request to Gemini
→ Receive generated recommendation
→ Display recommendation
→ Optionally save to History
→ Review or clear saved recommendations
→ END

## Failure Paths
- Missing/invalid budget → validation message.
- Missing API key → direct user to Settings or use Demo Mode.
- Gemini API error → display error and offer Demo Mode.
- Browser storage unavailable → application can still display current results, but history persistence may be unavailable.
