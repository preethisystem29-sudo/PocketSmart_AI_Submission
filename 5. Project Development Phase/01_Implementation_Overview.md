# Implementation Overview

The working application is delivered as `PocketSmart_AI.html` in the repository root.

## Modules Inside the Single File
1. Responsive UI and navigation.
2. Dashboard.
3. Budget planner.
4. AI recommendation form.
5. Gemini REST API integration.
6. Demo recommendation generator.
7. Recommendation renderer.
8. LocalStorage history.
9. Settings for API key and model.
10. Clipboard copy.

## Running
Open `PocketSmart_AI.html` in a modern browser.

No build step is required for Demo Mode.

For live AI generation:
1. Open Settings.
2. Enter a Gemini API key.
3. Select a model available to your API project.
4. Save Settings.
5. Open AI Recommendation and generate.

## Security Note
The single-file version stores the API key in browser LocalStorage and calls Gemini directly from the browser. This is acceptable only for a controlled classroom prototype. A production deployment should use a backend proxy and server-side secret storage.
