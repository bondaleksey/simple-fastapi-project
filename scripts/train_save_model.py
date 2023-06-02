import sys
from recosys.models.serialize import store
from recosys.models.item_based_model import Flower


def main():
    data = Flower(name="Kaktus", age=25, values=("1", "2", "3"))
    train_store(data)


def train_store(data, filename="baseline"):
    store(data, filename)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(1)
