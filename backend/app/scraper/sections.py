from urllib.parse import urljoin

def extract_sections(soup, base_url):
    sections = []
    idx = 0

    for tag in soup.find_all(["section", "main", "article"]):
        text = tag.get_text(" ", strip=True)
        if len(text) < 50:
            continue

        sections.append({
            "id": f"section-{idx}",
            "type": "section",
            "label": " ".join(text.split()[:5]),
            "sourceUrl": base_url,
            "content": {
                "headings": [h.get_text() for h in tag.find_all(["h1", "h2", "h3"])],
                "text": text,
                "links": [
                    {"text": a.get_text(), "href": urljoin(base_url, a.get("href"))}
                    for a in tag.find_all("a", href=True)
                ],
                "images": [
                    {"src": urljoin(base_url, i.get("src")), "alt": i.get("alt", "")}
                    for i in tag.find_all("img", src=True)
                ],
                "lists": [
                    [li.get_text() for li in ul.find_all("li")]
                    for ul in tag.find_all("ul")
                ],
                "tables": []
            },
            "rawHtml": str(tag)[:2000],
            "truncated": len(str(tag)) > 2000
        })
        idx += 1

    return sections
