from models import *
import os
from peewee import *
from datetime import datetime

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Fill database with test data
def populate_test_data():
    db.create_tables([Tag, Product, User, User_Products, Product_Tag, Transaction])

    # Tag: name
    game = Tag.create(name="game")
    baked_goods = Tag.create(name="baked goods")
    fruit = Tag.create(name="fruit")
    caramel = Tag.create(name="caramel")
    crafts = Tag.create(name="crafts")
    wood = Tag.create(name="wood")
    fabric = Tag.create(name="fabric")

    # Product: name, description, price_per_unit, stock
    puzzle = Product.create(name="Puzzle", description="game", price_per_unit=10, stock=30)
    card_deck = Product.create(name="Card deck", description="game", price_per_unit=5, stock=65)
    apple_pie = Product.create(name="Apple pie", description="Pie made of apples", price_per_unit=3, stock=5)
    stroopwafel = Product.create(name="Stroopwafel", description = "Dutch cookie with caramel", price_per_unit=2, stock=85)
    table = Product.create(name="Table", description="Wooden table", price_per_unit=145, stock=4)
    chair = Product.create(name="Chair", description="Upholstered chair", price_per_unit=60, stock=8)

    # Users: name, adress, billing_info
    didi = User.create(name="Didi", adress="Cherokee Plaza 274", billing_info='Didi King, Cherokee Plaza 274, 1504 AA, Amsterdam')
    lucius = User.create(name="Lucius", adress="ORM Street 23", billing_info='Lucius Burrows, Golf Parkway 992, 3439 ZZ, Nieuw-Lekkerland')
    phil = User.create(name="Phil", adress="Python Lane 13", billing_info='Phil Ginn, Stone Corner Alley 246, 4004 BB, Apeldoorn')

    User_Products.create(user=didi, product=apple_pie, quantity_owned=1)
    User_Products.create(user=didi, product=stroopwafel, quantity_owned=20)
    User_Products.create(user=lucius, product=puzzle, quantity_owned=2)
    User_Products.create(user=lucius, product=card_deck, quantity_owned=5)
    User_Products.create(user=phil, product=table, quantity_owned=1)
    User_Products.create(user=phil, product=chair, quantity_owned=6)

    # Product_Tag: product, tag
    Product_Tag.create(product=puzzle, tag=game)
    Product_Tag.create(product=card_deck, tag=game)
    Product_Tag.create(product=apple_pie, tag=baked_goods)
    Product_Tag.create(product=apple_pie, tag=fruit)
    Product_Tag.create(product=stroopwafel, tag=baked_goods)
    Product_Tag.create(product=stroopwafel, tag=caramel)
    Product_Tag.create(product=table, tag=crafts)
    Product_Tag.create(product=table, tag=wood)
    Product_Tag.create(product=chair, tag=crafts)
    Product_Tag.create(product=chair, tag=fabric)

# def search(term):
#     ...

# def list_user_products(user_id):
#     ...

# def list_products_per_tag(tag_id):
#     ...

# def add_product_to_catalog(user_id, product):
#     ...

# def update_stock(product_id, new_quantity):
#     ...

# def purchase_product(product_id, buyer_id, quantity):
#     ...

# def remove_product(user_id, product_id):
#     ...

if __name__ == "__main__":
    if os.path.exists('betsy-webshop.db') == False:
        populate_test_data()