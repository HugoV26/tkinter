from tkinter import *
from PIL import ImageTk, Image
import psycopg2

root = Tk()
root.title('Tu nerd')
root.geometry("400x400")

conn = psycopg2.connect(
    host = "localhost",
    database = "tkinter",
    user = "hugo",
    password = "hola123,"
)

#print(conn)

#Create a cursor and initialize it

myCursor = conn.cursor()

#Create database
#myCursor.execute("CREATE DATABASE codemy WITH OWNER hugo")

#Create a table

command = ("""CREATE TABLE customers (
    user_id SERIAL PRIMARY KEY, 
    first_name VARCHAR (255), 
    last_name VARCHAR (255), 
    zipcode INT, 
    price_paid NUMERIC(10, 2))""")


#myCursor.execute(command)


# Show table

#myCursor.execute("SELECT * FROM customers")
#print(myCursor.description)
root.mainloop()