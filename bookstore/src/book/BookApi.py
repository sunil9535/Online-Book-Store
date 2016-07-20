'''
Created on 14-Mar-2016

@author: parkar_s
'''

from contextlib import closing

from flask import jsonify, request
from flask_restful import Resource

from bookstore.src.Database.DBConnection import DBConnect
from bookstore.src.book.dao.BookDao import BookDao

from ..models.core.business.books.BookRepository import BookRepository


dao = BookDao()


class BookApi(Resource):
    '''
    classdocs
    '''

    def get(self):
        try:
            query = """select * from books"""
            with closing(self.connection.cursor()) as cursor:
                cursor.execute(query)
                book_list = cursor.fetchall()
                return BookRepository(book_list=book_list)
        except Exception as e:
            print("popular_book_api", e)


class PopularBookApi(Resource):
    '''
    classdocs
    '''

    def get(self):
        try:
            return jsonify({"books": dao.get_popular_books(), "type": "popular"})
        except Exception as e:
            print("popular_book_api", e)


class BookDescriptionApi(Resource):

    def post(self):
        try:
            bookInfo = dao.getBookInfo(request.json.get('isbn'))
            return jsonify({'status': 'success', 'bookData': bookInfo})
        except Exception:
            return jsonify({'status': 'failed', 'message': 'could not fetch the book info'})


class BookByCategoryApi(Resource):
    '''
    classdocs
    '''

    def post(self):
        try:
            return jsonify({"books": dao.get_books_by_category(request.get_json()), "type": "popular"})
        except Exception as e:
            print("popular_book_api", e)
