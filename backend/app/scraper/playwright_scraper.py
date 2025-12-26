from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from backend.app.scraper.sections import extract_sections
from backend.app.scraper.utils import extract_meta

def js_scrape(url):
    pages = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=20000)
        page.wait_for_load_state("networkidle")

        for _ in range(3):
            page.mouse.wheel(0, 3000)
            page.wait_for_timeout(1500)

        html = page.content()
        pages.append(page.url)
        browser.close()

    soup = BeautifulSoup(html, "lxml")

    return {
        "meta": extract_meta(soup, url),
        "sections": extract_sections(soup, url),
        "interactions": {
            "clicks": ["scroll"],
            "scrolls": 3,
            "pages": pages
        }
    }
