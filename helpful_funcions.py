import hashlib
from database import db
import datetime
from models import product


def encript(str):
    return hashlib.sha256(str.encode()).hexdigest()


def add_db_product(product_):
    try:
        price = product_["price"].replace(".", ",")
        price = float(price)
        new_product = product(product_["url"],
                              product_["name"],
                              price,
                              price,
                              datetime.datetime.now())
        db.session.add(new_product)
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True
