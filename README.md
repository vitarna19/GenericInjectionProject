# Generic Continuous Data Ingestion from Multiple Streaming Sources into Databricks

## Project Overview

This project demonstrates a generic and automated continuous data ingestion pipeline. It simulates ingesting data from both external APIs and a relational database, applies conditional logic to trigger workflows, and stores results in a cloud-like folder structure. The entire workflow is orchestrated using GitHub Actions to simulate a real-world Databricks or Azure Data Factory (ADF) pipeline.

## Features

1. Scheduled REST API Ingestion
   Fetches data for 5 countries (India, US, UK, China, Russia) from a public API and saves them as JSON files.

2. Conditional Database Ingestion
   Copies customer data from a local SQLite database only if the record count is greater than 500.

3. Parent-Child Pipeline Logic
   If the customer count exceeds 600, a child pipeline is triggered to ingest product data.

4. Simulated Data Lake (ADLS)
   Stores output files in a local folder `adls/`, simulating Azure Data Lake Storage.

5. GitHub Actions Automation
   All workflows run automatically at 12:00 AM and 12:00 PM IST.

6. Artifact Uploads
   JSON output files are uploaded as downloadable artifacts from every pipeline run.

## Architecture Diagram

```
GitHub Actions Scheduler (runs 2x daily)
        |
        v
  country_fetcher.py
    - Fetches data for 5 countries from REST API
    - Saves JSON to adls/
        |
        v
  db_to_adls_pipeline.py
    - Checks customer count from DB
    - Saves if count > 500
    - If count > 600, triggers:
        |
        v
  product_pipeline.py
    - Receives customer count
    - Saves product data to adls/
```

## Folder Structure

```
project/
├── adls/
│   ├── customers.json
│   └── products.json
├── country_fetcher.py
├── db_setup.py
├── db_to_adls_pipeline.py
├── product_pipeline.py
├── requirements.txt
└── .github/
    └── workflows/
        └── scheduler.yml
```

## Setup & Run Locally

Follow the steps below to run the project manually on your system:

### 1. Clone the Repository

```bash
git clone https://github.com/vitarna19/GenericInjectionProject.git
cd GenericInjectionProject
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up SQLite Database

```bash
python db_setup.py
```

This creates sample customer and product tables with dummy data.

### 4. Run Pipelines Manually (Optional Testing)

```bash
python country_fetcher.py
python db_to_adls_pipeline.py
```

* `country_fetcher.py`: Fetches country data and stores individual JSON files.
* `db_to_adls_pipeline.py`:

  * Saves customer data if count > 500
  * Triggers product pipeline if count > 600

## GitHub Automation

* Runs automatically every day at:

  * 12:00 AM IST
  * 12:00 PM IST

* View execution logs in the Actions tab of your GitHub repository.

* Download outputs (`customers.json`, `products.json`) from the workflow artifacts section.

## Tech Stack

* Python 3.10
* SQLite (mock DB)
* GitHub Actions (workflow scheduler)
* REST APIs (country data source)
* JSON (for all output files)
* Command-line parameter passing (simulates ADF/Databricks-style workflow)

## Author

* Name: Vitarna Sharma
* Role: Data Engineer Intern
* Project: Celebal Summer Internship — Generic Continuous Data Ingestion
