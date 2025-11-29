from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def instant():
    return "Live from production! :) second try"

# Export the app for Vercel
#__all__ = ["app"]


