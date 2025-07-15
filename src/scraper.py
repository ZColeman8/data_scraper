import requests
from src.utils.logger import logger

def fetch_jobs():
    url = "https://remoteok.com/api"
    logger.info(f"Fetching jobs from {url}")

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        jobs = []
        for job in data[1:]:
            title = job.get("position", "").strip()
            company = job.get("company", "").strip()
            tags = job.get("tags", [])
            link = job.get("url", "").strip()

            if not title or not company or not link:
                continue

            jobs.append({
                "title": title,
                "company": company,
                "tags": tags,
                "link": link
            })

        logger.info(f"Fetched {len(jobs)} jobs.")
        return jobs
    
    except Exception as e:
        logger.error(f"Error fetching jobs: {e}")
        return []