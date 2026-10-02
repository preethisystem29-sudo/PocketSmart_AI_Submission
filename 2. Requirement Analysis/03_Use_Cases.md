# Use Cases

## UC1 — Calculate Budget
Actor: User
1. Open Budget Planner.
2. Enter available budget.
3. Enter planned spend.
4. Optionally enter reserve.
5. Click Calculate Budget.
6. System displays utilization and remaining amount.

## UC2 — Generate Recommendation
Actor: User
1. Select category.
2. Enter budget.
3. Enter requirement.
4. Enter preferences.
5. Optionally enter quantity.
6. Click Generate with Gemini.
7. System sends a structured prompt to Gemini.
8. System displays the response.

## UC3 — Save Recommendation
1. Generate a recommendation.
2. Click Save to History.
3. System stores the result in browser LocalStorage.
4. User can reopen it later.

## UC4 — Demo Mode
1. Enter a category and budget.
2. Click Try Demo Mode.
3. System generates a deterministic sample recommendation without an API call.
