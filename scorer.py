from sentence_transformers import SentenceTransformer, util
import re

model = SentenceTransformer('all-MiniLM-L6-v2')

def clean_text(text):
    text = re.sub(r'\W+', ' ', text)
    return text.lower()

def compute_score(resume_text, job_desc):
    resume_text_clean = clean_text(resume_text)
    job_desc_clean = clean_text(job_desc)

    resume_embedding = model.encode(resume_text_clean, convert_to_tensor=True)
    jd_embedding = model.encode(job_desc_clean, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, jd_embedding).item()
    score = round(similarity * 100, 2)

    jd_keywords = set(job_desc_clean.split())
    resume_keywords = set(resume_text_clean.split())
    missing_keywords = list(jd_keywords - resume_keywords)
    suggestions = missing_keywords[:10]

    return score, suggestions