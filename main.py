
from chains.extraction_chain import extraction_chain
from utils.scoring_engine import calculate_score
import json
import re

print("🚀 HireSense AI – Intelligent Resume Screening System\n")

# -----------------------------
# RESUMES
# -----------------------------
strong_resume = """
Data Scientist with 4 years experience.
Skills: Python, Machine Learning, Deep Learning, SQL
Tools: Pandas, NumPy, TensorFlow
"""

average_resume = """
Data Analyst with 2 years experience.
Skills: Python, SQL
Tools: Pandas, Excel
"""

weak_resume = """
Fresher looking for job.
Skills: Python basics
"""

job_skills = ["Python", "Machine Learning", "Deep Learning", "SQL"]

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
# FUNCTION TO RUN PIPELINE
# -----------------------------
def run_pipeline(name, resume):
    print("\n" + "="*50)
    print(f"🔹 {name}")
    print("="*50)

    extracted = extraction_chain.invoke({"resume": resume})
    extracted = safe_json_parse(extracted)

    print("\n📌 Extracted Data:")
    print(extracted)

    result = calculate_score(extracted["skills"], job_skills)

    print("\n📊 Score Result:")
    print(result)


# -----------------------------
# RUN ALL CANDIDATES
# -----------------------------
print("🚀 Running Resume Screening for All Candidates...\n")

run_pipeline("STRONG CANDIDATE", strong_resume)
run_pipeline("AVERAGE CANDIDATE", average_resume)
run_pipeline("WEAK CANDIDATE", weak_resume)

print("\n✅ Pipeline Execution Completed Successfully!")