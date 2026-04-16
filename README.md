# 🚀 HireSense AI - Resume Screening System

## 📌 Project Overview
HireSense AI is an intelligent resume screening system built using LangChain and LLMs.  
It extracts skills from resumes, matches them with job descriptions, and provides an AI-based score with explanation.

---

## 🧠 Features
- Resume Skill Extraction using LLM
- Job Description Matching
- AI Scoring System (0–100)
- Strong / Average / Weak candidate evaluation
- Streamlit UI for interaction
- LangChain pipeline architecture

---

## ⚙️ Tech Stack
- Python
- LangChain
- Streamlit
- LLM (Groq / OpenAI)
- Regex & JSON parsing

---

## 🔄 Pipeline Flow
Resume → Extraction → Matching → Scoring → Output

---

## 📁 Project Structure
chains/ → LangChain logic  
prompts/ → Prompt templates  
utils/ → Helper functions  
main.py → CLI runner  
app.py → Streamlit UI  

---

## 🚀 How to Run

### 1. Streamlit UI (Recommended)
```bash
streamlit run app.py
python main.py