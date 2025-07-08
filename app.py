import streamlit as st
from logic import generate_llama_response, export_as_pdf

st.set_page_config(page_title="NurtureNest AI", page_icon="✨", layout="wide")


def main():
    # --- PAGE CONFIG ---
    st.set_page_config(page_title="NurtureNest AI", page_icon="✨", layout="wide")

    # --- CUSTOM CSS ---
    st.markdown("""
    <style>
        body { background-color: #f9fcff; }
        .block-container { padding-top: 1rem; padding-bottom: 2rem; }
        .stButton button {
            background-color: #6dc2ff;
            color: white;
            border-radius: 10px;
            font-size: 16px;
        }
        .stSelectbox, .stTextInput, .stRadio {
            border-radius: 10px !important;
        }
        .stSidebar { background-color: #f0f4ff; }
    </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    st.markdown("""
    <div style='text-align: center; margin-top: -50px;'>
        <h1 style='font-size: 48px;'>✨ <span style="color:#3e64ff;">NurtureNest AI</span></h1>
        <p style='font-size: 20px; color: gray;'>Smart AI Assistant for Parents & Teachers</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # --- SIDEBAR NAVIGATION ---
    st.sidebar.title("🧭 Navigation")
    selected_mode = st.sidebar.radio("🔹 Select Mode", ["🌐 Home", "👪 Parent Mode", "👩‍🏫 Teacher Mode"])

    tone = None
    class_level = None
    feature = None
    topic = ""
    generate = False

    if selected_mode == "👪 Parent Mode":
        tone = st.sidebar.selectbox("🗣️ Response Style", ["Fun", "Creative", "Formal"])
        class_level = st.sidebar.selectbox("🎓 Class Level", ["Nursery", "KG", "1", "2", "3", "4", "5"])
        feature = st.sidebar.selectbox("📌 Parent Features", [...])  # same as before
        topic = st.sidebar.text_input("📝 Ask Tips")
        generate = st.sidebar.button("🚀 Generate Response")

    elif selected_mode == "👩‍🏫 Teacher Mode":
        tone = st.sidebar.selectbox("🗣️ Response Style", ["Fun", "Creative", "Formal"])
        class_level = st.sidebar.selectbox("🎓 Class Level", ["Nursery", "KG", "1", "2", "3", "4", "5"])
        feature = st.sidebar.selectbox("📌 Teacher Features", [...])  # same as before
        topic = st.sidebar.text_input("📝 Enter Topic / Area")
        generate = st.sidebar.button("🚀 Generate Response")

    # --- Past Interactions ---
    if selected_mode != "🌐 Home":
        if "history" in st.session_state and st.session_state["history"]:
            with st.sidebar.expander("📜 Past Interactions"):
                for i, entry in enumerate(st.session_state["history"], 1):
                    short_prompt = entry['prompt'][:60] + "..." if len(entry['prompt']) > 60 else entry['prompt']
                    st.markdown(f"- {i}. {short_prompt}")

    # --- HOME MODE ---
    if selected_mode == "🌐 Home":
        st.markdown("""
        <div style='background-color: #e6f2ff; padding: 30px; border-radius: 15px;'>
            <h3>✨ Welcome to NurtureNest!</h3>
            <p style='font-size: 16px;'>Your creative AI companion for parenting and teaching.</p>
            <ul>
                <li>📅 Weekly plans and 🎯 activities by age/class</li>
                <li>🍎 Nutrition, 🛌 Sleep, 📚 Learning support</li>
                <li>🎙️ AI-generated stories and quizzes</li>
                <li>📝 Worksheets, rubrics, and personalized teaching ideas</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif generate and feature:
        prompt = get_prompt(
            mode="parent" if selected_mode == "👪 Parent Mode" else "teacher",
            feature=feature,
            tone=tone,
            topic=topic,
            class_level=class_level
        )
        show_response(prompt)

    # --- FOOTER ---
    st.markdown("---")
    st.markdown("<center><sub>🌼 Made with ❤️ for kids, parents, and teachers • © 2025 NurtureNest AI</sub></center>", unsafe_allow_html=True)

    


# --- PROMPT GENERATOR ---
def get_prompt(mode, feature, age=None, tone="Creative", topic="", class_level=""):
    if mode == "parent":
        return {
            "🎯 Get Activity Idea": f"Suggest a {tone.lower()} indoor activity for a child in class {class_level} related to {topic}.",
            "🗒️ Generate Worksheet": f"Create a worksheet for a child in class {class_level} on the topic '{topic}'.",
            "📝 Generate Quiz": f"Generate a simple quiz for class {class_level} on '{topic}'.",
            "📓 Parenting Help": f"Give parenting advice related to '{topic}' for a child in class {class_level}.",
            "📅 Weekly Planner": f"Create a 7-day weekly plan with {tone.lower()} activities for a child in class {class_level}.",
            "🛌 Sleep Routine Tips": f"Suggest a sleep routine for a child in class {class_level} who struggles with sleep.",
            "🍎 Nutrition Tips": f"Share healthy meal ideas and nutrition tips for a child in class {class_level}.",
            "📖 Interactive Story": f"Create a fun story including {topic} for a child in class {class_level}.",
            "🌟 Personalized Learning Plan": f"Build a custom learning plan for a child in class {class_level} interested in {topic}.",
            "🎁 Reward System": f"Design a reward system to encourage positive behavior in a child from class {class_level}.",
            "❓ Ask a Custom Question": topic
        }[feature]

    elif mode == "teacher":
        return {
            "🎯 Get Classroom Activity": f"Suggest a {tone.lower()} classroom activity for class {class_level} students related to '{topic}'.",
            "🗒️ Generate Worksheet": f"Create a worksheet for class {class_level} on '{topic}'.",
            "📝 Generate Quiz": f"Generate a quiz for class {class_level} students on the topic '{topic}'.",
            "📓 Teaching Tip": f"Give a teaching tip for managing class {class_level} students regarding '{topic}'.",
            "📅 Weekly Plan": f"Create a weekly classroom teaching plan for class {class_level} with {tone.lower()} style tips and activities.",
            "📋 Curriculum Help": f"Design a curriculum outline for class {class_level} focused on '{topic}'.",
            "📢 Parent Communication Template": f"Write a message template to update parents about their child’s progress in class {class_level}.",
            "🔁 Peer Collaboration Idea": f"Suggest a way for teachers to collaborate on a lesson about '{topic}' for class {class_level}.",
            "📊 Student Assessment Rubric": f"Create an assessment rubric for class {class_level} students learning '{topic}'.",
            "🎮 Interactive Tech-based Activity": f"Suggest a tech-based hands-on activity for class {class_level} about '{topic}'.",
            "❓ Ask a Custom Question": topic
        }[feature]


# --- SHOW RESPONSE ---
def show_response(prompt):
    with st.spinner("🤖 NurtureNest is thinking..."):
        result = generate_llama_response(prompt)
        st.success("✅ Response generated!")
        st.markdown("### 🧠 NurtureNest Suggests:")
        st.markdown(result)

        # Save response
        st.session_state["last_response"] = result

        # PDF Download
        with st.container():
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown(export_as_pdf(result), unsafe_allow_html=True)

        # Save to history
        if "history" not in st.session_state:
            st.session_state["history"] = []
        st.session_state["history"].append({"prompt": prompt})


if __name__ == "__main__":
    main()
