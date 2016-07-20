'''
Created on 14-Mar-2016

@author: parkar_s
'''

from flask import jsonify

from bookstore.src.config import BookConfig
from bookstore.src.dao.DataAccessor import DataAccessor

from ...category.CategoryService import CategoryService
from ...models.core.business.books.BookRepository import BookRepository


class BookDao(DataAccessor):
    '''
    classdocs
    '''
    __collection__ = "books"

    def __init__(self):
        '''
        Constructor
        '''
        super(BookDao, self).__init__()
        #self.collection = self.database[self.__collection__]
        self.categoryService = CategoryService()

    def get_popular_books(self):
        book_list = list()
        try:
            query = ("select books.isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc, category_id "
                     "from books"
                     " left join rating"
                     " on rating.isbn = books.isbn"
                     " where rating.score <={} and rating.score> {};").format(BookConfig.popular_max_rt, BookConfig.popular_min_rt)

            book_list = super(BookDao, self).read(query=query)
            return book_list
        except Exception as e:
            print(e, "get_popular_books")

    def get_all_books(self):
        try:
            query = (
                "select books.title ,books.category_id, category.name from books left join category on books.category_id = category.cat_id;")
            book_list = super(BookDao, self).read(query=query)
            return book_list
        except Exception as e:
            print(e, "get_all_books")

    def get_books_by_category(self, category_id):
        categories = self.categoryService.getCategoriesById(category_id)

        print(categories)
        try:
            if len(categories) == 0:
                return []
            query = ("select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc,cc.name as childcategory "
                     "from books"
                     " inner join category cc "
                     "on cc.cat_id = books.category_id "
                     "where cc.cat_id in " + str(tuple(categories)))
            book_list = super(BookDao, self).read(query=query)
            return book_list
        except Exception as e:
            print(e, "get_all_books")

    def getBookInfo(self, isbn):
        query = ("select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, "
                 "available_copies, price, format, keywords, subject,image_loc,description from books as b"
                 " left join category as c on b.Category_id = c.cat_id where b.ISBN='{}'").format(isbn)
        queryR = ("select * from rating where ISBN='{}'").format(isbn)
        result = super(BookDao, self).read(query=query)
        ratingResult = super(BookDao, self).read(query=queryR)
        return {'book': result[0], 'ratings': ratingResult}
