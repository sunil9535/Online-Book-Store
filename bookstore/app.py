'''
Created on 11-Mar-2016

@author: parkar_s
'''
from flask import Flask, redirect, render_template
from flask.blueprints import Blueprint
from .src.book import book_manager
from .src.category import category
from bookstore.src.cart import cart_manager
from bookstore.src.payment import payment
from bookstore.src.shipment import shipment
app= Flask(__name__)
bookstore= Blueprint("bookstore",__name__)

@app.route("/")
def index():
    return render_template("index.html")



app.register_blueprint(bookstore)
app.register_blueprint(book_manager)
app.register_blueprint(category)
app.register_blueprint(cart_manager)
app.register_blueprint(payment)
app.register_blueprint(shipment)