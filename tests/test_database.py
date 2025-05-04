import os
from database import init_db, insert_price, get_history
from datetime import datetime

DB = "test_prices.db"


def setup_module(module):
    if os.path.exists(DB):
        os.remove(DB)
    init_db(DB)


def test_insert_and_get_history():
    now = datetime.now()
    insert_price("TestProd", 99.9, now, DB)
    history = get_history("TestProd", DB)
    assert len(history) == 1
    assert history[0][0] == 99.9
