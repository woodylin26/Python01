import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

# Create product table
sql_command = """
CREATE TABLE product
(
product_id INTEGER PRIMARY KEY,
name VARCHAR(128) NOT NULL,
rrp FLOAT NOT NULL,
available_from DATE not NULL
);"""
cursor.execute(sql_command)

# Create order table
sql_command = """
CREATE TABLE orders
(
order_id INTEGER PRIMARY KEY,
product_id INTEGER NOT NULL,
quantity INTERGER NOT NULL,
order_price FLOAT NOT NULL,
dispatch_date DATE NOT NULL,
);"""
cursor.execute(sql_command)

sql_command = """INSERT INTO product (product_id, name, rrp, available_from)
    VALUES (101, "Bayesian Methods for Nonlinear Classification and Regression", "94.95", "(DATEADD(DD,-(DATEPART(WEEKDAY, GETDATE())+5)%7, GETDATE()))");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO product (product_id, name, rrp, available_from)
    VALUES (102, "(next year) in Review (preorder)", "21.95", "(DATEADD(year,1,getdate()))");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO product (product_id, name, rrp, available_from)
    VALUES (103, "Learn Python in Ten Minutes", "2.15", "(DATEADD(months,-3,getdate()))");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO product (product_id, name, rrp, available_from)
    VALUES (104, "sports almanac (1999-2049)", "3.38", "(DATEADD(year,-2,getdate()))");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO product (product_id, name, rrp, available_from)
    VALUES (105, "finance for dummies", "84.99", "(DATEADD(year,-1,getdate()))");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date)
    VALUES (1000, 101, 1, "90.00", "(DATEADD(months,-2,getdate()))");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date)
    VALUES (1001, 103, 1, "1.15", "(DATEADD(day,-40,getdate()))");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date)
    VALUES (1002, 101, 10, "90.00", "(DATEADD(months,-11,getdate()))");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date)
    VALUES (1003, 104, 11, "3.38", "(DATEADD(months,-6,getdate()))");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date)
    VALUES (1004, 105, 11, "501.33", "(DATEADD(year,-2,getdate()))");"""
cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()

cursor.execute("SELECT product.name product.available_from
FROM product
INNER JOIN orders ON product.product_id=orders.product_id"
WHERE (orders.quantity < 10) AND NOT (product.available_from <=DATEADD(m, -1, GETDATE()) )

connection.commit()

connection.close()
