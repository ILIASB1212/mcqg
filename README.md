# MCQ Generator with GPT-3.5

This project generates multiple-choice questions (MCQs) based on given text using GPT-3.5, LangChain, and Streamlit.

## Setup Instructions

1. Clone the repository: `git clone <repo_url>`
2. Install dependencies: `pip install -r requirements.txt`

3. Create a `.env` file and set your OpenAI API Key:

4. Run the app: `streamlit run streamlitapp.py`
5. Upload a PDF/TXT file, specify the number of questions, subject, and tone, and click "Create MCQ" to generate the quiz.
6. change the gpt_model to 4 or 4.o
## Features:
- Upload PDF/TXT files
- Generate MCQs based on the content
- Review the generated MCQs and adjust their complexity

## Requirements:
- Python 3.8+
- OpenAI API Key
- LangChain
- Streamlit
- PyPDF2
