from langchain_core.prompts import PromptTemplate

extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are HireSense AI, an intelligent resume screening system.

Extract the following:
- Skills
- Tools
- Experience

Rules:
- Do NOT assume anything
- Only extract from given text

Resume:
{resume}

Output JSON:
{{
    "skills": [],
    "tools": [],
    "experience": ""
}}
"""
)