# app.py

import streamlit as st
from generator import (
    generate_resume_bullets,
    generate_cover_letter,
    generate_match_score
)
from resume_parser import extract_text_from_pdf
import os
from dotenv import load_dotenv
api_key = st.secrets["PPLX_API_KEY"]

load_dotenv()

# ---------------- UI CONFIG ----------------
st.set_page_config(
    page_title="GenAI Job Optimizer",
    layout="wide",
    page_icon="💼"
)

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align: center; color: #0d6efd;'>🚀 Job Application Optimizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Boost your job applications using GenAI — tailor your resume, write a cover letter, and match the JD with ease.</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- SIDEBAR INPUTS ----------------
with st.sidebar:
    st.header("📂 Upload Inputs")
    uploaded_file = st.file_uploader("Upload your Resume (PDF only):", type=["pdf"])

    st.markdown("### 📋 Paste Job Description")
    job_desc = st.text_area("Job Description", height=250)

    st.markdown("---")
    generate = st.button("🚀 Generate Optimized Output")

# ---------------- PROCESSING ----------------
if generate:
    if not uploaded_file or not job_desc:
        st.warning("⚠️ Please upload a resume and paste a job description before continuing.")
    else:
        with st.spinner("🔍 Analyzing and generating..."):
            resume_text = extract_text_from_pdf(uploaded_file)

            bullets = generate_resume_bullets(resume_text, job_desc)
            cover_letter = generate_cover_letter(resume_text, job_desc)
            match_score = generate_match_score(resume_text, job_desc)

        # ---------------- OUTPUT DISPLAY ----------------
        tab1, tab2, tab3 = st.tabs(["✅ Resume Bullets", "✉️ Cover Letter", "📊 JD Match Score"])

        with tab1:
            st.subheader("Optimized Resume Bullets")
            st.code(bullets)

        with tab2:
            st.subheader("Generated Cover Letter")
            st.code(cover_letter)

        with tab3:
            st.subheader("Resume to JD Match Report")
            st.code(match_score)

        st.success("🎉 All done! You can now copy or save your optimized content.")
