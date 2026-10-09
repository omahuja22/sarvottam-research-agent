import streamlit as st
from agent import generate, PACK, read_docs

st.set_page_config(page_title="Evidence-First Research Agent", page_icon="📊", layout="wide")
st.title("📊 Evidence-First Equity Research Agent")
st.caption("Generate a concise, source-grounded research brief from a local document pack.")
ticker = st.text_input("NSE ticker", value="SRVCABLE").strip().upper()
mode = st.radio("Run mode", ["Offline evidence rules (no API key)", "LLM API (OpenAI-compatible)"], horizontal=True)
st.info("The included case is fictional. This tool summarizes supplied documents; it does not provide investment advice.")
if st.button("Generate research brief", type="primary"):
    try:
        with st.spinner("Reading documents and preparing brief..."):
            result = generate(ticker, "llm" if mode.startswith("LLM") else "offline")
        st.markdown(result)
        st.download_button("Download Markdown brief", result, file_name=f"{ticker.lower()}_research_brief.md", mime="text/markdown")
    except Exception as exc:
        st.error(str(exc))
with st.expander("Documents loaded"):
    for d in read_docs():
        st.write(f"- **{d['file']}** — {d['source']} ({d['published']})")
st.caption("Design choice: official disclosures are prioritized, conflicting figures are surfaced, prompt injection and similarly named entities are treated as untrusted input.")
