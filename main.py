from itertools import product
from math import prod
from models import *
from setupdb import *
from datetime import datetime
from rich import print

__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

def search(term: str):
    term = term.lower()
    query = Products.select().where(Products.name.contains(term) | Products.description.contains(term))
    
    if query:
        print(f"Your search term [green]{term}[/green] has been matched to:")
        for product in query:
            print(product.name)
    else:
        print(f"[bold red]:exclamation_mark: No products where found with your search term {term}[/bold red]")

def list_user_products(user_id: int):
    query = Products.select().where(Products.owner == user_id)
    
    if query:
        user = Users.get_by_id(user_id)
        print(f"Products of [green]{user.name}[/green]:")
        for product in query:
            print(f"{product.name} - amount in stock: {product.amount_in_stock}")
    else:
        print(f"[bold red]:exclamation_mark: No match was found or an invalid id was given[/bold red]")

def list_products_per_tag(tag_id: int):
    query = Products.select().join(ProductTag).join(Tags).where(Tags.tag_id == tag_id)

    if query:
        tag = Tags.get_by_id(tag_id)
        print(f"Products with the tag [green]{tag.name}[/green]:")
        for product in query:
            print(f"{product.name}")
    else:
        print(f"[bold red]:exclamation_mark: No products where found with this tag or this tag does not exist[/bold red]")

def add_product_to_catalog(user_id: int, product_id: int):
    user = Users.get_by_id(user_id)
    product = Products.get_by_id(product_id)

    product.owner = user
    product.save()

    print(f"Product [green]{product.name}[/green] is added to [green]{user.name}[/green]")

def update_stock(product_id, new_quantity):
    query = Products.get_by_id(product_id)

    old_stock = query.amount_in_stock
    query.amount_in_stock = new_quantity
    query.save()

    print(f"[green]{query.name}[/green] - old stock: {old_stock}, new stock: {new_quantity}")


def purchase_product(product_id: int, buyer_id: int, quantity: int):
    product = Products.get_by_id(product_id)
    buyer = Users.get_by_id(buyer_id)

    if buyer_id == product.owner:
        print(f"[bold red]:cross_mark: You cannot buy products from yourself {buyer.name}[/bold red]")

    if quantity >= product.amount_in_stock:
        print(
            f"[bold red]:exclamation_mark: Insufficient stock of {product.name},[/bold red] current stock is: {product.amount_in_stock}")

    else:
        price_per_unit = product.price_per_unit
        purchased_price = round(product.price_per_unit * quantity, 2)

        transaction = Transactions.create(
            buyer=buyer_id,
            purchased_product=product_id,
            purchased_quantity=quantity,
            purchased_price=purchased_price,
            date=datetime.now().date()
        )

        print(f"On {transaction.date} {buyer.name} bought {quantity}x {product.name} for the total amount of: €{transaction.purchased_price}\nPrice per unit is €{price_per_unit}")

        new_quantity = product.amount_in_stock - quantity

        update_stock(product_id, new_quantity)

def remove_product(product_id):
    try:
        query = Products.get_by_id(product_id)
        print(f"Product [green]{query.name}[/green] has been removed")
        query.delete_instance()

    except DoesNotExist:
        print(f"[bold red]:exclamation_mark: Product id {product_id} does not exist or has already been removed[/bold red]")

def main():
    if os.path.exists("betsy-webshop.db") == True:
        delete_database()

if __name__ == '__main__':
    main()