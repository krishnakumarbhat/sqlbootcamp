before going to backend(sql) part install some python library like :

pip install tkinter pymysql

execute above command 

Step 1: Open the MySQL command prompt or any MySQL client of your choice.

Step 2: Create the ecomms database using the following command:


CREATE DATABASE ecomms;

Step 3: Switch to the ecomms database:


USE ecomms;

Step 4: Create the products table using the following command:



CREATE TABLE products (
  productid INT PRIMARY KEY,
  productname VARCHAR(50),
  price DECIMAL(10,2)
);


Step 5: Insert the data into the products table using the following command:



INSERT INTO products (productid, productname, price) VALUES
(1, 'laptop', 20),
(2, 'mobile', 30),
(3, 'macbook', 90),
(4, 'smartwatch', 30),
(5, 'ipad', 40),
(6, 'airpod', 50);



Step 6: Create the customer table using the following command:



CREATE TABLE customer (
  customerid INT PRIMARY KEY,
  Name VARCHAR(50),
  email VARCHAR(50)
);



Step 7: Insert the data into the customer table using the following command:



INSERT INTO customer (customerid, Name, email) VALUES
(123456, 'ravi', 'ravi45@gmail.com'),
(2, 'ramesh', 'ramesh44@sjce.com'),
(3, 'ragu', 'ragu899@gmail.com'),
(4, 'aneesh', 'aneesh45@outlook.com'),
(5, 'ashish', 'ashish24@proton.com'),
(6, 'karthik', 'karthik34@hotmail.com'),
(7, 'pranav', 'pranav23@gmail.com'),
(8, 'darshan', 'darshan23@ieee.com'),
(9, 'abhishak', 'abhishak33@outlook.com');



Step 8: Create the order_table using the following command:



CREATE TABLE order_table (
  orderid INT PRIMARY KEY,
  customerid INT,
  productid INT,
  totalprice DECIMAL(10,2),
  FOREIGN KEY (customerid) REFERENCES customer(customerid),
  FOREIGN KEY (productid) REFERENCES products(productid)
);



Step 9: Insert the data into the order_table using the following command:


INSERT INTO order_table (orderid, customerid, productid, totalprice) VALUES
(2, 3, 3, 55),
(3, 2, 30, 19),
(1, 3, 1, 24),
(1, 1, 3, 25),
(1, 2, 1, 25),
(2, 1, 2, 20);
That's it! You have successfully created the ecomms database with three tables - products, customer, and order_table.cong guys


![image](https://user-images.githubusercontent.com/79183768/230646259-95909489-413a-4b2c-a44e-30779af6a3fe.png)

