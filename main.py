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
        print(f"Your search term [bold cyan]{term}[/bold cyan] has been matched to:")
        for product in query:
            print(product.name)
    else:
        print(f"[bold red]:exclamation_mark: No products found with {term}[/bold red]")

# def list_user_products(user_id):
#     ...

# def list_products_per_tag(tag_id):
#     ...

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