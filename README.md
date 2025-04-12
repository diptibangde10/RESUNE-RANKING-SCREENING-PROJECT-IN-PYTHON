# AI Resume Screening & Candidate Ranking System

This is an AI-based Resume Screening and Candidate Ranking System using Streamlit. It evaluates the similarity between a given job description and uploaded resumes (PDF format) using **TF-IDF** and **Cosine Similarity**.

## Features

- **Job Description Input**: Users can provide the job description for screening resumes.
- **Resume Upload**: Users can upload resumes in PDF format.
- **Ranking System**: The system ranks the uploaded resumes based on their similarity to the job description using **TF-IDF** and **Cosine Similarity**.

## Technologies Used

- **Python**: Programming language for backend logic.
- **Streamlit**: Web framework for creating the app.
- **PyPDF2**: For extracting text from PDF files.
- **Scikit-learn**: For performing **TF-IDF** and calculating **Cosine Similarity**.
- **NLTK**: For natural language processing tasks like tokenization.

## Requirements

1. Python (>=3.6)
2. Install the following libraries:
   - `streamlit`
   - `PyPDF2`
   - `scikit-learn`
   - `nltk`

## Installation

### Clone the repository:

```bash
git clone https://github.com/diptibangde10/RESUNE-RANKING-SCREENING-PROJECT-IN-PYTHON.git
cd RESUNE-RANKING-SCREENING-PROJECT-IN-PYTHON
