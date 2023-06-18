import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root123",
  database='ms'
)

mycursor = mydb.cursor(buffered=True)

def save_data(name,address,contactnum,pending,clusternum):
  print(f"INSERT INTO CUSTOMERS (name,address,contactnum,pending,clusternum) VALUES ('{name}','{address}',{contactnum},{pending},{clusternum});")
  mycursor.execute(f"INSERT INTO CUSTOMERS (name,address,contactnum,pending,clusternum) VALUES (%s,%s,%s,%s,%s);",(name,address,contactnum,pending,clusternum))
  mydb.commit()

def fetch_data():
  mycursor.execute("SELECT * FROM CUSTOMERS;")
  return mycursor.fetchall()

