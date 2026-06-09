from telegram import Bot
from config import BOT_TOKEN, CHAT_ID
from collectors import fetch_bonds
from ai import analyze
from db import load, save

bot = Bot(token=BOT_TOKEN)


def run():
    old = load()
    old_ids = {x["id"] for x in old}

    new = fetch_bonds()

    for b in new:
        if b["id"] not in old_ids:

            text = f"""
🆕 НОВА ОВДП

📌 {b['name']}
📆 {b['maturity']}

🤖 AI:
{analyze(b)}
"""

            bot.send_message(chat_id=CHAT_ID, text=text)

            old.append(b)

    save(old)


if __name__ == "__main__":
    run()
