import MySQLdb
import pickle

db = MySQLdb.connect("localhost","root","9266","HelpDesk" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * from Outlook")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

dataset = []
for row in data:
    dataset.append((row[0], "Outlook"))
    
cursor.execute("SELECT * from Adobe")
# Fetch a single row using fetchone() method.
data = cursor.fetchall()
  
for row in data:
    dataset.append((row[0], "Adobe"))

fileout = open("dataset.pickle","wb")
pickle.dump(dataset,fileout)
fileout.close()



# disconnect from server
db.close()
