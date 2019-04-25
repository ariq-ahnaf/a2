"""
Module to read data from CSV files and HTML file
to populate an SQL database

ITEC649 2019
"""

import csv
import sqlite3
from bs4 import BeautifulSoup
from database import DATABASE_NAME, create_tables


def read_relations(db, openfile):
    """Store the relations listed in filename into the database
    - db      : a connection to a database.
    - openfile: CSV file open for reading and holding a relation per line.
    This function does not return any values. After executing this function, each row of the CSV file
    will be stored as a relation in the database.

    Example of use:
    >>> db = sqlite3.connect(DATABASE_NAME)
    >>> with open('relations.csv') as f:
    >>>    read_relations(db, f)
    """
    pass

    reader = csv.DictReader(openfile, delimiter=',')
    for row in reader:
        db.execute('''insert into relations(product, location) values (?,?)''',(row['product'], row['location']))
        db.commit()


def read_locations(db, openfile):
    """Store the locations listed in the open file into the database
    - db      : a connection to a database.
    - openfile: CSV file open for reading and holding a location per line.
    This function does not return any values or print anything on screen. After executing this function,
    each row of the CSV file will be stored as a location in the database.

    Example of use:
    >>> db = sqlite3.connect(DATABASE_NAME)
    >>> with open('locations.csv') as f:
    >>>     read_locations(db, f)
    """
    pass

    reader = csv.DictReader(openfile, delimiter=',')
    for row in reader:
        db.execute('''insert into locations values (?,?,?,?,?)''',(row['id'], row['number'], row['street'], row['city'], row['state']))
        db.commit()


def read_stock(db, openfile):
    """Read the products from the open file and store them in the database
    - db      : a connection to a database.
    - openfile: HTML file open for reading and listing products.
    This function does not return any values or print anything on screen. After executing this function,
    the products found in the HTML file will be stored as product records in the database.

    Example of use:
    >>> db = sqlite3.connect(DATABASE_NAME)
    >>> with open('index.html', encoding='utf-8') as f:
    >>>     read_stock(db, f)
    """
    pass

    soup = BeautifulSoup(openfile.read(), 'html.parser')
    getContent = soup.find_all("div", class_="product")

    for item in getContent:
        getID = item.find_all("a")[0]
        id = getID.attrs["href"].split('/')[-1]
        description = getID.contents[0]
        getStock = item.find_all("div", class_="inventory")[0].contents[0]
        stock = getStock.split(' ')[0]
        getValue = item.find_all("div", class_="cost")[0].contents[0]
        currency = getValue[0:1]
        price = getValue[1:]
        db.execute('''insert into products values(?,?,?,?,?)''', (id, description, stock, price, currency))
        db.commit()


def report(db, openfile):
    """Generate a database report and store it in outfile
    - db      : a connection to a database
    - openfile: a CSV file open for writing
    This function does not return any values or print anything on screen. After executing this function,
    the file outfile will contain the product information, one row in the CSV file per product. Each row must
    contain the following information:
      - description
      - price (including the currency symbol)
      - amount in stock
      - store location

    Example of use:
    >>> db = sqlite3.connect(DATABASE_NAME)
    >>> with open('report.csv', 'w') as f:
    >>>     report(db, open('report.csv', 'w'))
    """
    pass

def main():
    """Execute the main code that calls all functions
    This code should call the above functions to read the files "relations.csv",
    "locatons.csv" and "index.html", and generate "report.csv" as described in
    the assignment specifications.
    """
    db = sqlite3.connect(DATABASE_NAME)
    create_tables(db)

    # Write your code below

    with open('relations.csv') as f:
        read_relations(db, f)

    with open('locations.csv') as f:
        read_locations(db, f)

    with open('index.html', encoding='utf-8') as f:
        read_stock(db, f)


# Do not edit the code below
if __name__=='__main__':
    main()
