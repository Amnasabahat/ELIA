import streamlit as st
from logic import generate_llama_response, export_as_pdf

st.set_page_config(layout="wide")
def main():
# --- SESSION STATE SETUP ---
    st.set_page_config(layout="wide")

    # --- SESSION STATE SETUP ---
    if "selected_mode" not in st.session_state:
        st.session_state.selected_mode = "🌐 Home"

    # --- HEADER ---
    st.markdown("""
        <div style='text-align: center; margin-top: -50px;'>
            <h1 style='font-size: 48px;'>✨ <span style="color:black;">ELIA</span></h1>
            <p style='font-size: 20px; color: gray;'>Empowered Learning & Interaction Assistant</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # --- LAYOUT: SIDEBAR-STYLE MENU + MAIN CONTENT ---
    left_col, right_col = st.columns([1, 5])

    with left_col:
        st.markdown("### ☰ Menu")
        selected = st.radio("Choose Mode", ["🌐 Home", "👪 Parent Mode", "👩‍🏫 Teacher Mode"])
        st.session_state.selected_mode = selected

    with right_col:
        mode = st.session_state.selected_mode

        if mode == "🌐 Home":
            st.markdown("""
                <div style='background-color: #e6f2ff; padding: 30px; border-radius: 15px;'>
                    <h3>🌱 Welcome to ELIA!</h3>
                    <p style='font-size: 16px;'>Empowered Learning & Interaction Assistant.</p>
                    <ul>
                        <li>📅 Weekly plans and 🎯 activities by age/class</li>
                        <li>🍎 Nutrition, 🛌 Sleep, 📚 Learning support</li>
                        <li>🎙️ AI-generated stories and quizzes</li>
                        <li>📝 Worksheets, rubrics, and personalized teaching ideas</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

        elif mode == "👪 Parent Mode":
            st.subheader("👪 Parent Mode")
            tone = st.selectbox("🗣️ Response Style", ["Fun", "Creative", "Formal"])
            class_level = st.selectbox("🎓 Class Level", ["Nursery", "KG", "1", "2", "3", "4", "5"])
            feature = st.selectbox("📌 Parent Features", [
                "🎯 Get Activity Idea", "🗒 Generate Worksheet", "📝 Generate Quiz",
                "📓 Parenting Help", "📅 Weekly Planner", "🛌 Sleep Routine Tips",
                "🍎 Nutrition Tips", "📖 Interactive Story", "🌟 Personalized Learning Plan",
                "🎁 Reward System", "❓ Ask a Custom Question"
            ])
            topic = st.text_input("📝 Ask Tips")
            if st.button("🚀 Generate Response"):
                prompt = get_prompt("parent", feature, tone, topic, class_level)
                show_response(prompt)

        elif mode == "👩‍🏫 Teacher Mode":
            st.subheader("👩‍🏫 Teacher Mode")
            tone = st.selectbox("🗣️ Response Style", ["Fun", "Creative", "Formal"])
            class_level = st.selectbox("🎓 Class Level", ["Nursery", "KG", "1", "2", "3", "4", "5"])
            feature = st.selectbox("📌 Teacher Features", [
                "🎯 Get Classroom Activity", "🗒 Generate Worksheet", "📝 Generate Quiz",
                "📓 Teaching Tip", "📅 Weekly Plan", "📋 Curriculum Help",
                "📢 Parent Communication Template", "🔁 Peer Collaboration Idea",
                "📊 Student Assessment Rubric", "🎮 Interactive Tech-based Activity", "❓ Ask a Custom Question"
            ])
            topic = st.text_input("📝 Enter Topic / Area")
            if st.button("🚀 Generate Response"):
                prompt = get_prompt("teacher", feature, tone, topic, class_level)
                show_response(prompt)

    # --- FOOTER ---
    st.markdown("---")
    st.markdown("<center><sub>🌼 Made with ❤️ for kids, parents, and teachers • © 2025 ELIA</sub></center>", unsafe_allow_html=True)






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
            "🧠 Learning Recommendation": f"Some prompt with {topic}, {age}, {class_level}",
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
