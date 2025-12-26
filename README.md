# Universal Website Scraper

A full-stack **Universal Website Scraper (MVP)** built using **FastAPI** for the backend and **React (Vite)** for the frontend.

The system accepts a website URL, scrapes both static and JavaScript-rendered content, explores additional content via scrolling, groups content into logical sections, and returns structured, section-aware JSON. A minimal React UI is provided to view and download the scraped JSON.

---

## How to Set Up and Run the Project

### Prerequisites

- Python **3.10+**
- Node.js **16+**
- npm

---

### Linux / macOS / Windows

```bash
chmod +x run.sh
./run.sh

Server starts at http://localhost:8000

Windows does not support chmod. Run these steps-
python -m venv venv
.\venv\Scripts\activate

pip install -r backend\app\requirements.txt
python -m playwright install chromium

cd frontend
npm install
npm run build
cd ..

python -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000

### Environment Details

Backend: FastAPI served using uvicorn

Frontend: React (Vite), built and served as static files by FastAPI

Scraping strategy:

Static HTML scraping using httpx and BeautifulSoup

JavaScript rendering fallback using Playwright

run.sh:

Creates/uses a virtual environment

Installs backend dependencies

Runs playwright install chromium

Builds the frontend

Starts the FastAPI server


### API Endpoints
Health Check
GET /healthz


Response:

{
  "status": "ok"
}

### Scrape Website
POST /scrape


Request body:

{
  "url": "https://example.com"
}


Response:

Section-aware JSON containing:

Page metadata

Extracted content sections

Interaction details (scrolls, pages)

Errors (if any, without crashing the server)

Frontend UI

Accessible at: http://localhost:8000

Features:

URL input field

“Scrape” button

Loading state

Expandable list of sections

JSON viewer for each section

“Download JSON” button

### Primary URLs Used for Testing

https://en.wikipedia.org/wiki/Artificial_intelligence

Largely static page

Used to validate static scraping, metadata extraction, and section grouping
