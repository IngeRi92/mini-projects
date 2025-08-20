import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://www.cv.ee/api/v1/vacancy-search-service/search?limit=20&offset=0&keywords[]=Python&fuzzy=true&sorting=RELEVANCE&showHidden=true"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(url)
data = response.json()


def make_cv_url(job):
    base = "https://www.cv.ee/et/vacancy/"
    job_id = job["id"]
    employer_slug = job["employerName"].lower().replace(" ", "-")
    title_slug = job["positionTitle"].lower().replace(" ", "-")
    url = f"{base}{job_id}/{employer_slug}/{title_slug}"
    return url


with open("Beginner/web-scraper/jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Company", "Publish Date", "Expiration Date", "Link"])

    for job in data["vacancies"]:
        title = job.get("positionTitle", "Puudub pealkiri")
        company = job.get("employerName", "Puudub firma")

        publish_raw = job.get("publishDate")
        expiration_raw = job.get("expirationDate")

        publish_date = (
            datetime.fromisoformat(publish_raw.replace("Z", "+00:00")).strftime(
                "%d.%m.%Y"
            )
            if publish_raw
            else "Puudub"
        )
        expiration_date = (
            datetime.fromisoformat(expiration_raw.replace("Z", "+00:00")).strftime(
                "%d.%m.%Y"
            )
            if expiration_raw
            else "Puudub"
        )

        link = make_cv_url(job)

        writer.writerow([title, company, publish_date, expiration_date, link])
