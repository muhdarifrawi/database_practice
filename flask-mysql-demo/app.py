from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='password',
        database='chinook'
        )
        
    employeeCursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = "SELECT * FROM Employee"
    employeeCursor.execute(sql)
   
    
    albumCursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = "SELECT * FROM Album"
    albumCursor.execute(sql)
    return render_template("index.template.html", albumResults=albumCursor, employeeResults=employeeCursor)
        

#"magic code" - - boilerplate
if __name__ == "__main__":
   app.run(host=os.environ.get("IP"),
      port=int(os.environ.get("PORT")),
      debug=True)