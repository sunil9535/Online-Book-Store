'''
Created on 23-Mar-2016

@author: parkar_s
'''
from bookstore.src.dao.DataAccessor import DataAccessor
import uuid
from bookstore.config import userid
from bookstore.src.models.core.business.cart import Cart
from bookstore.src.models.core.business.cart.CartItem import CartItem

class CartDao(DataAccessor):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(CartDao,self).__init__()
        
    def get_cart_by_user(self, userid):
        query = ("select *"
                 " from cart "
                 "join book_item "
                 "on cart.item_id = book_item.item_id "
                 "where user_id= '{}'").format(userid)
        result = super(CartDao,self).read(query= query)
        if len(result) == 0:
            query= ("select * from cart where user_id = '{}'").format(userid)
            result = super(CartDao,self).read(query= query)
            return Cart(cart_id= result[0]['cart_id'], user_id= userid, items=[],total=0.0, count=0)
        count = 0
        cart_items = []
        total= 0.0
        for value in result :
            count+= value['quantity']
            total = total + value['book_item.total']
            cart_items.append(CartItem(isbn=value['ISBN'], quantity= value['quantity'], item_id= value['item_id'], price= value['price'], total= value['book_item.total']))
        return Cart(cart_id= result[0]['cart_id'], user_id= userid, items=cart_items,total=total, count=count)
    
    def add_item__to_cart(self, data):
        book = data['item']
        book_exist_in_item_q= ("select c.item_id, count(*) as count"
                               " from cart as c "
                               "join book_item as bi "
                               "on c.item_id= bi.item_id "
                               "where user_id ='{}' and isbn='{}'").format(userid, book['isbn'])
        c = super(CartDao,self).read(query= book_exist_in_item_q)[0]
            
        if c['count'] > 0: 
            q1= ("update book_item set quantity= quantity+ {} where isbn= '{}'").format(book['quantity'], book['isbn'])
            super(CartDao,self).read(query= q1)
        else :
            item_id = uuid.uuid4().hex[0:6]
            q2= ("insert into book_item values('{}',{},'{}', {}, {})").format(book['isbn'],book['quantity'],item_id,book['price'],book['quantity']*book['price'])
            super(CartDao,self).read(query= q2)

            q3= ("insert into cart values('{}','{}',{}, {}, '{}')").format(data['cart_id'],userid,float(book['quantity']*book['price']), book['quantity'],item_id)
            super(CartDao,self).read(query= q3)
            
    def delete_items_from_cart(self,items= [], delete_all= True, cart_id=None):
        for item in items:
            query= ("delete from cart"
                    " where cart_id= '{}'"
                    " and user_id = '{}'"
                    " and item_id = '{}'").format(cart_id,userid, item['item_id'])
            
            super(CartDao,self).read(query= query)
        query = ("insert into cart (cart_id, user_id, total,item_id) "
                     "values('{}', '{}',{},'{}')").format(cart_id,userid,0.0, "-1")
        super(CartDao,self).read(query= query)
            
        