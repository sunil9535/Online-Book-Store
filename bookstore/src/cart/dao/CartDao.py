'''
Created on 23-Mar-2016

@author: parkar_s
'''
from bookstore.src.dao.DataAccessor import DataAccessor

class CartDao(DataAccessor):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        super(CartDao,self).__init__()
        
    def get_cart_by_user(self, userid):
        query = ("select cart_id, item_id,user_id, total, SUM(count) as count from cart where user_id = {}").format(userid)
        cart = super(CartDao,self).read(query= query)
        return cart