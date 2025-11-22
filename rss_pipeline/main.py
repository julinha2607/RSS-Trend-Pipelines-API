from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from .database import init_db, SessionLocal, Trend, Article

app = FastAPI(title="RSS Trends API")

# Dependency to get DB session
#The code underneath creates the connection and makes sure that the connection to the database is closed after the request is finished, indepedently of 
# the result of the request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#This code is executed when the application starts up and makes sure the database is initialized
@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to RSS Trends API. Go to /docs for documentation."}

@app.get("/trends")
def get_trends(limit: int = 10, db: Session = Depends(get_db)):
    """
    Returns the top trending keywords.
    """
    trends = db.query(Trend).order_by(Trend.count.desc()).limit(limit).all()
    return trends

@app.get("/articles")
def get_articles(limit: int = 10, db: Session = Depends(get_db)):
    """
    Returns latest articles. Optionally filtered by keyword in title.
    """
    articles = db.query(Article).order_by(Article.published_at.desc()).limit(limit).all()
    return articles
