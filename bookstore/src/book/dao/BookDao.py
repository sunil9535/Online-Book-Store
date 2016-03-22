'''
Created on 14-Mar-2016

@author: parkar_s
'''

from bookstore.src.config import BookConfig
from flask import jsonify
from ...models.core.business.books.BookRepository import BookRepository
from bookstore.src.dao.DataAccessor import DataAccessor

class BookDao(DataAccessor):
    '''
    classdocs
    '''
    __collection__ = "books"

    def __init__(self):
        '''
        Constructor
        '''
        super(BookDao,self).__init__()
        #self.collection = self.database[self.__collection__]
        
    def get_popular_books(self):
        book_list = list()
        try:
            query =( "select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc, category_id,cat.name "
                     "from books"
                     " left join (category as cat left join Category as subcat on cat.cat_id = subcat.parent) "
                     "on books.category_id = cat.cat_id"
                     " where books.ratings<={} and books.ratings> {};").format(BookConfig.popular_max_rt, BookConfig.popular_min_rt)
            '''self.collection.aggregate([{"$lookup":{
                "from":"categories",
                "localField":"category_id",
                "foreignField":"_id",
                "as":"category"
                    }
                                                 },
                    {
                     "$out":"booksWithCategory"
                    }
            ]);
            
            cursor = self.database.booksWithCategory.aggregate([{"$lookup":{"from":"ratings","localField":"isbn","foreignField":"isbn", "as":"booksWithratings"}},{"$out":"booksWithRatings"}])
            cursor = self.database.booksWithRatings.find()
            while True:
                try: 
                    
                    book_list.append(cursor.next())
                except StopIteration:
                    break'''
            book_list = super(BookDao,self).read(query= query)
            return book_list
        except Exception as e:
            print(e,"get_popular_books")
            
            
    def get_all_books(self):
        try:
            query =("select books.title ,books.category_id, category.name from books left join category on books.category_id = category.cat_id;")
            book_list = super(BookDao,self).read(query= query)
            return book_list
        except Exception as e:
            print(e,"get_all_books")
            
    def get_books_by_category(self, category_id ):
        try:
            query =("select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, available_copies, price, format, keywords, subject,image_loc,cc.name as childcategory "
                    "from books"
                    " inner join category cc "
                    "on cc.cat_id = books.category_id "
                    "where cc.parent={};").format(category_id)
            book_list = super(BookDao,self).read(query= query)
            return book_list
        except Exception as e:
            print(e,"get_all_books")

        