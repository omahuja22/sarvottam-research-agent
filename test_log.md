# Test log — three local regression runs

Date used by the assignment: 23 September 2026.

**Transparency note:** these are three local offline-path regression runs of this prototype, not three external LLM API calls. The LLM mode is available but requires an API key; no API key was provided in this environment. If you run the LLM mode, replace/add entries with the exact model, prompts, outputs, and observations from those real runs.

## Run 1 — baseline source inclusion
- **Design:** read the provided Markdown files and summarize all cable-related articles.
- **Observed issue during review:** a naive all-document summary could conflate the local “Sarvottam Cable Network” cable-TV operator with Sarvottam Cables Ltd, the listed fictional manufacturer.
- **Change:** added exact ticker/legal-name matching and an explicit exclusion note for the similarly named entity.

## Run 2 — source hierarchy and numeric conflicts
- **Design:** prioritize documents mentioning the exact company and extract headline financial data.
- **Observed issue during review:** the news article says Q1 revenue was ₹1,428 crore (+35%), while the official company release says ₹1,248 crore (+18%).
- **Change:** the brief prioritizes the official release for reported results and flags the mismatch as an open question rather than silently choosing one number.

## Run 3 — final evidence-first prompt and guardrails
- **Design:** added a separate system prompt, inline source IDs, source dates/URLs, handling for stale/conflicting claims, and instruction-injection resistance.
- **Observed checks:** generated brief contains all five required sections; identifies GST demand of ₹46.3 crore; distinguishes management guidance from achieved results; treats the promotional ₹1,450 target as unverified; excludes the similarly named cable-TV operator.
- **Remaining limitation:** offline mode is deterministic and tailored to this test pack. Generalization and the LLM API path still need a live run with a configured key.

## Quick repeatability check
Command used:
```bash
python agent.py --ticker SRVCABLE --mode offline --output generated_brief.md
```

Automated assertions passed in this environment: all five sections present; GST demand surfaced; conflicting revenue figures both surfaced; similarly named local operator excluded; promotional buy claim not repeated as a recommendation. The blog's title remains listed as a source title but its claim is explicitly described as promotional and unverified. These assertions verify the offline path only.

Follow-up QA fix: included the earnings-call transcript using its supplied research-pack identity because the excerpt itself did not repeat the ticker string. Verified that management-guidance claims now have source [2] and that source [2] appears in the source list.
