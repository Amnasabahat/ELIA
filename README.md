# 🌈 NurtureNest AI

**NurtureNest** is a friendly AI-powered assistant built for **parents** and **teachers** of children aged **3–10 years**. It helps generate age-appropriate activities, quizzes, emotional development tips, and weekly planners — all through a beautiful, interactive interface!

---

## ✨ Features

- 🎯 **Creative Activity Ideas** – Non-screen, indoor or classroom-based
- 📝 **Worksheets** – Learning worksheets based on child's age
- ❓ **Custom Questions** – Ask any parenting or teaching-related question
- 📓 **Parenting & Teaching Guidance** – Tips for handling classroom or child behavior
- 🗒️ **Quizzes** – Age-appropriate educational quizzes
- 📅 **7-Day Weekly Planner** – Personalized planner with day-wise activities and tips
- 📄 **PDF Export** – Download responses or planners as PDF
- 📜 **Interaction History** – Review past queries and results

---

## 🖥️ Tech Stack

| Tech        | Purpose                          |
|-------------|----------------------------------|
| **Python**  | Programming Language             |
| **Streamlit** | Web UI for the app             |
| **Groq API (LLaMA 3)** | AI-generated responses |
| **FPDF**    | PDF generation                   |
| **dotenv**  | Secure API key management        |


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

