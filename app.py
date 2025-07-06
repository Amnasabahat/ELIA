# app.py

import streamlit as st
from logic import generate_llama_response, export_as_pdf, age_map

st.set_page_config(page_title="NurtureNest AI", page_icon="🌈", layout="wide")

def main():
    # Title
    st.markdown("<h1 style='text-align: center;'>🌈 NurtureNest AI</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Your Smart Assistant for Parents & Teachers of Kids</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Feature Info
    with st.expander("✨ What NurtureNest Can Do"):
        st.markdown("""
        ✅ Generate **activity ideas**, **quizzes**, and **teaching tips**  
        ✅ Ask **custom parenting/teaching questions**  
        ✅ Get a **7-day weekly planner**  
        ✅ **Download responses as PDF**  
        ✅ View all **past conversations**
        """)

    # Input Controls
    st.markdown("### 👤 User Preferences")
    col1, col2, col3 = st.columns(3)
    with col1:
        mode = st.radio("Who are you?", ["👩‍🏫 Teacher", "👪 Parent"])
    with col2:
        tone = st.selectbox("Response Style", ["Fun", "Creative", "Formal"])
    with col3:
        if mode == "👪 Parent":
            age_group = st.selectbox("Child Age", ["3–5", "6–8", "9–10"])
            child_age = age_map.get(age_group, "6")
        else:
            child_age = "7"

    # Feature Selection
    st.markdown("### 🎯 What Do You Want Help With?")
    action = st.selectbox(
        "Select a Feature",
        [
            "❓ Ask a Question",
            "🎯 Get Activity Idea",
            "🗒️ Generate Worksheet",
            "📝 Generate Quiz",
            "📓 Parenting / Teaching Help",
            "📅 Weekly Planner"
        ]
    )

    user_input = ""
    if action == "❓ Ask a Question":
        user_input = st.text_area("Type your question:")

    if st.button("🚀 Generate Now"):
        if action == "🎯 Get Activity Idea":
            prompt = f"Suggest a creative classroom activity for age {child_age} students" if mode == "👩‍🏫 Teacher" else f"Suggest a fun indoor non-screen activity for a {child_age} year old child"

        elif action == "🗒️ Generate Worksheet":
            prompt = f"Create a worksheet for age {child_age} students on basic subjects"

        elif action == "📝 Generate Quiz":
            prompt = f"Create a simple quiz with answers for {child_age} year olds on science or math"

        elif action == "📓 Parenting / Teaching Help":
            prompt = "Give tips for managing a classroom and keeping students engaged" if mode == "👩‍🏫 Teacher" else f"Provide parenting guidance for emotional development of a {child_age} year old child"

        elif action == "❓ Ask a Question":
            if user_input.strip():
                prompt = user_input
            else:
                st.warning("Please type your question.")
                return

        elif action == "📅 Weekly Planner":
            prompt = f"Create a fun, friendly and clear 7-day {mode.lower()} plan with {tone.lower()} tips and activities for a {child_age} year old. Format with each day as heading and bullet points."

        # Call AI
        with st.spinner("🤖 NurtureNest is thinking..."):
            result = generate_llama_response(prompt)
            st.success("✅ Response generated!")
            st.markdown("### 🧠 NurtureNest Suggests:")
            st.markdown(result)
            st.markdown(export_as_pdf(result), unsafe_allow_html=True)

            # Save in session
            if "history" not in st.session_state:
                st.session_state["history"] = []
            st.session_state["history"].append({"prompt": prompt, "response": result})

    # View History
    with st.expander("📜 View Past Interactions"):
        if "history" in st.session_state:
            for i, entry in enumerate(st.session_state["history"], 1):
                st.markdown(f"**{i}.** 🗣️ {entry['prompt']}")
                st.markdown(f"🧠 {entry['response']}")

    # Footer
    st.markdown("---")
    st.markdown("<center><sub>Made with ❤️ for kids, parents, and teachers</sub></center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
