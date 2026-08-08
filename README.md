# 🤖 Govind's AI Portfolio

> An interactive AI-powered portfolio that lets recruiters and visitors explore my skills, projects, experience, and background through a conversational AI assistant.

🌐 **Live Portfolio:** https://ai-portfolio-smoky-alpha.vercel.app

---

## 📌 Overview

Traditional portfolios are static. This project turns my portfolio into an interactive AI assistant.

Instead of simply reading through a resume or portfolio, a recruiter can ask questions such as:

- "Tell me about Govind's projects."
- "What are his technical skills?"
- "Which AI projects has he worked on?"
- "Tell me about his experience."
- "Is he suitable for this job?"

The AI assistant uses my portfolio information as its knowledge source and responds conversationally while being instructed not to invent information.

---

## ✨ Features

### 🤖 AI Portfolio Assistant

A conversational AI assistant that can answer questions about:

- Skills
- Projects
- Experience
- Achievements
- Technical background

### 🧠 Conversation Memory

The assistant maintains conversation history so that follow-up questions can understand the previous conversation.

Example:

```text
User:
Tell me about Govind's projects.

AI:
Govind has worked on several projects including ...

User:
Which one involved Generative AI?

AI:
The project involving Generative AI was ...
```

### 📄 Job Description Matching

A recruiter can upload a job description in supported document formats.

The backend extracts the text and uses the LLM to evaluate how well the candidate profile matches the requirements.

Supported formats:

- PDF
- DOCX

### 🔐 Controlled AI Responses

The system prompt instructs the LLM to:

- Use the provided portfolio information.
- Answer honestly.
- Avoid fabricating skills or experience.
- Avoid exaggerating achievements.
- Clearly communicate when information is unavailable.

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │        USER          │
                    │     / Recruiter      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       FRONTEND       │
                    │                      │
                    │    HTML + CSS + JS   │
                    │        Vercel        │
                    └──────────┬───────────┘
                               │
                         HTTP Requests
                               │
                               ▼
                    ┌──────────────────────┐
                    │       BACKEND        │
                    │       FastAPI        │
                    │        Render        │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
          Portfolio         Memory        File Parser
             Data           History        PDF / DOCX
                │              │              │
                └──────────────┼──────────────┘
                               │
                               ▼
                         ┌───────────┐
                         │   GROQ    │
                         │    LLM    │
                         └─────┬─────┘
                               │
                               ▼
                         AI Response
```

---

# 🛠️ Tech Stack

## Frontend

- HTML
- CSS
- JavaScript

The frontend is built without React or any other frontend framework.

## Backend

- Python
- FastAPI
- Uvicorn

## AI

- Groq API
- LLM
- System Prompts
- Prompt Engineering
- JSON Responses

## Data & Validation

- Pydantic
- PDF Parsing
- DOCX Parsing

## Deployment

- Vercel — Frontend
- Render — Backend

---

# 📂 Project Structure

```text
AI-Portfolio/
│
├── backend/
│   │
│   ├── data/
│   │   └── portfolio.txt
│   │
│   ├── app.py
│   ├── config.py
│   ├── llm.py
│   ├── memory.py
│   ├── models.py
│   ├── parser.py
│   └── prompts.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
├── README.md
└── requirements.txt
```

> `.env` is intentionally excluded from the repository because it contains the Groq API key.

---

# 🔍 Backend Components

### `app.py`

Main FastAPI application.

Responsibilities:

- Receive user messages
- Handle portfolio conversations
- Handle job description matching
- Connect the backend components

### `llm.py`

Contains the LLM interaction logic.

It handles communication with the Groq API and sends the required prompts to the language model.

### `prompts.py`

Contains the system instructions used to control the AI assistant.

The prompt defines:

- The role of the assistant
- What information it can use
- How it should answer
- What it should avoid
- How it should behave when information is unavailable

### `memory.py`

Handles conversation history.

Previous messages are stored so the LLM can understand follow-up questions and maintain conversational context.

### `parser.py`

Handles document text extraction for uploaded PDF and DOCX files.

### `models.py`

Contains Pydantic models used to validate structured API requests and responses.

### `config.py`

Handles application configuration and environment variables such as the API key.

Sensitive values are kept outside the source code using environment variables.

---

# 💬 Example Conversation

```text
User:
Tell me about Govind's AI projects.

AI:
Govind has worked on multiple AI-focused projects,
including projects involving LLMs, AI automation,
and computer vision.

User:
Which project involved computer vision?

AI:
IRIS is a computer vision project focused on
thermal imagery and AI-based object detection.
```

The assistant is instructed to use the available portfolio information rather than inventing details.

---

# 📄 Job Fit Analysis

The portfolio includes a job description matching workflow.

```text
Job Description
       │
       ▼
Document Upload
       │
       ▼
Text Extraction
       │
       ▼
LLM Analysis
       │
       ▼
Candidate Profile Comparison
       │
       ▼
Job Fit Response
```

Supported document formats:

```text
PDF
DOCX
```

---

# 🔄 Chat Workflow

For a normal portfolio question:

```text
User Question
      │
      ▼
Frontend JavaScript
      │
      ▼
FastAPI /chat
      │
      ▼
Conversation Memory
      │
      ▼
System Prompt + Portfolio Information
      │
      ▼
Groq LLM
      │
      ▼
AI Response
      │
      ▼
Frontend
```

---

# 🚀 Running Locally

## 1. Clone the repository

Clone this repository from GitHub and open the project directory:

```bash
git clone YOUR_REPOSITORY_URL
cd AI-Portfolio
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create `.env`

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file to GitHub.

## 5. Start the backend

Move into the backend directory:

```bash
cd backend
```

Run:

```bash
uvicorn app:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

## 6. Start the frontend

Open another terminal and move into the frontend directory:

```bash
cd frontend
```

Run a simple local server:

```bash
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500
```

---

# 🌐 Deployment

The application is deployed using two services.

### Frontend — Vercel

The static HTML, CSS and JavaScript frontend is deployed on Vercel.

🌐 **Live Portfolio:**

https://ai-portfolio-smoky-alpha.vercel.app

### Backend — Render

The FastAPI backend is deployed on Render.

The backend handles API requests from the frontend and communicates with the Groq API.

🔗 **Backend:**

https://ai-portfolio-oly8.onrender.com

FastAPI documentation:

https://ai-portfolio-oly8.onrender.com/docs

---

# 🔐 Environment Variables

The application requires:

```env
GROQ_API_KEY=your_groq_api_key
```

The API key is stored as an environment variable instead of being written directly into the source code.

For deployment, the environment variable is configured in the backend hosting platform.

---

# 📚 Concepts Used

This project brings together concepts learned while studying LLM application development:

- LLM API Calls
- System Roles
- Prompt Engineering
- Temperature
- Tokens
- JSON
- Pydantic
- Conversation Memory
- Prompt Chaining
- ReAct Concepts
- API Integration
- FastAPI
- Document Parsing
- Frontend-Backend Communication
- Deployment

The main goal of the project is to combine these concepts into one practical full-stack AI application.

---

# 🎯 Why I Built This

A resume gives recruiters information to read.

An AI portfolio gives them a way to **interact with that information**.

This project explores how a personal portfolio can become a conversational interface where recruiters can directly ask questions about a candidate's background, projects, and technical skills.

It also provided practical experience connecting:

```text
LLM
 ↓
Backend
 ↓
API
 ↓
Frontend
 ↓
Deployment
```

into one complete application.

---

# 🔮 Future Improvements

Possible improvements for future versions include:

- More advanced portfolio knowledge retrieval
- Persistent conversation storage
- More detailed job matching
- Authentication
- Additional document formats
- Improved UI interactions

---

# 👨‍💻 Author

## Govind Khandelwal

**B.Tech — Mathematics & Computing**  
**Delhi Technological University**

### Interests

- Artificial Intelligence
- Generative AI
- Agentic AI
- Web Development
- Data Structures & Algorithms
- AI-powered Applications

---

# ⭐ Live Demo

👉 **Try Govind's AI Portfolio:**

https://ai-portfolio-smoky-alpha.vercel.app
