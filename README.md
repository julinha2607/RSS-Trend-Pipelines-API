# RSS Trends Pipeline + API

A Data Engineering project that fetches tech news from RSS feeds, extracts trending keywords, and serves the data via a REST API.

## 🚀 Features
- **ETL Pipeline**: Fetches data from Hacker News, TechCrunch, and The Verge.
- **NLP Processing**: Cleans text and extracts top keywords.
- **FastAPI Backend**: Serves trends and articles via JSON endpoints.
- **Automation**: Scheduler to run the pipeline every 10 minutes.
- **Database**: SQLite storage with SQLAlchemy ORM.

## 🛠️ Setup

1. **Create a Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/WSL
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ How to Run

### 1. Run the Pipeline (Manually)
To fetch data and populate the database immediately:
```bash
python -m rss_pipeline.pipeline
```

### 2. Start the API Server
To serve the data:
```bash
uvicorn rss_pipeline.main:app --reload
```
- Access documentation at: `http://127.0.0.1:8000/docs`

### 3. Start the Scheduler (Automation)
To keep fetching data automatically every 10 minutes:
```bash
python -m rss_pipeline.scheduler
```

## 📡 API Endpoints

- `GET /trends`: Returns top keywords (e.g., `?limit=10`).
- `GET /articles`: Returns latest articles (e.g., `?keyword=google`).

## 📂 Project Structure
- `rss_pipeline/ingestor.py`: Fetches RSS feeds.
- `rss_pipeline/processor.py`: Cleans text and extracts keywords.
- `rss_pipeline/database.py`: Database models and connection.
- `rss_pipeline/pipeline.py`: Orchestrates the ETL process.
- `rss_pipeline/scheduler.py`: Runs the pipeline periodically.
- `rss_pipeline/main.py`: FastAPI application.
