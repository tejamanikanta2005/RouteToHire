# MY FIRST PROJECT
import streamlit as st
from helper import ask_gemini
from pdf_reader import extract_text_from_pdf

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="RouteToHire",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🚀 RouteToHire")

st.sidebar.markdown("""
### Welcome!

Your personal AI Career Assistant.

# 🚀 RouteToHire

Helping job seekers with AI-powered career guidance.

### ✨ Features

- 📄 Resume Analyzer
- 💼 Job Match Analysis
- ✍️ AI Cover Letter Generator
- 🎤 AI Interview Coach
- 📊 Skill Gap Analyzer
- 📥 Download Reports

---

### 🛠️ Tech Stack

- 🐍 Python
- 🎨 Streamlit
- 🤖 Google Gemini AI
- 📄 PDF Processing

---

### 👨‍💻 Developed By

**Teja Manikanta Sala**


Python • Streamlit • Gemini AI

---

⭐ Thank you for using AI Job Assistant!

Good luck with your placements and interviews! 🚀
""")

# --------------------------------------------------
# Upload Resume (GLOBAL)
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload Your Resume (PDF)",
    type=["pdf"]
)

resume_text = ""

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.success("✅ Resume Uploaded Successfully!")

# --------------------------------------------------
# Create Tabs
# --------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📄 Resume Analyzer",
        "✍️ Cover Letter",
        "🎤 Interview Coach",
        "📊 Skill Gap"
    ]
)

# ==================================================
# TAB 1
# Resume Analyzer
# ==================================================

with tab1:

    st.header("📄 Resume Analyzer")

    if uploaded_file:

        with st.expander("📄 Resume Preview"):

            st.write(resume_text[:1200])

        job_description = st.text_area(
            "Paste Job Description",
            height=220,
            placeholder="Paste the company's job description here..."
        )

        if st.button(
            "🚀 Analyze Resume",
            use_container_width=True
        ):

            if job_description.strip() == "":

                st.warning(
                    "Please paste a Job Description."
                )

            else:

                with st.spinner(
                    "Analyzing Resume..."
                ):

                    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze this resume against the given Job Description.

Provide:

# Job Match Score

# Matching Skills

# Missing Skills

# Resume Improvements

# Learning Roadmap

Resume:

{resume_text}

Job Description:

{job_description}
"""

                    response = ask_gemini(prompt)

                st.success("✅ Analysis Complete")

                st.markdown(response)
                st.download_button(
    "📥 Download Analysis",
    data=response,
    file_name="Resume_Analysis.txt",
    mime="text/plain"
)

    else:

        st.info(
            "Upload your resume above to begin."
        )

# ===== CONTINUE WITH PART 2 =====
# =================================================
# TAB 2
# Cover Letter Generator
# =================================================

with tab2:

    st.header("✍️ AI Cover Letter Generator")

    if uploaded_file:

        company_name = st.text_input(
            "Company Name"
        )

        job_role = st.text_input(
            "Job Role"
        )

        cover_jd = st.text_area(
            "Paste Job Description (Optional)",
            height=200
        )

        if st.button(
            "📨 Generate Cover Letter",
            use_container_width=True
        ):

            if company_name.strip() == "" or job_role.strip() == "":

                st.warning(
                    "Please enter Company Name and Job Role."
                )

            else:

                with st.spinner("Generating Cover Letter..."):

                    cover_prompt = f"""
You are an expert career assistant.

Write a professional cover letter.

Candidate Resume:

{resume_text}

Company:

{company_name}

Job Role:

{job_role}

Job Description:

{cover_jd}

Instructions:

- Professional
- ATS friendly
- Fresher friendly
- One page
- Mention candidate strengths
- Mention relevant projects
- End politely
"""

                    cover_letter = ask_gemini(
                        cover_prompt
                    )

                st.success("✅ Cover Letter Generated")

                st.markdown(cover_letter)
                st.download_button(
    "📥 Download Cover Letter",
    data=cover_letter,
    file_name="Cover_Letter.txt",
    mime="text/plain"
)

    else:

        st.info(
            "📄 Please upload your resume first in the Resume Analyzer tab."
        )

# ===== CONTINUE WITH PART 3 =====
# ==================================================
# TAB 3
# AI Interview Coach
# ==================================================

with tab3:

    st.header("🎤 AI Interview Coach")

    if uploaded_file:

        interview_company = st.text_input(
            "Company Name",
            key="interview_company"
        )

        interview_role = st.text_input(
            "Job Role",
            key="interview_role"
        )

        interview_type = st.selectbox(
            "Interview Level",
            [
                "Fresher",
                "Internship",
                "Experienced"
            ]
        )

        if st.button(
            "🎯 Generate Interview Questions",
            use_container_width=True
        ):

            if interview_company.strip() == "" or interview_role.strip() == "":

                st.warning(
                    "Please enter Company Name and Job Role."
                )

            else:

                with st.spinner(
                    "Preparing interview questions..."
                ):

                    interview_prompt = f"""
You are an expert technical interviewer.

Candidate Resume:

{resume_text}

Company:

{interview_company}

Job Role:

{interview_role}

Interview Level:

{interview_type}

Generate:

# Technical Questions
(10 questions)

# HR Questions
(5 questions)

# Resume-Based Questions
(5 questions)

# Project-Based Questions
(5 questions)

# Tips to Crack the Interview

Keep the questions suitable for the selected interview level.
"""

                    interview_response = ask_gemini(
                        interview_prompt
                    )

                st.success("✅ Interview Questions Generated!")

                st.markdown(interview_response)
                st.download_button(
    "📥 Download Interview Questions",
    data=interview_response,
    file_name="Interview_Questions.txt",
    mime="text/plain"
)

    else:

        st.info(
            "📄 Please upload your resume first."
        )

# ===== CONTINUE WITH PART 4 =====
# ==================================================
# TAB 4
# AI Skill Gap Analyzer
# ==================================================

with tab4:

    st.header("📊 AI Skill Gap Analyzer")

    if uploaded_file:

        target_role = st.text_input(
            "Target Job Role",
            key="skill_role"
        )

        target_company = st.text_input(
            "Target Company (Optional)",
            key="skill_company"
        )

        skill_job_description = st.text_area(
            "Paste Job Description",
            height=250,
            placeholder="Paste the complete job description here..."
        )

        if st.button(
            "📈 Analyze Skill Gap",
            use_container_width=True
        ):

            if target_role.strip() == "" or skill_job_description.strip() == "":

                st.warning(
                    "Please enter the Job Role and paste the Job Description."
                )

            else:

                with st.spinner(
                    "Analyzing your skills..."
                ):

                    skill_prompt = f"""
You are an expert AI Career Coach.

Candidate Resume:

{resume_text}

Target Company:

{target_company}

Target Job Role:

{target_role}

Job Description:

{skill_job_description}

Analyze and provide the following:

# Overall Job Readiness Score (out of 100)

# Skills Already Present

# Missing Skills

# Important Tools & Technologies to Learn

# Priority Learning Order

# 30-Day Learning Roadmap

# Recommended Certifications

# Final Career Advice

Use bullet points wherever appropriate.
"""

                    skill_response = ask_gemini(
                        skill_prompt
                    )

                st.success("✅ Skill Gap Analysis Completed!")

                st.markdown(skill_response)
                st.download_button(
    "📥 Download Skill Gap Report",
    data=skill_response,
    file_name="Skill_Gap_Report.txt",
    mime="text/plain"
)

    else:

        st.info(
            "📄 Please upload your resume first."
        )

# ===== CONTINUE WITH PART 5 =====
# ==================================================
# FOOTER
# ==================================================

st.divider()

st.markdown(
    """
---
### 🚀 AI Job Assistant

Built with ❤️ using:

- 🐍 Python
- 🎨 Streamlit
- 🤖 Google Gemini API

This project helps job seekers:

- 📄 Analyze resumes
- 💼 Match resumes with Job Descriptions
- ✍️ Generate professional Cover Letters
- 🎤 Prepare for Interviews
- 📊 Find Skill Gaps & Learning Roadmaps

Happy Learning & Best of Luck! 🌟
"""
)

# ==================================================
# END OF APP
# ==================================================