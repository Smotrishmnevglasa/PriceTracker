import matplotlib.pyplot as plt
from database import get_history


def plot_price_history(product: str, db_path: str = "prices.db", save_path: str = None):
    data = get_history(product, db_path)
    if not data:
        print(f"No data for {product}")
        return

    prices, times = zip(*data)
    plt.figure()
    plt.plot(times, prices)
    plt.title(f"Price history for {product}")
    plt.xlabel("Time")
    plt.ylabel("Price, ₽")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
