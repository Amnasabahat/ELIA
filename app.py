import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Create client
client = Groq(api_key=groq_api_key)

# Streamlit setup
st.set_page_config(page_title="NurtureNest", page_icon="🌈", layout="wide")

def generate_llama_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300,
            top_p=1.0,
            stream=False,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

def main():
    st.title("🌈 NurtureNest AI")
    st.subheader("AI Assistant for Parents & Teachers of Kids Aged 3–10")

    # Sidebar: all options
    st.sidebar.header("🧠 NurtureNest Controls")

    mode = st.sidebar.radio("Who are you?", ["👩‍🏫 Teacher", "👪 Parent"])

    st.sidebar.markdown("---")

    # Age group for personalization
    age_group = None
    if mode == "👪 Parent":
        age_group = st.sidebar.selectbox("Select Child Age", ["3–5", "6–8", "9–10"])

    st.sidebar.markdown("### 🔧 Choose an Action")

    action = st.sidebar.selectbox(
        "Choose Feature",
        [
            "🎯 Get Activity Idea",
            "❓ Ask a Question",
            "📝 Generate Worksheet/Quiz",
            "📖 Parenting / Teaching Help"
        ]
    )

    user_input = ""
    if action == "❓ Ask a Question":
        user_input = st.sidebar.text_area("Your Question")

    if st.sidebar.button("✨ Submit"):
        # Build prompt dynamically
        if action == "🎯 Get Activity Idea":
            if mode == "👩‍🏫 Teacher":
                prompt = "Suggest a creative classroom activity for early learners"
            else:
                prompt = f"Suggest a fun indoor non-screen activity for a child aged {age_group}"
        
        elif action == "📝 Generate Worksheet/Quiz":
            if mode == "👩‍🏫 Teacher":
                prompt = "Create a quiz or worksheet for teaching basic science to 7-year-olds"
            else:
                prompt = f"Create a home learning worksheet for a child aged {age_group}"
        
        elif action == "📖 Parenting / Teaching Help":
            if mode == "👩‍🏫 Teacher":
                prompt = "Give tips for managing a classroom and keeping students engaged"
            else:
                prompt = f"Provide parenting guidance for emotional development of a {age_group} child"
        
        elif action == "❓ Ask a Question":
            if user_input.strip():
                prompt = user_input
            else:
                st.warning("Please type your question.")
                return

        with st.spinner("Talking to NurtureNest AI..."):
            result = generate_llama_response(prompt)
            st.markdown("### 🧠 NurtureNest Suggests:")
            st.success(result)

   

if __name__ == "__main__":
    main()
