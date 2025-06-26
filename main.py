from fastapi import FastAPI, UploadFile, Form
from parser import extract_text_from_pdf
from scorer import compute_score

app=FastAPI()

@app.get("/")
def first_page():
    return "API is working"

@app.post("/rank")
async def rank_resume(resume: UploadFile, job_description: str=Form(...)):
    contents = await resume.read()
    resume_text = extract_text_from_pdf(contents)
    score, suggestions = compute_score(resume_text, job_description)
    return {"score": score, "suggestions": suggestions}