'''
Created on 15-Mar-2016

@author: parkar_s
'''

class BookRepository(object):
    '''
    classdocs
    '''


    def __init__(self, book_list, category=None, repository_name = "general"):
        '''
        Constructor
        '''
        self.books = book_list
        self.book_category = category
        self.repository_name = repository_name
        
    
        