import streamlit as st
from logic import generate_llama_response, export_as_pdf

st.set_page_config(page_title="NurtureNest AI", page_icon="🌈", layout="wide")


def main():
    st.markdown("<h1 style='text-align: center;'>🌈 NurtureNest AI</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Smart AI Assistant for Parents & Teachers</h4>", unsafe_allow_html=True)
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
        feature = st.sidebar.selectbox("📌 Parent Features", [
            "🎯 Get Activity Idea", "🗒️ Generate Worksheet", "📝 Generate Quiz",
            "📓 Parenting Help", "📅 Weekly Planner", "🛌 Sleep Routine Tips",
            "🍎 Nutrition Tips", "📖 Interactive Story", "🌟 Personalized Learning Plan",
            "🎁 Reward System", "❓ Ask a Custom Question"
        ])
        topic = st.sidebar.text_input("📝 Ask Tips")
        generate = st.sidebar.button("🚀 Generate Response")

    elif selected_mode == "👩‍🏫 Teacher Mode":
        tone = st.sidebar.selectbox("🗣️ Response Style", ["Fun", "Creative", "Formal"])
        class_level = st.sidebar.selectbox("🎓 Class Level", ["Nursery", "KG", "1", "2", "3", "4", "5"])
        feature = st.sidebar.selectbox("📌 Teacher Features", [
            "🎯 Get Classroom Activity", "🗒️ Generate Worksheet", "📝 Generate Quiz",
            "📓 Teaching Tip", "📅 Weekly Plan", "📋 Curriculum Help",
            "📢 Parent Communication Template", "🔁 Peer Collaboration Idea",
            "📊 Student Assessment Rubric", "🎮 Interactive Tech-based Activity", "❓ Ask a Custom Question"
        ])
        topic = st.sidebar.text_input("📝 Enter Topic / Area")
        generate = st.sidebar.button("🚀 Generate Response")

    # Past Interactions
    if selected_mode != "🌐 Home":
        if "history" in st.session_state and st.session_state["history"]:
            with st.sidebar.expander("📜 Past Interactions"):
                for i, entry in enumerate(st.session_state["history"], 1):
                    short_prompt = entry['prompt'][:60] + "..." if len(entry['prompt']) > 60 else entry['prompt']
                    st.markdown(f"- {i}. {short_prompt}")

    # --- MAIN AREA OUTPUT ---
    if selected_mode == "🌐 Home":
        st.markdown("""
            <style>
            ::-webkit-scrollbar { display: none; }
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("""
           🌈 NurtureNest AI is your creative companion designed to support both parents and teachers in nurturing and educating young minds. 
            From 🍎 nutrition tips and healthy meal ideas to help your child grow strong, 
            to 💡 teaching advice that makes classroom management easier,
            NurtureNest covers it all. It provides 🛌 
            routine guidance to establish better sleep habits and 📚
            parenting suggestions tailored to your child's specific needs and age
            . Plan the week effortlessly with 📅 creative weekly schedules, 
            and access 🎯 classroom resources categorized by subject and level.
            Whether you need to 📝 auto-generate quizzes or worksheets, build 🌿
            personalized learning paths, or explore 🎙️ interactive storytelling with
            custom characters and themes—NurtureNest delivers. It even supports you
            in monitoring growth with 📈 behavioral tracking and emotional support tools.
            Everything you need to raise, teach, and inspire—beautifully simplified in one place.
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

    # Footer
    st.markdown("---")
    st.markdown("<center><sub>Made with ❤️ for kids, parents, and teachers</sub></center>", unsafe_allow_html=True)


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
