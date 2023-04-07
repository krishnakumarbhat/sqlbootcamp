import tkinter 
from tkinter import *
import pymysql
from tkinter import ttk
from tkinter import messagebox

# establish database connection
db = pymysql.connect(host='localhost', user='root', password='yourpass', database='ecomms')
cursor = db.cursor()

top = tkinter.Tk()
top.geometry("800x400")

L = Label(top, text="Enter your customerid: ", fg='blue')
L.grid(row=0, column=0)
E = Entry(top, bd=5, width=50)
E.grid(row=0, column=1)

L1 =Label(top,text = "Enter your order_id: ",fg = 'blue')
L1.grid(row=1,column =0)
E1=Entry(top,bd=5,width=50)
E1.grid(row=1,column=1)



def cancel_order():
    # create a cursor object
    customerid = E.get()
    productid =E1.get()
    cursor = db.cursor()
    
    # delete the row with given customer_id and product_id from order_table
    delete_query = "DELETE FROM order_table WHERE customerid=%s AND productid=%s"
    cursor.execute(delete_query, (customerid, productid))
    
    # commit the transaction
    db.commit()
    
    # close the cursor
    cursor.close()
    
    print("Order for customer ID", customerid, "and product ID", productid, "has been cancelled.")



def search_data():
    # clear previous search results
    for row in table.get_children():
        table.delete(row)

    # get input values
    customerid = E.get()

    # retrieve data from database
    sql = f"SELECT customer.*, order_table.productid, order_table.totalprice FROM customer JOIN order_table ON customer.customerid=order_table.customerid WHERE customer.customerid='{customerid}'"
    cursor.execute(sql)
    data = cursor.fetchall()

    # insert retrieved data into table widget
    for row in data:
        table.insert('', END, values=row)

def add_to_order(productid):
    # insert a new row into the order_table
    customerid = E.get()
    # customerid = int(customerid)
    query = "INSERT INTO order_table (customerid, productid) VALUES (%s, %s)"
    values = (customerid, productid)
    cursor.execute(query, values)
    db.commit()  # commit the transaction




# Define a function to create a product box
def create_product_box(name, price, detail, image_file, row, column, productid):
    # Create a frame to hold the product information
    product_frame = tkinter.Frame(top, bd=1, relief="groove", padx=9, pady=9)
    product_frame.grid(row=row, column=column, padx=9, pady=9)

    # Create a label to display the product name
    product_name_label = tkinter.Label(product_frame, text=name, font=("Helvetica", 16, "bold"))
    product_name_label.pack()

    # Create a label to display the product price
    product_price_label = tkinter.Label(product_frame, text=price, font=("Helvetica", 10))
    product_price_label.pack()

    # Create a label to display the product details
    product_detail_label = tkinter.Label(product_frame, text=detail, font=("Helvetica", 8), wraplength=300)
    product_detail_label.pack(pady=10)

    # Load the image
    image = tkinter.PhotoImage(file=image_file)

    # Create a label to display the image
    image_label = tkinter.Label(product_frame, image=image)
    image_label.image = image
    image_label.pack(side="right", padx=1)

    # Create a button to buy the product
    # create the buy button and associate it with the add_to_order function
    buy_button = tkinter.Button(product_frame, text="Buy Now", bg="green", fg="white", font=("Helvetica", 12), command=lambda: add_to_order(productid))
    # buy_button = tkinter.Button(product_frame, text="Buy Now", bg="green", fg="white", font=("Helvetica", 12), command=lambda: add_to_order(productid))

    buy_button.pack(pady=10)
# Create 5 product boxes
create_product_box("Laptop", "$20", "intel i9 with RTX 4060", "a1.png", 6, 0,1)
create_product_box("mobile", "$20", "Snapdragon 8 Gen 1", "a1.png", 6, 1,2)
create_product_box("macbook", "$50", "m2 arm cortex ", "a3.png", 6, 3,3)
create_product_box("smart watch", "$30", "p-oled display", "a4.png", 7, 0,4)
create_product_box("i-pad", "$40", "retina display", "a5.png", 7, 1,5)
create_product_box("Airpod", "$50", "Noise cancelation", "a6.png", 7, 3,6)

def update_order():
    customerid = E.get()
    productid = E1.get()
    try:
        
        # Create a cursor object
        cursor = db.cursor()
        
        # Update the order table for the given customer id
        update_query = "UPDATE order_table SET productid = %s WHERE customerid = %s ORDER BY orderid DESC LIMIT 1"
        cursor.execute(update_query, (productid, customerid))
        
        # Commit the transaction
        db.commit()
        
        print(f"Order for customer id {customerid} has been updated with product id {productid}")
        
    except pymysql.Error as e:
        print(f"Error updating order: {e}")
        
    finally:
        # Close the database connection
        db.close()



def myButtonEvent():
    # get input values
    customerid = E.get()
    productid = E1.get()

    # retrieve data from database
    sql = f"SELECT * FROM customer WHERE customerid='{customerid}'"
    cursor.execute(sql)
    customer_data = cursor.fetchone()

    sql = f"SELECT * FROM products WHERE id='{productid}'"
    cursor.execute(sql)
    product_data = cursor.fetchone()

    # add order to database
    sql = f"INSERT INTO orders (customerid, productid, price) VALUES ('{customerid}', '{productid}', '{product_data[2]}')"
    cursor.execute(sql)
    db.commit()

    # show confirmation message
    messagebox.showinfo("Confirmation", f"Order for product {product_data[1]} with ID {productid} has been placed by customer {customer_data[1]} with ID {customerid}.")



Bcancel = tkinter.Button(text='cancel order', fg='blue', bg='orange', command=lambda: cancel_order())
Bcancel.grid(row=5, column=1)


Breplace = tkinter.Button(text='replace from cart', fg='blue', bg='orange', command=lambda: update_order())
Breplace.grid(row=5, column=0)


table = ttk.Treeview(top, columns=('ID', 'Name', 'Email', 'product-id'), show='headings')
table.configure(height=2)
table.heading('ID', text='ID')
table.column('ID', width=30)
table.heading('Name', text='Name')
table.column('Name', width=100)
table.heading('Email', text='Email')
table.column('Email', width=150)
table.heading('product-id', text='product-id')
table.column('product-id', width=80)
# table.heading('Price', text='Price')
# table.column('Price', width=60)
# table.heading('product-name', text='product-name')
# table.column('product-name', width=150)
table.grid(row=2, column=0, columnspan=2)



BSearch = tkinter.Button(text='Search', fg='blue', bg='orange', command=search_data)
BSearch.grid(row=0, column=2)



top.mainloop()

