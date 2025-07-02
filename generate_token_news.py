
import openai
import json
from datetime import datetime
import requests
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

TOKEN_TOPICS = {
    "irz": "Iran Israel",
    "nvbs": "NATO BRICS",
    "ukr": "Ukraine Russia",
    "cnx": "China Xi Jinping",
    "kju": "North Korea Kim Jong Un",
    "twc": "Taiwan China conflict",
    "pal": "Palestine Israel Gaza"
}

def get_recent_headlines(topic):
    url = f"https://news.google.com/rss/search?q={topic}&hl=en&gl=US&ceid=US:en"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return [f"Headline {i+1} about {topic}" for i in range(2)]
    except:
        return []
    return []

def summarize_with_gpt4(headlines):
    prompt = f"Summarize the following headlines into a short geopolitical news update (max 70 words):\n" + "\n".join(headlines)
    completion = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )
    return completion.choices[0].message.content.strip()

def generate_all_token_news():
    today = datetime.now().strftime("%Y-%m-%d")

    for token, topic in TOKEN_TOPICS.items():
        headlines = get_recent_headlines(topic)
        if not headlines:
            continue
        summary = summarize_with_gpt4(headlines)

        filename = f"news_{token}.json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = {"updates": []}

        data["updates"].insert(0, {"date": today, "text": summary})
        data["updates"] = data["updates"][:10]

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✔️ Mise à jour générée pour {token.upper()}")
