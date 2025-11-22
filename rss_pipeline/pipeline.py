from sqlalchemy.orm import Session
from datetime import datetime
import time
from .database import SessionLocal, Article, Trend
from .ingestor import fetch_feeds
from .processor import extract_keywords

def save_article(db: Session, entry):
    """
    Saves an article to the database if it doesn't exist.
    """
    # Check if article already exists (by link)
    existing = db.query(Article).filter(Article.link == entry.link).first()
    if existing:
        return None
    
    # Handle date parsing (simplified)
    published_date = datetime.utcnow()
    if hasattr(entry, 'published_parsed') and entry.published_parsed:
        published_date = datetime.fromtimestamp(time.mktime(entry.published_parsed))

    article = Article(
        title=entry.title,
        link=entry.link,
        source=entry.get('source', 'Unknown'),
        published_at=published_date,
        content=entry.get('summary', '') # RSS usually has 'summary' or 'description'
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

def update_trends(db: Session, text):
    """
    Extracts keywords and updates the Trend table.
    """
    keywords = extract_keywords(text)
    for word, count in keywords:
        # Check if trend exists
        trend = db.query(Trend).filter(Trend.keyword == word).first()
        if trend:
            trend.count += count
            trend.date = datetime.utcnow() # Update last seen date
        else:
            trend = Trend(keyword=word, count=count)
            db.add(trend)
    db.commit()

def run_pipeline():
    """
    Main function to run the ETL process.
    """
    print("Starting pipeline...")
    db = SessionLocal()
    try:
        entries = fetch_feeds()
        new_articles_count = 0
        
        for entry in entries:
            article = save_article(db, entry)
            if article:
                new_articles_count += 1
                # Combine title and summary for better keyword extraction
                text = f"{article.title} {article.content or ''}"
                update_trends(db, text)
                print(f"Saved: {article.title[:50]}...")
        
        print(f"Pipeline finished. {new_articles_count} new articles processed.")
        
    except Exception as e:
        print(f"Error running pipeline: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    run_pipeline()
