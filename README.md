# Sparks AI Chatbot

A simple AI chatbot application built with **FastAPI**, **HTMX**, **Jinja2**, and **Google Gemini AI**.

-------------------------------------------
## 🌐 Live Demo

👉 https://chatbot-xxxx.onrender.com

--------------------------------------------
## Features

- AI-powered chat replies using Gemini API
- FastAPI backend
- Jinja2 template rendering
- HTMX-based form submission without page reload
- Simple clean chat UI
- Press Enter to send message
- Shift + Enter for new line
- Messages clear on page refresh
  

## Tech Stack

- Python
- FastAPI
- Google Gemini API
- HTMX
- Jinja2
- HTML
- CSS

## Project Structure

```text
Ai chatbot/
│
├── main.py
├── models.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── chat-messages.html
│
└── static/
    └── styles.css

-----------------------------------------
Setup Instructions
-----------------------------------------
1. Clone the repository
git clone https://github.com/muhammedfahimk/ChatBot.git
cd ChatBot

2. Create virtual environment
python -m venv .venv

3. Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

4. Install dependencies
pip install -r requirements.txt

5. Create .env file
GEMINI_API_KEY=your_gemini_api_key_here


🔑 How to Get Gemini API Key
Go to https://aistudio.google.com
Sign in with your Google account
Click Get API Key
Click Create API Key
Copy the key
Paste it into your .env file


▶️ Run the Application
uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000
