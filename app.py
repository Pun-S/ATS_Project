import streamlit as st
from parser import extract_text_from_pdf
from scorer import compute_score
import io

st.set_page_config(page_title="AI Resume Ranker", layout="centered")
st.title("📄 AI Resume Ranker")

st.markdown("Upload your **resume (PDF)** and paste a **job description** to evaluate the match.")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

job_desc = st.text_area("Paste Job Description Here", height=200)

if st.button("🔍 Evaluate", key="evaluate_button"):
    if uploaded_file and job_desc.strip():
        with st.spinner("Analyzing resume..."):
            resume_bytes = uploaded_file.read()
            resume_text = extract_text_from_pdf(resume_bytes)
            score, suggestions = compute_score(resume_text, job_desc)

        st.success(f"✅ Match Score: {score}%")
        st.markdown("**🔑 Top Missing Keywords:**")
        st.write(", ".join(suggestions) if suggestions else "🎉 No missing keywords! Strong match!")
    else:
        st.error("Please upload a resume and enter job description.")