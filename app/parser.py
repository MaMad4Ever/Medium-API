import requests
import xmltodict

from bs4 import BeautifulSoup
from fastapi import HTTPException


def parse_data(username: str):

    uri = f"https://medium.com/feed/@{username}"

    try:
        response = requests.get(uri, timeout=15)
        response.raise_for_status()

        data = xmltodict.parse(response.text)

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to fetch or parse Medium feed"
        )

    articles = []

    items = data['rss']['channel'].get('item', [])

    if isinstance(items, dict):
        items = [items]

    for k in items:

        data_dict = {}

        try:
            guid = k.get('guid', '')

            if isinstance(guid, dict):
                guid = guid.get('#text', '')

            data_dict["id"] = guid.split("/")[-1]
            data_dict["title"] = k.get('title')
            data_dict["link"] = k.get('link')
            data_dict["pub_date"] = k.get('pubDate')
            data_dict["author"] = k.get('dc:creator')

            description = k.get('description', '')

            content = k.get('content:encoded', '')

            soup = BeautifulSoup(content, 'html.parser')

            image = soup.find('img')

            data_dict["img"] = image.get('src', '') if image else ''

        except Exception:
            continue

        articles.append(data_dict)

    return articles
