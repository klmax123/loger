from flask import Flask
import sqlite3
app = Flask(__name__)

@app.route("/insert")
def main():
    connect = sqlite3.connect("db.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Loger (type, message, date, time, url) VALUES (?, ?, ?, ?, ?)", (1, "test", "2020-12-05", "11:11:11", "/ures/add"))
    connect.commit()
    return ""



app.run()