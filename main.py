from models import *
import os
from peewee import *
from datetime import datetime

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Create tables and fill database with test data
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

    # Users: name, address, billing_info
    didi = User.create(name="Didi", address="Cherokee Plaza 274", billing_info='Didi King, Cherokee Plaza 274, 1504 AA, Amsterdam')
    lucius = User.create(name="Lucius", address="ORM Street 23", billing_info='Lucius Burrows, Golf Parkway 992, 3439 ZZ, Nieuw-Lekkerland')
    phil = User.create(name="Phil", address="Python Lane 13", billing_info='Phil Ginn, Stone Corner Alley 246, 4004 BB, Apeldoorn')

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

def search(term):
    '''Print product name when given term matches a product name or is found in product description'''
    search_name_query = Product.select().where((Product.name ** f'%{term}%') | (Product.description ** f'%{term}%'))
    for product in search_name_query:
        print(product.name)

def list_user_products(user_id):
    '''Print list of products for given user'''
    user_products = []
    products = (Product.select()
                .join(User_Products)
                .join(User)
                .where(User.id == user_id)
    )
    for product in products:
        user_products.append(product.name)

    print(user_products)

def list_products_per_tag(tag_id):
    '''Print list of products for given tag'''
    tag_products = []
    products = (Product.select()
                .join(Product_Tag)
                .join(Tag)
                .where(Tag.id == tag_id)
    )
    for product in products:
        tag_products.append(product.name)

    print(tag_products)

# Check check check > fails
def add_product_to_catalog(user_id, product):
    '''Add product to given user'''
    get_user = User.get(User.id == user_id)
    get_product = Product.get(Product.name == product)
    User_Products.get_or_create(user=get_user, product=get_product)

    print(f'{product} added to user')

def update_stock(product_id, new_quantity):
    '''Update quantity in stock for given product'''
    update_stock = Product.update(stock=new_quantity).where(Product.id == product_id)
    update_stock.execute()

    print('Successfully updated stock')

# Check check check > fails
def purchase_product(product_id, buyer_id, quantity):
    '''Store user instance and product name so both can be used to: add a product to a user's catalog, update quantity of product owned by a user'''
    user = User.get(User.id == buyer_id)
    product_name = Product.get(Product.id == product_id).name

    '''Create transaction'''
    Transaction.create(buyer=buyer_id, purchased_product=product_id, amount_of_purchased_items=quantity, transaction_date=datetime.now())

    '''Update stock after transaction'''
    purchased_product = Product.get(Product.id == product_id)
    updated_stock = purchased_product.stock - quantity
    update_stock(product_id, updated_stock)

    '''Add product to user'''
    add_product_to_catalog(buyer_id, product_name)

    '''Update quantity of products owned by user'''
    update_quantity = (User_Products.update(quantity_owned=User_Products.quantity_owned + quantity).where(User_Products.user == user, User_Products.product == product_name))
    update_quantity.execute()

    print('Successfully updated quantity owned by user')

def remove_product(user_id, product_id):
    '''Remove product from user if product_id is found in User_Products'''
    user_product = User_Products.get_or_none(User_Products.user == user_id and User_Products.product == product_id)
    user_product.delete_instance()

    print('Successfully removed product from user')

if __name__ == "__main__":
    if os.path.exists('betsy-webshop.db') == False:
        populate_test_data()