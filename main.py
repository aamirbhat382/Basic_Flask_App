from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os
app = Flask(__name__)

# DataBase C
client = MongoClient("mongodb://127.0.0.1:27017") #host uri
db = client.mymongodb #Select the database
todos = db.todo #Select the collection name

@app.route("/")
def Home():   
   return render_template('index.html')

@app.route("/about")
def About():
    return render_template('about.html')
app.run(debug=True)
