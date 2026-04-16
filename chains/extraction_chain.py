from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

# -------------------------
# LLM (UPDATED MODEL)
# -------------------------
llm = ChatGroq(model="llama-3.1-8b-instant")

# -------------------------
# PROMPT TEMPLATE
# -------------------------
extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are a strict information extraction system.

RULES:
- Return ONLY valid JSON
- No explanation
- No extra text

FORMAT:
{{
  "skills": [],
  "tools": [],
  "experience": ""
}}

Resume:
{resume}
"""
)

# -------------------------
# CHAIN
# -------------------------
extraction_chain = extraction_prompt | llm | StrOutputParser()