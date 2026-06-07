from groq import Groq

# ── CONFIG ────────────────────────────────────────────────────────────────────
API_KEY  = "YOUR_GROQ_API_KEY_HERE"    # 🔑 Paste your gsk_... key here
BOT_NAME = "Astra"
SYSTEM_PROMPT = """You are Astra, a helpful and friendly AI assistant.
You answer clearly, concisely, and in a conversational tone.
If you don't know something, admit it honestly."""
# ──────────────────────────────────────────────────────────────────────────────

client = Groq(api_key=API_KEY)

def print_banner():
    print("\n" + "═" * 50)
    print(f"   🤖  {BOT_NAME} — AI Chatbot powered by Groq")
    print("   Type 'exit' or 'quit' to end the session.")
    print("═" * 50 + "\n")

def chat():
    print_banner()
    history = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "bye"]:
            print(f"\n{BOT_NAME}: Goodbye! Have a great day! 👋\n")
            break

        history.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=history,
            )
            bot_reply = response.choices[0].message.content
            history.append({"role": "assistant", "content": bot_reply})
            print(f"\n{BOT_NAME}: {bot_reply}\n")

        except Exception as e:
            print(f"\n⚠️  Error: {e}\n")
            history.pop()

if __name__ == "__main__":
    chat()
