from flask.blueprints import Blueprint
from flask_restful import Api
from .BookApi import BookApi, PopularBookApi
from bookstore.src.book.BookApi import BookByCategoryApi

book_manager = Blueprint("books", __name__)
api= Api(book_manager)

api.add_resource(BookApi,"/api/v1.0/books/getAllBooks")
api.add_resource(PopularBookApi,"/api/v1.0/books/getPopularBooks")
api.add_resource(BookByCategoryApi,"/api/v1.0/books/getBooksByCategory")    