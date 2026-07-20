# Customer Churn Analysis Pipeline

## Overview

This project is an end-to-end Data Engineering pipeline that extracts, transforms, and loads customer churn data into PostgreSQL for analytics and reporting.

The pipeline demonstrates industry-standard ETL practices including data ingestion, cleaning, validation, transformation, Dockerized PostgreSQL deployment, and SQL analytics.

---

## Project Architecture

```text
Raw CSV Data
      │
      ▼
Extract (Python)
      │
      ▼
Transform & Clean Data
      │
      ▼
PostgreSQL Database (Docker)
      │
      ▼
SQL Analytics
      │
      ▼
Business Insights
```

---

## Features

- Automated ETL Pipeline using Python
- Data Cleaning & Validation
- PostgreSQL Data Warehouse
- Dockerized Database
- SQL Analytics Queries
- Modular Python Architecture
- Documentation Included

---

## Tech Stack

- Python
- PostgreSQL
- Docker
- SQL
- Pandas
- Git
- GitHub

---

## Project Structure

```text
Customer-Churn-Analysis-Pipeline
│
├── data/
├── docs/
├── screenshots/
├── sql/
├── src/
├── tests/
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ETL Workflow

### 1. Extract

Reads customer churn data from CSV.

### 2. Transform

- Cleans missing values
- Removes duplicates
- Standardizes data
- Validates records

### 3. Load

Loads transformed data into PostgreSQL for analytics.

---

## Running the Project

### Clone the repository

```bash
git clone https://github.com/matthewoke94/Customer-Churn-Analysis-Pipeline.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start PostgreSQL

```bash
docker compose up -d
```

### Run the ETL Pipeline

```bash
python -m src.extract
python -m src.transform
python -m src.load
```

---

## Sample SQL Analytics

Count all customer records:

```sql
SELECT COUNT(*) FROM raw_churn;
```

Count churned vs retained customers:

```sql
SELECT churn, COUNT(*)
FROM raw_churn
GROUP BY churn;
```

---

## Screenshots

### GitHub Repository

![GitHub Repository](screenshots/github_home.png)

### Project Structure

![VS Code Project](screenshots/vscode_project.png)

### ETL Pipeline

![Extract Pipeline](screenshots/extract_run.png)

### PostgreSQL Database

![PostgreSQL Database](screenshots/postgres_database.png)

---

## Business Value

This pipeline demonstrates how customer churn data can be transformed into a structured analytics dataset suitable for business intelligence, reporting, dashboarding, and future machine learning applications.

---

## Future Improvements

- Power BI Dashboard
- AWS Deployment
- Apache Airflow Scheduling
- Automated Data Quality Monitoring
- CI/CD Pipeline

---

## Author

**Matthew James**

**Data Engineer | Python | SQL | PostgreSQL | Docker | ETL Pipelines**

GitHub:  
https://github.com/matthewoke94# Customer-Churn-Analysis-Pipeline
