# Testing Report

## Test Environment
- Modern Chromium-based browser
- Desktop and mobile-width viewport
- Demo Mode without API key
- Live Gemini mode with a valid API key

## Expected Result
The application should remain usable when Gemini is unavailable by allowing Demo Mode. Calculations should be deterministic and client-side. Saved recommendations should persist through browser LocalStorage.

## Limitations
- API response quality depends on the selected Gemini model.
- Current prototype does not verify live market prices.
- Browser LocalStorage is not a multi-user database.
- Direct browser API use exposes the key to the local browser environment.
