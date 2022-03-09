from models import *
from rich import print
import os

# Delete database
def delete_database():
    cwd = os.getcwd()
    path_database = os.path.join(cwd, "betsy-webshop.db")
    if os.path.exists(path_database):
        os.remove(path_database)

# Create database
def create_database():
    db.connect()
    print(f"[green]Database created![/green]")

    db.create_tables([Users, Products, Tags, ProductTag, Transactions])

    # Users
    phil = Users.create(name="Phil Fisby", address="Chive Plaza 723", zip_code="6216 AA", city="Norfolk", billing_information="VISA 5100147716225856")
    lucius = Users.create(name="Lucius Twigg", address="Meadow Vale Pass 5", zip_code="3808 BB", city="Dingle", billing_information="MasterCard 5048376528697995")
    roger = Users.create(name="Roger Reynolds", address="Laurel Street 293", zip_code="2770 CC", city="Nakuru", billing_information="Maestro 5048372216402848")
    jane = Users.create(name="Jane York", address="Bultman Pass 228", zip_code="4425 DD", city="Oster", billing_information="American Express 5002352453112296")
    emma = Users.create(name="Emma Sully", address="Russell Parkway 3", zip_code="6139 EE", city="New York City", billing_information="Bankcard 5002351853507998")

    # Products
    shirt = Products.create(owner= phil, name="Shirt", description="Long sleeves, with buttons at the front" ,price_per_unit=129.00, amount_in_stock=5,)
    hoodie = Products.create(owner= lucius, name="Hoodie", description="Sweater with a hood, with pockets at the front" ,price_per_unit=79.95, amount_in_stock=3,)
    chino = Products.create(owner= roger, name="Chino", description="Pants made of cotton, loose fit" ,price_per_unit=39.95, amount_in_stock=12,)
    cardigan = Products.create(owner= jane, name="Vest", description="Woolen vest with buttons" ,price_per_unit=19.95, amount_in_stock=6,)
    skirt = Products.create(owner= emma, name="Skirt", description="A fluttery ankle length skirt" ,price_per_unit=14.95, amount_in_stock=18,)

    # Tags
    top = Tags.create(name="top")
    bottom = Tags.create(name="bottom")
    cotton = Tags.create(name="cotton")
    wool = Tags.create(name="wool")
    buttons = Tags.create(name="buttons")
    casual = Tags.create(name="casual")
    business = Tags.create(name="business")
    prints = Tags.create(name="prints")

    # ProductTags
    ProductTag.create(product=shirt, tag=top)
    ProductTag.create(product=shirt, tag=buttons)
    ProductTag.create(product=shirt, tag=casual)

    ProductTag.create(product=hoodie, tag=top)
    ProductTag.create(product=hoodie, tag=cotton)
    ProductTag.create(product=hoodie, tag=casual)

    ProductTag.create(product=chino, tag=bottom)
    ProductTag.create(product=chino, tag=cotton)
    ProductTag.create(product=chino, tag=business)

    ProductTag.create(product=cardigan, tag=top)
    ProductTag.create(product=cardigan, tag=wool)
    ProductTag.create(product=cardigan, tag=buttons)

    ProductTag.create(product=skirt, tag=bottom)
    ProductTag.create(product=skirt, tag=prints)
    ProductTag.create(product=skirt, tag=casual)