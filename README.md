# Betsy Webshop

Betsy Webshop is a database management system for a fictional marketplace where users can buy and sell products.

## Delete or create database

1. Go to your terminal
2. Enter **py** and press enter
3. Enter **import setupdb** and press enter

To _delete_ the current database type in **setupdb.delete_database()**

To _create_ a new database type in **setupdb.create_database()**

## Check functions

1. Go to your terminal
2. Enter **py** and press enter
3. Enter **import main** and press enter

_Examples:_

```
main.search("Cardigan")
main.list_user_products(1)
main.list_products_per_tag(1)
main.add_product_to_catalog(1, 2)
main.update_stock(1, 10)
main.purchase_product(1, 3, 4)
main.remove_product(1)
```

## Check the database

1. Make sure the database is created (see above)
2. Go to your terminal
3. Enter **sqlite3 betsy-webshop.db** and press enter
4. Enter **.headers ON** and press enter
5. Enter **.mode column** and press enter
6. Enter **.table** and press enter to see an overview of all existing tables
7. Select one of the tables, for example:

**SELECT \* FROM users;**

Or

**SELECT \* FROM products;**
