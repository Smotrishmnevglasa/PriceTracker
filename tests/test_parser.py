import pytest
from parser import fetch_price


class DummyResp:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        pass


def test_fetch_price(monkeypatch):
    html = '<div data-test-id="price">1 234 ₽</div>'
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: DummyResp(html))
    price = fetch_price("http://example.com")
    assert price == 1234.0
