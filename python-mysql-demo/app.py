import pymysql

connection = pymysql.connect(host='localhost',
    user="admin",
    password="password",
    database="chinook"
)

cursor = connection.cursor()
cursor.execute("SELECT * from Employee")
for row in cursor:
    # print (r)
    # We have to refer each field by its index
    #print ("Name: " + row[1] + " " + row[2] + " is a " + row[3])
    print ("Employee ID: {} {} is {}".format(row[1],row[2],row[3]))