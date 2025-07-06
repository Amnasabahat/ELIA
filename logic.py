# logic.py

import os
from dotenv import load_dotenv
from groq import Groq
from fpdf import FPDF
import base64

# Load API Key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Age group mapping
age_map = {"3–5": "4", "6–8": "7", "9–10": "9"}

# Generate PDF
def export_as_pdf(text, filename="nurturenest_output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)

    with open(filename, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        return f'<a href="data:application/pdf;base64,{base64_pdf}" download="{filename}">📄 Download PDF</a>'

# Generate response from Groq
def generate_llama_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500,
            top_p=1.0,
            stream=False,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"
