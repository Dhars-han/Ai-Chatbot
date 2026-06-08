# 🤖 Gopal — AI Chatbot powered by Groq

A conversational AI chatbot built with Python and Groq API.  
Supports multi-turn conversations with full context memory across the session.  
Powered by **Llama 3.3 70B** — one of the most capable open-source LLMs available.

---

## ✨ Features

- 🧠 **Multi-turn memory** — remembers everything said in the session
- ⚡ **Llama 3.3 70B** — Meta's powerful open-source model via Groq
- 🚀 **Ultra-fast responses** — Groq's LPU hardware delivers blazing speed
- 🎯 **Custom system prompt** — personality and behaviour fully configurable
- 🛡️ **Error handling** — gracefully recovers from API errors
- 💻 **Terminal-based** — lightweight, no UI dependencies

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Dhars-han/ai-chatbot.git
cd ai-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API Key
- Get a free key at → [console.groq.com](https://console.groq.com) (no credit card needed!)
- Open `chatbot.py` and replace `YOUR_GROQ_API_KEY_HERE` with your key

### 4. Run the chatbot
```bash
python chatbot.py
```

---

## 💬 Example Conversation

```
══════════════════════════════════════════════════
   🤖  Gopal — AI Chatbot powered by Groq
   Type 'exit' or 'quit' to end the session.
══════════════════════════════════════════════════

You: Hello! Who are you?

Astra: Hi there! I'm Gopal, your friendly AI assistant powered by Groq
       and Llama 3.3 70B. I'm here to help you with anything you need!

You: What can you do?

Astra: I can answer questions, help you brainstorm ideas, explain complex
       topics, write or debug code, and much more. What would you like
       to explore today?

You: exit

Astra: Goodbye! Have a great day! 👋
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Groq API | Ultra-fast LLM inference |
| Llama 3.3 70B | Open-source language model by Meta |
| groq SDK | Official Python client |

---

## 📁 Project Structure

```
ai-chatbot/
├── chatbot.py          # Main chatbot script
├── requirements.txt    # Python dependencies
├── .env.example        # API key template
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## 👤 Author

**Dharshan M**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-dharshanmmm-blue)](https://www.linkedin.com/in/dharshanmmm/)
[![GitHub](https://img.shields.io/badge/GitHub-Dhars--han-black)](https://github.com/Dhars-han)
