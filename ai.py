from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze(bond):
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""
Проаналізуй ОВДП:
Назва: {bond['name']}
Строк: {bond['maturity']}

Дай короткий висновок і ризик (low/medium/high).
"""
            }]
        )

        return resp.choices[0].message.content

    except Exception as e:
        return "AI недоступний"
