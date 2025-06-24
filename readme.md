# ATS-Score

A lightweight Streamlit-based web application that evaluates resumes using an Applicant Tracking System (ATS)-style scoring approach. Upload your resume and a job description to get instant feedback on how well your resume matches the job — helping you increase your chances of passing ATS filters.

![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

---

## 🚀 Features

- 📑 Upload your resume (PDF format)
- 🧠 Upload a job description text
- 📊 Get an ATS-style score instantly
- 🔍 See matched keywords and skill gaps
- ⚡ Fast and interactive Streamlit UI

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - for the front-end web UI
- **PyMuPDF** - to extract text from resumes
- **NLTK / Spacy** *(optional)* - for keyword parsing and text preprocessing

---

## 📦 Installation

```bash
git clone https://github.com/abhin9v/ATS-Score.git
cd ATS-Score
pip install -r requirements.txt
