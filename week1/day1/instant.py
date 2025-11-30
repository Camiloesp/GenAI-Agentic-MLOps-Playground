from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def instant():
    client = OpenAI()
    message= """
    You are on a website that has just been deployed to production for the first time!
    Please reply  with an enthusiastic message to welcome the user to the website, explaining that it is live on production for the first time!
    """

    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br>")
    html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"

    return html

# Export the app for Vercel
#__all__ = ["app"]

# Change folder in terminal: cd .\week1\day1\
