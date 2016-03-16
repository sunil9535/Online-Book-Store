'''
Created on 14-Mar-2016

@author: parkar_s
'''

from flask_restful import Resource
from bookstore.src.Database.DBConnection import DBConnect

from contextlib import closing
from ..models.core.business.books.BookRepository import BookRepository
from bookstore.src.dao.BookDao import BookDao
from flask import jsonify

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
                return BookRepository(book_list= book_list)
        except Exception as e:
            print("popular_book_api",e )
        
class PopularBookApi(Resource):
    '''
    classdocs
    '''
    def __init__(self):
        self.connection = DBConnect().get_connection()
        self.connection.autocommit(True)
    def get(self):
        try:
            return jsonify({"books":dao.get_popular_books(),"type":"popular"})
        except Exception as e:
            print("popular_book_api",e )