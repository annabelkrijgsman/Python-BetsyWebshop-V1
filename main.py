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
        print(f"[bold red]:exclamation_mark: No products found with {term}[/bold red]")

def list_user_products(user_id: int):
    query = Products.select().where(Products.owner == user_id)
    
    if query:
        user = Users.get_by_id(user_id)
        print(f"Products of [green]{user.name}[/green]:")
        for product in query:
            print(f"{product.name}. Amount in stock: {product.amount_in_stock}")
    else:
        print(f"[bold red]:exclamation_mark: No match was found or a invalid id was given.[/bold red]")

def list_products_per_tag(tag_id: int):
    query = Products.select().join(ProductTag).join(Tags).where(Tags.tag_id == tag_id)

    if query:
        tag = Tags.get_by_id(tag_id)
        print(f"Tagged products with the tag [green]{tag.name}[/green]:")
        for product in query:
            print(f"{product.name}")
    else:
        print(f"[bold red]:exclamation_mark: No products found with this tag or this tag does not exist[/bold red]")

# # Check check check > fails
# def add_product_to_catalog(user_id, product):
#     ...

# def update_stock(product_id, new_quantity):
#     ...

# # Check check check > fails
# def purchase_product(product_id, buyer_id, quantity):
#     ...

# def remove_product(user_id, product_id):
#     ...

def main():
    if os.path.exists("betsy-webshop.db") == True:
        delete_database()

if __name__ == '__main__':
    main()