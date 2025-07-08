# ✨ELIA-Empowered Learning & Interaction Assistant

**ELIA** is a friendly AI-powered assistant built for **parents** and **teachers** of children aged **3–10 years**. It helps generate age-appropriate activities, quizzes, emotional development tips, and weekly planners — all through a beautiful, interactive interface!

---

## 🌱 Features

- 🏠 **Smart Mode Selection** – Clean UI with Parent & Teacher modes shown only when selected
- 🎯 **Creative Activity Ideas** – Non-screen, indoor or classroom-based activities
- 📝 **Worksheets** – Learning worksheets customized by topic and class level
- ❓ **Custom Questions** – Ask any parenting or teaching-related question
- 📓 **Parenting & Teaching Guidance** – Tips for classroom handling or behavior issues
- 🗒️ **Quizzes** – Instant educational quiz generation
- 📅 **7-Day Weekly Planner** – Personalized day-wise planner with suggestions
- 📖 **Interactive Stories** – AI-generated stories using given themes or characters
- 📄 **PDF Export** – Download any result as a well-formatted PDF
- 📜 **Interaction History** – View and reuse your past generated prompts

---

## 🖥️ Tech Stack

| Tech               | Purpose                                 |
|--------------------|------------------------------------------|
| **Python**         | Core programming language                |
| **Streamlit**      | Web interface framework                  |
| **Groq API (LLaMA 3)** | Fast, accurate AI text generation    |
| **FPDF**           | Export responses and plans to PDF        |        |
| **python-dotenv**  | Environment variable & API key handling  |
| **BlackBox.AI**     | Logging and debugging AI model behavior  |

---


## 🚀 Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/nurturenest-ai.git
cd nurturenest-ai
```
### 2. Create Virtual Environment
```bash 
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Add API Key
Create a .env file and add your Groq API key:
```bash
GROQ_API_KEY=your_actual_key_here
```
### 5. Run the App
```bash
streamlit run app.py

