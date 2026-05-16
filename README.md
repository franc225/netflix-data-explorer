# Netflix Data Explorer


![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-20BEFF)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

A simple Python data pipeline project using Docker and GitHub Actions CI/CD.

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
├── requirements.txt
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

## Sample Output

```text
      type  count
0    Movie   XXXX
1  TV Show   XXXX
```

## Future Improvements

- Add automated tests with pytest
- Add GitHub Actions CI/CD
- Publish Docker image
- Add dashboard visualization