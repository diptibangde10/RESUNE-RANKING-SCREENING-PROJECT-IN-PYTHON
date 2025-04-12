# AI Resume Screening & Candidate Ranking System

This is an AI-based Resume Screening and Candidate Ranking System using Streamlit, which evaluates the similarity between a given job description and uploaded resumes (PDF format) using **TF-IDF** and **Cosine Similarity**.

## Features

- **Job Description Input**: User can provide the job description for screening resumes.
- **Resume Upload**: Users can upload resumes in PDF format.
- **Ranking System**: Ranks the uploaded resumes based on their similarity to the job description using **TF-IDF** and **Cosine Similarity**.

## Technologies Used

- **Python**: Programming language used for backend logic.
- **Streamlit**: Framework used for creating the web app.
- **PyPDF2**: Python library for extracting text from PDF files.
- **Scikit-learn**: For performing **TF-IDF** and calculating **Cosine Similarity**.
- **NLTK**: Natural Language Toolkit for text processing.

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

```
### Create and activate a virtual environment:

python -m venv venv
.\venv\Scripts\activate  # For Windows



### Install the required libraries:

pip install -r requirements.txt



### Usage

1. After installing the dependencies, run the app using Streamlit:
   streamlit run app.py
2. Open the app in the browser at http://localhost:8501.
3. Enter the job description, upload the resumes in PDF format, and click on Rank Resumes to see the ranking based on similarity.



### Folder Structure

Resume_Screening_App/
├── app.py                      ← Main Streamlit app
├── resumes/                    ← (Optional) Store uploaded resumes
├── requirements.txt            ← List of project dependencies
├── README.md                  ← Project overview and instructions



### Contributing
Feel free to fork this repo and contribute by creating pull requests!

### License
This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

