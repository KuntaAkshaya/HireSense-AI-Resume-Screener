from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

# -------------------------
# LLM (UPDATED MODEL)
# -------------------------
llm = ChatGroq(model="llama-3.1-8b-instant")

# -------------------------
# PROMPT TEMPLATE (FIXED)
# -------------------------
scoring_prompt = PromptTemplate(
    input_variables=["resume_data", "job_description"],
    template="""
You are a strict resume scoring engine.

RULES:
1. Only compare skills explicitly mentioned.
2. If all required skills are present → score 80–100
3. If 50% skills match → score 40–70
4. If less than 50% → score below 40
5. DO NOT assume skills
6. DO NOT hallucinate experience

Resume Data:
{resume_data}

Job Description:
{job_description}

Return ONLY valid JSON:
{{
  "score": 0,
  "matched_skills": [],
  "missing_skills": [],
  "explanation": ""
}}
"""
)

# -------------------------
# CHAIN
# -------------------------
scoring_chain = scoring_prompt | llm | StrOutputParser()