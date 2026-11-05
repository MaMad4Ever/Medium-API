from fastapi import FastAPI, HTTPException

from app.schemas import Medium
from app.parser import parse_data


app = FastAPI()


@app.post("/")
def get_data(medium: Medium):
    return parse_data(medium.username)


@app.get("/medium/{username}/article/{article_id}")
def get_article(username: str, article_id: str):

    articles = parse_data(username)

    for article in articles:
        if article["id"] == article_id:
            return article

    raise HTTPException(
        status_code=404,
        detail="Article not found"
    )


@app.get("/health")
def get_health():
    return {"ping": "Its working fast 🚅"}
