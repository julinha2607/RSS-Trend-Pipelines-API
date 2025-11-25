from apscheduler.schedulers.blocking import BlockingScheduler
from .pipeline import run_pipeline
from datetime import datetime

def job():
    print(f"[{datetime.now()}] Starting scheduled job...")
    run_pipeline()
    print(f"[{datetime.now()}] Job finished.")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    
    # Run every 10 minutes
    scheduler.add_job(job, 'interval', minutes=10)
    
    print("Scheduler started. Press Ctrl+C to exit.")
    try:
        # Run once immediately on startup
        job()
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
