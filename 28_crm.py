from tkinter import *
from PIL import ImageTk, Image
import psycopg2

root = Tk()
root.title('Tu nerd')
root.geometry("400x600")

try:
    conn = psycopg2.connect("dbname=tkinter user=hugo password=hola123, host=localhost port=5432")
    print("Database is on")
except:
    print("Database is off")

#print(conn)

#Create a cursor and initialize it

myCursor = conn.cursor()

#Create database
#myCursor.execute("CREATE DATABASE codemy WITH OWNER hugo")

#Create a table

#command = ("""CREATE TABLE customers (
 #   user_id SERIAL PRIMARY KEY, 
  #  first_name VARCHAR (255), 
   # last_name VARCHAR (255), 
    #zipcode INT, 
    #price_paid NUMERIC(10, 2))""")

    #command = ("CREATE TABLE customers (
    #user_id SERIAL PRIMARY KEY, \
    #first_name VARCHAR (255), \
    #last_name VARCHAR (255), \
    #zipcode INT, \
    #price_paid NUMERIC(10, 2))")


#Alter Table
#myCursor.execute("ALTER TABLE customers ADD COLUMN address_2 VARCHAR(255);")
'''
myCursor.execute("""
ALTER TABLE customers 
ADD COLUMN phone VARCHAR(255),
ADD COLUMN payment_method VARCHAR(50),
ADD COLUMN discount_code VARCHAR(255)
""")
'''

# Show table
#myCursor.execute("SELECT * FROM customers")
#print(myCursor.description)

#Clear Text Fields
def clearFields():
    firstNameBox.delete(0, END)
    lastNameBox.delete(0, END)
    address1Box.delete(0, END)
    address2Box.delete(0, END)
    cityBox.delete(0, END)
    stateBox.delete(0, END)
    zipcodeBox.delete(0, END)
    countryBox.delete(0, END)
    phoneBox.delete(0, END)
    emailBox.delete(0, END)
    usernameBox.delete(0, END)
    paymentMethodBox.delete(0, END)
    discountCodeBox.delete(0, END)
    pricePaidBox.delete(0, END)

#Submit Customer to Database
def addCustomer():
    sqlCommand = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (firstNameBox.get(), lastNameBox.get(), zipcodeBox.get(), pricePaidBox.get(), emailBox.get(), address1Box.get(), address2Box.get(), cityBox.get(), stateBox.get(), countryBox.get(), phoneBox.get(), paymentMethodBox.get(), discountCodeBox.get(), usernameBox.get())
    myCursor.execute(sqlCommand, values)

    #Commit the changes to the database
    conn.commit()
    myCursor.close()
    conn.close()
    

    #Clear fields
    clearFields()
    
    

#Create a Label
titleLabel = Label(root, text = "Customer Database", font = ("Helvetica", 16))
titleLabel.grid(row = 0, column = 0, columnspan = 2, pady = "10")

#Create Main Form to Enter Customer Data
firstNameLabel = Label(root, text = "First Name").grid(row = 1, column = 0, sticky = W, padx = 10)
lastNameLabel = Label(root, text = "Last Name").grid(row = 2, column = 0, sticky = W, padx = 10)
address1Label = Label(root, text = "Address 1").grid(row = 3, column = 0, sticky = W, padx = 10)
address2Label = Label(root, text = "Address 2").grid(row = 4, column = 0, sticky = W, padx = 10)
cityLabel = Label(root, text = "City").grid(row = 5, column = 0, sticky = W, padx = 10)
stateLabel = Label(root, text = "State").grid(row = 6, column = 0, sticky = W, padx = 10)
zipcodeLabel = Label(root, text = "Zipcode").grid(row = 7, column = 0, sticky = W, padx = 10)
countryLabel = Label(root, text = "Country").grid(row = 8, column = 0, sticky = W, padx = 10)
phoneLabel = Label(root, text = "Phone Number").grid(row = 9, column = 0, sticky = W, padx = 10)
emailLabel = Label(root, text = "Email Address").grid(row = 10, column = 0, sticky = W, padx = 10)
usernameLabel = Label(root, text = "Username").grid(row = 11, column = 0, sticky = W, padx = 10)
paymentMethodLabel = Label(root, text = "Payment Method").grid(row = 12, column = 0, sticky = W, padx = 10)
discountCodeLabel = Label(root, text = "Discount Code").grid(row = 13, column = 0, sticky = W, padx = 10)
pricePaidLabel = Label(root, text = "Price Paid").grid(row = 14, column = 0, sticky = W, padx = 10)

#Create Entry Boxes
firstNameBox = Entry(root)
firstNameBox.grid(row = 1, column = 1)
firstNameBox.focus()

lastNameBox = Entry(root)
lastNameBox.grid(row = 2, column = 1, pady = 5)

address1Box = Entry(root)
address1Box.grid(row = 3, column = 1, pady = 5)

address2Box = Entry(root)
address2Box.grid(row = 4, column = 1, pady = 5)

cityBox = Entry(root)
cityBox.grid(row = 5, column = 1, pady = 5)

stateBox = Entry(root)
stateBox.grid(row = 6, column = 1, pady = 5)

zipcodeBox = Entry(root)
zipcodeBox.grid(row = 7, column = 1, pady = 5)

countryBox = Entry(root)
countryBox.grid(row = 8, column = 1, pady = 5)

phoneBox = Entry(root)
phoneBox.grid(row = 9, column = 1, pady = 5)

emailBox = Entry(root)
emailBox.grid(row = 10, column = 1, pady = 5)

usernameBox = Entry(root)
usernameBox.grid(row = 11, column = 1, pady = 5)

paymentMethodBox = Entry(root)
paymentMethodBox.grid(row = 12, column = 1, pady = 5)

discountCodeBox = Entry(root)
discountCodeBox.grid(row = 13, column = 1, pady = 5)

pricePaidBox = Entry(root)
pricePaidBox.grid(row = 14, column = 1, pady = 5)

#Create Buttons
addCustomerButton = Button(root, text = "Add Customer To Database", command = addCustomer)
addCustomerButton.grid(row = 15, column = 0, padx = 10, pady = 10)
clearFieldsButton = Button(root, text = "Clear Fields", command = clearFields)
clearFieldsButton.grid(row = 15, column = 1)



root.mainloop()