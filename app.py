import streamlit as st
from chains.extraction_chain import extraction_chain
from utils.scoring_engine import calculate_score
import json
import re

st.title("HireSense AI - Resume Screener")

# -----------------------------
# SAFE JSON PARSER
# -----------------------------
def safe_json_parse(text):
    if not text:
        return {"skills": [], "tools": [], "experience": ""}

    text = text.replace("```json", "").replace("```", "")

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        return json.loads(match.group())

    return {"skills": [], "tools": [], "experience": ""}


# -----------------------------
# INPUT
# -----------------------------
resume = st.text_area("Paste Resume")
job = st.text_area("Paste Job Description")

# -----------------------------
# RUN BUTTON
# -----------------------------
if st.button("Analyze"):

    # STEP 1: Extraction
    extracted = extraction_chain.invoke({"resume": resume})
    extracted = safe_json_parse(extracted)

    st.subheader("🔹 Extracted Data")
    st.write(extracted)

    # -----------------------------
    # 🔥 FIXED JOB SKILL EXTRACTION
    # -----------------------------
    allowed_skills = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "SQL"
    ]

    job_skills = [skill for skill in allowed_skills if skill.lower() in job.lower()]

    # -----------------------------
    # STEP 3: Scoring
    # -----------------------------
    result = calculate_score(
        extracted["skills"],
        job_skills
    )

    st.subheader("🔹 Score Result")
    st.write(result)