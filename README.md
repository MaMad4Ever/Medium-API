# 📰 Medium API

**FastAPI** service that fetches a Medium user's articles from their public RSS feed and returns them as JSON. It supports listing all articles for a username or retrieving a single article by its ID.

---

## ✨ Features

- 📥 Fetch the list of articles for any Medium user
- 🔍 Retrieve a specific article by its `id`
- ⚡ Built with FastAPI (fast + auto-generated Swagger docs)
- ❤️ Health-check endpoint (`/health`) to verify the server is running

---

## 🚀 Installation & Running
1. Clone the repository
```
git clone <repository-url>
cd Medium-API
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the server
```
uvicorn app.main:app --reload
```
The server starts on http://127.0.0.1:8000 by default.

- Interactive docs (Swagger UI): http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🔌 Endpoints
### 1. Get a user's articles
```
POST /

Request body:

{
"username": "username"
}

Example response:

[
{
"id": "abc123def456",
"title": "Article title",
"link": "",
"pub_date": "Mon, 01 Jan 2024 12:00:00 GMT",
"author": "Author name",
"img": ""
}
]
```

### 2. Get a specific article
```
GET /medium/{username}/article/{article_id}

Request:

GET /medium/username/article/abc123def456

If the article is found, the article object is returned; otherwise:

{
"detail": "Article not found"
}
```
### 3. Health check
```
Request:

GET /health

Response:

{
"ping": "Its working fast 🚅"
}
```
