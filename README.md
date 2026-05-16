# Netflix Data Explorer


![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![Pytest](https://img.shields.io/badge/Tests-pytest-success)
[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-20BEFF)](https://www.kaggle.com/datasets/shivamb/netflix-shows)
![CI Pipeline](https://github.com/franc225/netflix-data-explorer/actions/workflows/ci.yml/badge.svg)

A containerized Python data pipeline project using Docker, pytest, and GitHub Actions continuous integration workflows.

## Project Overview

This project:
- loads a Netflix dataset using pandas
- performs a simple aggregation analysis
- exports a summary CSV file
- runs inside a Docker container
- will later include GitHub Actions CI/CD automation

Dataset source:
- Netflix Movies and TV Shows Dataset from Kaggle

## Technologies Used

- Python 3.12
- pandas
- Docker
- GitHub Actions

## Project Structure

```text
netflix-data-explorer/
|
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   └── main.py
│
├── data/
│   └── netflix_titles.csv
│
├── output/
│   └── summary.csv
│
├── tests/
│   └── test_main.py
|
├── requirements.txt
├── run_pipeline.bat
├── Dockerfile
└── README.md
```

## Run Locally

### Python

```bash
python app/main.py
```

### Docker

Build image:

```bash
docker build -t netflix-pipeline .
```

Run container:

```bash
docker run netflix-pipeline
```

## Run Tests

### Local pytest

```bash
pytest
```

### Dockerized tests

Build image:

```bash
docker build -t netflix-pipeline .
```

Run tests inside container:

```bash
docker run netflix-pipeline
```

## Local Development Workflow

Run the complete local validation pipeline:

```bash
run_pipeline.bat
```

This script automatically:
1. Runs pytest automated tests
2. Builds the Docker image
3. Runs the Docker container

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration.

The automated workflow runs on:
- push to main branch
- pull requests

Pipeline steps:
1. Checkout repository
2. Setup Python
3. Install dependencies
4. Run pytest automated tests
5. Build Docker image

## Sample Output

```text
      type  count
0    Movie   XXXX
1  TV Show   XXXX
```

## Skills Demonstrated

- Python data processing
- pandas data analysis
- Docker containerization
- Automated testing with pytest
- GitHub Actions CI/CD
- Linux-based development workflows
- Reproducible environments

## Future Improvements

- Publish Docker image automatically
- Add advanced data validation tests
- Add data visualization dashboard
- Add logging and monitoring
- Add scheduled workflow execution