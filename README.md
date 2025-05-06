# AI601-PROJ

```markdown
# 📰 Urdu News Classification Pipeline

A modular ETL + ML + Dashboard project to scrape Urdu news articles, classify them using an ML model, and visualize predictions through a live dashboard.

---

## 🚀 Architecture Overview

```

Airflow DAG (scraper → preprocessing → store in Postgres)
|
v
🗃️ PostgreSQL (stores raw and processed predictions)
|
v
⚡ FastAPI (serves ML predictions)
|
v
📊 Streamlit (visualizes predictions by label/sentiment)

````

---

## 📦 Tech Stack

| Component     | Tech                     |
|---------------|--------------------------|
| Scraper/ETL   | Airflow + Python         |
| Database      | PostgreSQL (via Docker)  |
| Model Server  | FastAPI + ML pipeline    |
| Dashboard     | Streamlit + Plotly       |
| Orchestration | Docker Compose           |

---

## 🛠️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/urdu-news-pipeline.git
cd urdu-news-pipeline
````

### 2. Start PostgreSQL with Docker

```bash
docker-compose up -d postgres
```

📌 This runs Postgres on `localhost:5432` and initializes schema using `db/init.sql`.

### 3. Set up and run the Streamlit Dashboard

```bash
cd dashboard
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📊 Sample Predictions Table

| title           | predicted\_label | sentiment | persons        |
| --------------- | ---------------- | --------- | -------------- |
| کرکٹ میں فتح    | Sports           | Positive  | \["بابر اعظم"] |
| معیشت میں بہتری | Economy          | Positive  | \[]            |

---

## 📁 Repo Structure

```
urdu-news-pipeline/
│
├── docker-compose.yml           # Postgres setup
├── db/
│   └── init.sql                 # Schema + seed data
│
├── airflow/                     # Scraper and ETL DAGs
│   ├── dags/
│   └── Dockerfile
│
├── inference_api/              # FastAPI ML service
│   └── app.py
│
└── dashboard/                   # Streamlit dashboard
    ├── app.py
    ├── requirements.txt
    ├── config.py
    └── utils.py
```

---

## 🧠 Authors

* **Affan** – Streamlit dashboard & Postgres integration
* **Mudassar** – Airflow ETL & scraping pipeline
* **Usama** – Model API using FastAPI

---

## 📌 To Do

* [ ] Add live scraping via Airflow DAG
* [ ] Connect ML model to FastAPI
* [ ] Deploy dashboard with real predictions
* [ ] Optional: Add filter/sort in Streamlit UI

---

## 📜 License

MIT License – Use, modify, and share freely.

```

---

Let me know if you want me to update it with:
- GitHub repo link
- Airflow setup commands
- ML model example
- Deployment instructions (e.g., for Heroku or Dockerized dashboard)
```
