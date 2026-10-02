# Functional Test Cases

| ID | Test | Input | Expected |
|---|---|---|---|
| TC01 | Page load | Open HTML | Dashboard loads |
| TC02 | Budget calculation | 50000 / 42000 | Remaining = ₹8,000 |
| TC03 | Over-budget | 50000 / 55000 | Over-budget message |
| TC04 | Empty AI budget | blank | Validation message |
| TC05 | Demo generation | Category + budget | Recommendation displayed |
| TC06 | Save result | Generated result | History count increases |
| TC07 | Reopen history | Saved result | Result displayed |
| TC08 | Clear history | History present | History becomes empty |
| TC09 | Missing API key | Live generation | Settings prompt |
| TC10 | Invalid API response | Bad key/model | Error shown, app remains usable |
| TC11 | Mobile layout | Narrow viewport | Responsive layout |
| TC12 | Copy result | Generated result | Text copied where browser permits |

## Acceptance Criteria
All P0 functions must pass before submission.
