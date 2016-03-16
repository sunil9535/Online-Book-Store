'''
Created on 11-Mar-2016

@author: parkar_s
'''
from flask import Flask, redirect, render_template
from flask.blueprints import Blueprint
from .src.book import book_manager
app= Flask(__name__)
bookstore= Blueprint("bookstore",__name__)

@app.route("/")
def index():
    return render_template("index.html")



app.register_blueprint(bookstore)
app.register_blueprint(book_manager)