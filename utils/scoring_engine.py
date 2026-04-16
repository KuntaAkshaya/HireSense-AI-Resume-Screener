def calculate_score(resume_skills, job_skills):
    resume_set = set([s.lower() for s in resume_skills])
    job_set = set([s.lower() for s in job_skills])

    matched = list(job_set & resume_set)
    missing = list(job_set - resume_set)

    score = (len(matched) / len(job_set)) * 100 if job_set else 0

    # 🔥 ADD LEVEL CLASSIFICATION
    if score >= 75:
        level = "Strong"
    elif score >= 50:
        level = "Medium"
    else:
        level = "Weak"

    return {
        "score": round(score),
        "level": level,   # ⭐ THIS IS WHAT YOU WERE MISSING
        "matched_skills": matched,
        "missing_skills": missing
    }