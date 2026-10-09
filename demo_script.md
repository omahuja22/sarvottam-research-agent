# 2–3 minute demo walkthrough

**Before recording:** open a terminal in this folder and run `streamlit run app.py`, or run `python agent.py --ticker SRVCABLE --mode offline --output generated_brief.md`. Record the actual app/terminal, not a mock-up.

## Suggested script (about 2 minutes)

**0:00–0:20 — Introduce it**
“Hi, this is my evidence-first equity research agent. It takes a ticker and a folder of documents and creates a one-page brief with a snapshot, bull case, bear case, open questions, and sources. This case is fictional, and I’ve kept the agent restricted to the supplied documents.”

**0:20–0:55 — Run it**
Enter `SRVCABLE` and generate the brief. Point out the Q1 results and source references. If running offline mode, say so accurately. If you configured the API, identify the exact model you used.

**0:55–1:30 — Design decision**
“One design decision I’m proud of is that the agent doesn’t blindly trust every retrieved document. The official release and a news article disagree on revenue, so the brief prioritizes the official company release and explicitly flags the discrepancy. It also ignores instructions embedded in a promotional blog and treats the ₹1,450 target as unverified.”

**1:30–2:00 — Limitation**
“One limitation is that the agent only works from the supplied document pack and doesn’t independently verify the source or estimate fair value. The offline mode is rule-based; the LLM mode requires an API key and should be evaluated with repeated runs.”

**2:00–2:15 — Close**
“The goal is not to produce a buy/sell call. It’s to help a retail investor see the evidence, counter-evidence, and unanswered questions quickly.”
