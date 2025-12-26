def extract_meta(soup, url):
    title = soup.title.string if soup.title else ""
    desc = ""
    canonical = None
    lang = soup.html.get("lang") if soup.html else "en"

    d = soup.find("meta", attrs={"name": "description"})
    if d:
        desc = d.get("content", "")

    c = soup.find("link", rel="canonical")
    if c:
        canonical = c.get("href")

    return {
        "title": title or "",
        "description": desc or "",
        "language": lang or "en",
        "canonical": canonical
    }
