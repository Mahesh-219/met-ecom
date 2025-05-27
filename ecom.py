
from fastapi import FastAPI, Request
import sqlite3
 
 
def connect_db():
    conn = sqlite3.connect("user1.db")
    return conn
 
app = FastAPI()

@app.get("/user1")
def read_users():
    #1. get conn object
    conn = connect_db()
 
    #2. use cursor menthod
    cursor = conn.cursor()
 
    #3. use execute() and pass SQL as argument
    cursor.execute("SELECT * FROM user1")
 
    #4. use fetchall() to get all records
    data = cursor.fetchall()
 
    conn.close()
 
    output = []
 
    for entry in data:
        output.append({
            "username": entry[1],
            "password": entry[2]
        })
    return data

@app.post("/signup")
def signup(username,password):
    conn=connect_db()
 
    cursor=conn.cursor()
 
    cursor.execute("INSERT INTO users(username,password) VALUES (?,?)",(username,password))
   
    data=cursor.fetchall()
 
    conn.commit()
 
    conn.close()
 
    output=["signup success"]
 
    for entry in data:
        output.append({
            "username": entry[1],
            "password": entry[2]
        })
    return output


@app.post("/user1/login")
def login(username,password):

    conn=connect_db()

    cursor=conn.cursor()

    cursor.execute("SELECT * FROM user1 WHERE username=? AND password=?",(username,password))

    data=cursor.fetchall()

    for entry in data:

        if username == entry[1] and password == entry[2]:

            cursor.execute("UPDATE user1 SET is_login =1 WHERE username =?",(username, ))


        #else:
        # return "login failed"

        conn.commit()

        conn.close()

        return "login successfully"
    

@app.post("/user1/logout")

def logout(username,password):
 
     conn=connect_db()
 
     cursor=conn.cursor()
 
     cursor.execute("SELECT * FROM user1 WHERE username=? AND password=?",(username, password))

     data = cursor.fetchall()

     for entry in data:

         if username == entry[1] and password == entry[2]:

             cursor.execute("UPDATE user1 SET is_login =0 WHERE username =?",(username, ))

     # else:

     #     return "logout failed"

     conn.commit()

     conn.close()

     return "logout successfully"


@app.get("/items")
def read_items():
    #1. get conn object
    conn = connect_db()
 
    #2. use cursor menthod
    cursor = conn.cursor()
 
    #3. use execute() and pass SQL as argument
    cursor.execute("SELECT * FROM items")
 
    #4. use fetchall() to get all records
    data = cursor.fetchall()
 
    conn.close()
 
    output = []
 
    for entry in data:
        output.append({
            "username": entry[1],
            "password": entry[2]
        })
    return data


