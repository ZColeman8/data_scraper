import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("job_scraper")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("logs/job_scraper.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
