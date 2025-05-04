import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


def load_config(path: str = "config.json") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def fetch_price(url: str) -> float:
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    # TODO: корректные селекторы для разных сайтов
    price_tag = soup.select_one('div[data-test-id="price"]')
    text = price_tag.get_text().strip().replace("₽", "").replace(" ", "")
    return float(text)


def parse_all() -> dict:
    cfg = load_config()
    results = {}
    for name, url in cfg.get("products", {}).items():
        try:
            price = fetch_price(url)
            results[name] = {"price": price, "timestamp": datetime.now()}
        except Exception as e:
            print(f"Error parsing {name}: {e}")
    return results
