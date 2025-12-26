import httpx
from bs4 import BeautifulSoup
from backend.app.scraper.sections import extract_sections
from backend.app.scraper.utils import extract_meta

def static_scrape(url):
    res = httpx.get(url, timeout=10)
    soup = BeautifulSoup(res.text, "lxml")

    return {
        "meta": extract_meta(soup, url),
        "sections": extract_sections(soup, url),
        "interactions": {
            "clicks": [],
            "scrolls": 0,
            "pages": [url]
        }
    }
