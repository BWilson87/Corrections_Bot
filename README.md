## 📜 Corrections Bot

A secure local chatbot for **New Zealand Corrections legislation** — built with **LangChain**, **Ollama**, and **Chroma**.

This bot demonstrates how to run a **retrieval-augmented generation (RAG)** pipeline entirely offline, so sensitive info never leaves your machine. It’s ideal for staff to query up-to-date Acts and Regulations without sending any data to the cloud.

---

## ⚡ Key Features

✅ **Local LLM** — uses Ollama to run Mistral on your computer, no API keys needed.  
✅ **Vector Store** — Chroma indexes your legislation text for fast, relevant answers.  
✅ **Custom Document Loader** — handles messy text files safely.  
✅ **Private by design** — all embeddings & answers stay on your hardware.

---

## 🗂️ Tech Stack

- Python  
- LangChain  
- Ollama (Mistral model)  
- Chroma

---

## 🚀 How to Run

### 1️⃣ Clone this repo

```
git clone https://github.com/YOURUSERNAME/corrections_bot.git
cd corrections_bot
```

### 2️⃣ Set up your environment
# Create a virtual environment if needed
python -m venv .venv

# Activate it
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Mac/Linux

# Install requirements
pip install -r requirements.txt

### 3️⃣ Start Ollama

In a separate terminal, run:

ollama serve

Make sure the Mistral model is pulled:

ollama pull mistral

### 4️⃣ Put your legislation .txt files in the data/ folder

data/
  Corrections Act 2004.txt
  Corrections Regulations 2005.txt
  Crimes Act 1961.txt

  ✅ Use cleaned UTF-8 files for best results!


### 5️⃣ Run the bot

python corrections_bot.py

Ask questions like:
Who can grant temporary release under the Corrections Act?

### 🔒 Why This Matters
This bot solves a real workplace problem: staff can look up rules & forms securely without sending confidential data or case details to cloud chatbots.
