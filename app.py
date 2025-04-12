import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np

# Download stopwords (only once)
nltk.download('punkt')
nltk.download('stopwords')

# Text extraction
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

# Resume ranking function
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents).toarray()

    job_description_vector = vectors[0].reshape(1, -1)
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity(job_description_vector, resume_vectors).flatten()
    return cosine_similarities

# 🌟 Streamlit UI
st.title("📄 AI Resume Screening & Candidate Ranking System")

# Input Job Description
st.header("📝 Job Description")
job_description = st.text_area("Enter the job description here")

# Upload resumes
st.header("📤 Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)

if st.button("🔍 Rank Resumes"):
    if not job_description:
        st.warning("Please enter a job description.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        resume_texts = []
        filenames = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resume_texts.append(text)
            filenames.append(file.name)

        # Calculate similarities
        similarities = rank_resumes(job_description, resume_texts)

        # Display ranking
        st.subheader("📊 Ranking Results:")
        ranking = sorted(zip(filenames, similarities), key=lambda x: x[1], reverse=True)

        for i, (name, score) in enumerate(ranking):
            st.write(f"**{i+1}. {name}** — Similarity: `{round(score*100, 2)}%`")
