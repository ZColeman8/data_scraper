# 🕸️ RemoteOK Job Scraper

A Python automation project that scrapes remote job listings from [RemoteOK](https://remoteok.com), saves them to a CSV file, and generates a summary report highlighting the top hiring companies and most in-demand skills.

---

## 🚀 Features

- Scrapes live remote jobs using RemoteOK’s public API
- Saves job data to a CSV file
- Generates a human-readable text summary report
- Uses structured logging throughout the project
- Includes automated tests using `pytest`
- Generates a Pytest HTML report
- Integrated with GitHub Actions for Continuous Integration (CI)

---

## 🛠️ Tech Stack

- Python 3.11
- `requests` for API calls
- `csv` for file handling
- `collections.Counter` for frequency analysis
- `logging` for log tracking
- `pytest` for testing
- GitHub Actions for CI

---

## 📁 Project Structure

```
data_scraper/
├── data/                        # Stores the generated jobs.csv file
├── reports/                     # Contains the generated summary_report.txt
├── src/
│   ├── scraper.py               # Main scraping logic
│   ├── report_generator.py      # Generates text summary report
│   └── utils/
│       ├── file_writer.py       # CSV export functionality
│       ├── logger.py            # Logging setup
├── tests/
│   └── test_scraper.py          # Pytest-based unit tests
├── main.py                      # Entry point for the scraper workflow
├── requirements.txt             # Required packages
├── pytest.ini                   # Pytest configuration
└── .github/workflows/ci.yml     # GitHub Actions workflow for CI
```

---

## 🧪 Running the Project

### ▶️ Run the Scraper

This command will:
- Scrape job listings from RemoteOK
- Save them to `data/jobs.csv`
- Generate a summary text report in `reports/summary_report.txt`

```bash
python main.py
```

### 🧪 Run Tests

All tests can be executed using:

```bash
pytest
```

Pytest will run test validations and check the output file structure.

---

## 📝 Sample Summary Output

```
📊 Total jobs scraped: 99

🏢 Top Hiring Companies:
- TransPerfect: 4 job(s)
- Tether Operations Limited: 4 job(s)
- TELUS Digital: 2 job(s)
- Arbitrum Foundation: 2 job(s)
- ModelVault: 2 job(s)

🏷️ Most In-Demand Tags:
- support: 36 job(s)
- digital nomad: 31 job(s)
- senior: 28 job(s)
- technical: 27 job(s)
- engineer: 27 job(s)
```

---

## 📋 Logging

Logs provide real-time visibility into the scraping and file generation process.

Example:
```
INFO - Starting job scraping workflow...
INFO - Saving 99 jobs to data/jobs.csv...
INFO - ✅ Jobs successfully saved to data/jobs.csv
INFO - Generating summary report...
INFO - Summary report saved to reports/summary_report.txt
INFO - Job scraping workflow completed successfully.
```

---

## 🔄 Continuous Integration (CI)

CI is set up with **GitHub Actions** to automatically run tests on every push to `main`.

You’ll find the workflow config in:

```
.github/workflows/ci.yml
```

It installs dependencies, runs `pytest`, and uploads the HTML report artifact.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/data_scraper.git
cd data_scraper
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🧼 .gitignore

Your `.gitignore` should include:

```
__pycache__/
*.pyc
.env
data/
reports/
```

---

## 📃 License

This project is for educational and portfolio use. Attribution appreciated if reused.

---

## 👨‍💻 Author

**Zach Coleman**  
QA Automation Engineer in Training

---

## 🙌 Acknowledgements

- [RemoteOK](https://remoteok.com) — for making job listings publicly accessible.
