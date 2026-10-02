# System Architecture

```text
                    USER
                      |
                      v
             +------------------+
             |  Single-file UI  |
             | HTML/CSS/JS      |
             +--------+---------+
                      |
             +--------v---------+
             | Input Validation |
             | Budget Logic     |
             +--------+---------+
                      |
             +--------v---------+
             | Prompt Builder   |
             +--------+---------+
                      |
             +--------v---------+
             | Gemini REST API  |
             | Generative AI    |
             +--------+---------+
                      |
             +--------v---------+
             | Recommendation   |
             | Renderer         |
             +--------+---------+
                      |
            +---------+----------+
            |                    |
            v                    v
       Browser UI          LocalStorage
                         (history/settings)
```

## Design Principle
The budget is treated as a hard constraint in the prompt. The model is asked to provide estimated allocations that do not exceed the stated budget and to label estimates appropriately.
