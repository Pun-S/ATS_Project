# AI Resume Ranker

AI Resume Ranker is a web and API application that evaluates how well a resume matches a given job description using advanced natural language processing. It provides a match score and highlights missing keywords to help users optimize their resumes for specific job postings.

## Features

- **Streamlit Web App**: Upload your resume (PDF) and paste a job description to get an instant match score and suggestions for improvement.
- **FastAPI Backend**: REST API for programmatic access to resume ranking and keyword suggestions.
- **Semantic Matching**: Uses state-of-the-art sentence embeddings to compare resume and job description content.
- **Keyword Suggestions**: Identifies top missing keywords from the job description.

## Demo

## Getting Started

### Prerequisites

- Python 3.7+

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ATS-Project.git
   cd ATS-Project
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Web App (Streamlit)

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the provided local URL in your browser. Upload a PDF resume and paste a job description to get your match score.

### API (FastAPI)

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

#### Endpoints

- `GET /` — Health check, returns "API is working"
- `POST /rank` — Rank a resume against a job description
  - **Form Data:**
    - `resume`: PDF file
    - `job_description`: string
  - **Response:**
    ```json
    {
      "score": 87.5,
      "suggestions": ["python", "leadership", ...]
    }
    ```

## How it Works

- **PDF Parsing:** Extracts text from uploaded PDF resumes using `pdfplumber`.
- **Semantic Scoring:** Computes similarity between resume and job description using `sentence-transformers`.
- **Keyword Analysis:** Finds missing keywords from the job description in the resume.

## Dependencies

- fastapi
- uvicorn
- pdfplumber
- python-dotenv
- sentence-transformers
- torch
- streamlit

Install all dependencies with `pip install -r requirements.txt`.

## License

[MIT](LICENSE)

## Acknowledgements

- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)

---

Feel free to contribute or open issues for suggestions and improvements!
