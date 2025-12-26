from fastapi import APIRouter, HTTPException
from urllib.parse import urlparse
from datetime import datetime, timezone
from backend.app.scraper.static import static_scrape
from backend.app.scraper.playwright_scraper import js_scrape

router = APIRouter()

@router.get("/healthz")
def healthz():
    return {"status": "ok"}

@router.post("/scrape")
def scrape(payload: dict):
    url = payload.get("url")

    if not url or urlparse(url).scheme not in ["http", "https"]:
        raise HTTPException(status_code=400, detail="Invalid URL")

    errors = []

    try:
        result = static_scrape(url)
        if len(result["sections"]) < 2:
            raise ValueError("Insufficient static content")
        strategy = "static"
    except Exception as e:
        errors.append({"message": str(e), "phase": "static"})
        result = js_scrape(url)
        strategy = "js"

    result.update({
        "url": url,
        "scrapedAt": datetime.now(timezone.utc).isoformat(),
        "errors": errors,
        "strategy": strategy
    })

    return {"result": result}
