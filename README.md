# AI Interview Question Generator

## Overview

AI Interview Question Generator is a web application that generates technical interview questions based on the user's selected topic, difficulty level, and number of questions. The application uses Google's Gemini AI model to generate customized interview questions through an interactive Gradio interface.

---

## Features

- Generate technical interview questions for any topic.
- Select difficulty level (Easy, Medium, Hard).
- Choose the number of questions to generate.
- Interactive web interface using Gradio.
- FastAPI backend for handling API requests.
- Input validation using Pydantic.
- Secure API key management using Python Dotenv.

---

## Technologies Used

- Python
- FastAPI
- Gradio
- Google Gemini API (Gemini 2.5 Flash)
- Pydantic
- Python Dotenv
- Requests

---

## Project Structure

```text
AI-Interview-Question-Generator/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env (Not uploaded to GitHub)
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Interview-Question-Generator.git
cd AI-Interview-Question-Generator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project folder and add your Gemini API key.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

---

## Running the Project

### Start the FastAPI Backend

```bash
python -m uvicorn main:app --reload
```

### Start the Gradio Frontend

Open another terminal and run:

```bash
python app.py
```

Then open the Gradio URL shown in the terminal (usually `http://127.0.0.1:7860`) in your browser.

---

## How It Works

1. The user enters an interview topic.
2. The user selects the difficulty level.
3. The user chooses the number of questions.
4. The Gradio frontend sends the request to the FastAPI backend.
5. The backend sends the prompt to the Gemini API.
6. Gemini generates technical interview questions.
7. The generated questions are displayed in the Gradio interface.

---

## Future Enhancements

- Generate interview answers.
- Export interview questions as PDF.
- AI-powered mock interview mode.
- Save interview history.
- Support additional AI models.

---

## Author

Developed as an AI/NLP learning project using FastAPI, Gradio, and Google Gemini AI.