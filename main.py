import schedule
import time
from parser import parse_all
from database import init_db, insert_price
from visualizer import plot_price_history


def job():
    init_db()
    results = parse_all()
    for name, info in results.items():
        insert_price(name, info["price"], info["timestamp"])
        plot_price_history(
            product=name, save_path=f"reports/{name.replace(' ', '_')}_history.png"
        )


if __name__ == "__main__":
    schedule.every().day.at("00:00").do(job)
    print("Scheduler started, waiting for jobs...")
    while True:
        schedule.run_pending()
        time.sleep(60)
