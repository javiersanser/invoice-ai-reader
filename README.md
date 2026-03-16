# 📑 Invoice AI Reader

![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-orange)

⚠️ Note: This project is currently under active development as part of the Harvard CS50P course final project. Some features may be incomplete or subject to change.

**Invoice AI Reader** is an AI-powered document processing tool designed to automate data extraction from invoices using the **Google Gemini API**. It features a web interface for validation and a local database for persistence.

## 🚀 Features
* **Automated Extraction:** Uses Gemini 1.5 Flash to read PDFs and images.
* **Human-in-the-Loop:** Streamlit dashboard to verify and edit extracted data.
* **Local Storage:** Saves structured data into a SQLite database.
* **Modern Tooling:** Managed with `uv` for lightning-fast dependency management.

## 🤖 Tech Stack
* **Language:** Python 3.12+
* **AI Model:** Google Gemini (Generative AI)
* **Frontend:** Streamlit
* **Database:** SQLite
* **Environment:** `uv`

## 📂 Project Structure Plan
```
invoice-ai-reader/
├── data/               # Input folder for invoice PDFs/Images
├── database/           # SQLite database storage
├── src/                # Source code
│   ├── app.py          # Streamlit web dashboard
│   ├── extractor.py    # Gemini API integration & logic
│   └── database.py     # SQL database management & schemas
├── .env                # API Keys and secrets (Local only)
├── .gitignore          # Git ignore rules
├── pyproject.toml      # Project dependencies and metadata (uv)
└── README.md           # Project documentation
```

## 🛠️ Roadmap / To-Do
- [x] Initial project structure and Git setup.
- [ ] Database schema design (SQLite).
- [ ] Gemini API integration for PDF/Image parsing.
- [ ] Streamlit dashboard development.
- [ ] Data validation logic.
- [ ] Final project submission and video demo.

## 📦 Installation & Setup
* TODO once finished the first version.