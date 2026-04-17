from openai import OpenAI
import requests
import datetime
import random
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

now = datetime.datetime.now()
date_str = f"{now.month}月{now.day}日"

topics = ["歴史", "科学", "食べ物", "文化", "雑学"]
topic = random.choice(topics)

prompt = f"""
{date_str}に関係する{topic}の面白い雑学を1つ作ってください。
・140文字以内
・「実は」から始める
・最後は疑問形
"""

response = client.responses.create(
    model="gpt-5.3",
    input=prompt
)

tweet_text = response.output[0].content[0].text
tweet_text += "\n#今日は何の日 #雑学"

url = "https://api.twitter.com/2/tweets"
headers = {
    "Authorization": f"Bearer {os.environ['X_BEARER_TOKEN']}",
    "Content-Type": "application/json"
}

requests.post(url, headers=headers, json={"text": tweet_text})
