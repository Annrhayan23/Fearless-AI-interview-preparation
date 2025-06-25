import streamlit as st
from ollama_nlp import analyze_soft_skills
from aptitude import get_question
from feedback import check_answer

# Setup the page
st.set_page_config(page_title="Fearless | AI Interview & Aptitude Bot", layout="centered")

# ----------- GLOBAL BACKGROUND CSS ----------- #
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://cdn.wallpapersafari.com/24/2/CgOJNk.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .centered-title {
        text-align: center;
        color: #FF6F61;
        font-size: 60px;
        font-weight: bold;
    }
    .centered-subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
        color: #ffffff;
    }
    .stButton>button {
        font-size: 18px;
        padding: 12px 30px;
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# ----------- NAVIGATION STATE ----------- #
if "page" not in st.session_state:
    st.session_state.page = "home"

# ----------- HOME PAGE ----------- #
if st.session_state.page == "home":
    st.markdown("<div class='centered-title'>FEARLESS</div>", unsafe_allow_html=True)
    st.markdown("<div class='centered-subtitle'>Empowering your interview and aptitude preparation with AI.</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Start Your Journey 🚀"):
            st.session_state.page = "main"
            st.rerun()

# ----------- MAIN PAGE ----------- #
elif st.session_state.page == "main":
    st.title("🤖 AI Interview & Aptitude Bot using Ollama")

    mode = st.radio("Select Mode", ["Interview (Soft Skill)", "Aptitude Test"])

    if mode == "Interview (Soft Skill)":
        domain_questions = {
            "Data Science": "How would you explain a complex model to a non-technical stakeholder?",
            "Software Development": "Describe a time you had to fix a critical bug under pressure.",
            "Cybersecurity": "How do you prioritize security in a fast-paced dev environment?",
            "Cloud Computing": "How do you handle data privacy in cloud deployments?",
            "AI & ML": "How do you ensure fairness in AI model predictions?",
            "Web Development": "Describe how you handle cross-browser compatibility issues.",
            "Mobile App Dev": "How do you test your app for various screen sizes and OS versions?",
            "UI/UX Design": "How do you gather and implement user feedback?",
            "Product Management": "How do you handle conflicts between business and engineering teams?",
            "Business Analysis": "Tell me how you capture and communicate business requirements.",
            "DevOps": "Describe your experience with CI/CD pipelines.",
            "Database Admin": "How do you ensure database security and availability?",
            "Game Dev": "How do you balance performance and visual quality in games?",
            "Blockchain": "How do you explain blockchain to someone from a non-tech background?",
            "Embedded Systems": "What are the challenges in real-time embedded development?",
            "Computer Vision": "How do you evaluate the accuracy of an object detection model?",
            "NLP": "What are common issues when working with multi-language NLP systems?",
            "IT Support": "How do you deal with an angry or frustrated user?",
            "Testing / QA": "How do you decide what to automate in your tests?",
            "AR/VR": "What challenges do you face with AR user interaction design?",
            "Robotics": "How do you troubleshoot sensor failures in robotic systems?",
            "IoT": "What are major security concerns with IoT devices?",
            "Networking": "How would you diagnose intermittent network issues?",
            "IT Consulting": "How do you approach giving strategic tech advice to a client?",
            "Technical Writing": "How do you simplify complex technical content?"
        }

        domain = st.selectbox("Select Your Domain", list(domain_questions.keys()))
        st.write("🧠 Domain-Specific Question:")
        st.info(domain_questions[domain])
        user_input = st.text_area("Paste your response here:")

        if st.button("Analyze"):
            with st.spinner("Analyzing..."):
                result = analyze_soft_skills(user_input)
                st.success("Analysis Complete:")
                st.markdown(result)

    elif mode == "Aptitude Test":
        if "question" not in st.session_state:
            st.session_state.question, st.session_state.correct = get_question()
            st.session_state.answered = False
            st.session_state.feedback = ""

        st.write("🧩 Question:", st.session_state.question)
        user_ans = st.text_input("Your Answer:")

        if st.button("Check") and not st.session_state.answered:
            st.session_state.feedback = check_answer(user_ans, st.session_state.correct)
            st.session_state.answered = True

        if st.session_state.answered:
            st.write(st.session_state.feedback)
            if st.button("Next Question"):
                st.session_state.question, st.session_state.correct = get_question()
                st.session_state.answered = False
                st.session_state.feedback = ""


