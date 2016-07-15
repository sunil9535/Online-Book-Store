'''
Created on Apr 1, 2016

@author: Dell
'''
from bookstore.src.dao.DataAccessor import DataAccessor
import random,datetime, pymysql
from bookstore.config import userid

class OrderDao(DataAccessor):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        super(OrderDao,self).__init__()
        self.order_id = None
    
    def get_order_details(self):
        query=("select od.isbn "
               "from orders as o "
               "join order_detail as od "
               "on o.order_id = od.order_id "
               "join book_item as bi "
               "on od.item_id = bi.item_id "
               "join shipment as s "
               "on od.shipment_id = s.id where o.login_id ={};").format(userid)
        result= super(OrderDao,self).read(query= query)
    def insert_order_book(self,book_items =[] ):
        
        for item in book_items:
            isbn, available = item['book']['isbn'], item['book']['available']
            query = ("insert into order_book"
                     " (order_id , isbn, copies_ordered)"
                     " values({}, '{}',{})").format(self.order_id, item['book']['isbn'], available)
            try:        
                super(OrderDao,self).read(query= query)  
            except pymysql.err.IntegrityError as e:
                print("duplicate book", isbn)
                pass
        
        
    def insert_into_details(self,book_items =[], shipment_id= 0):
        
        for item in book_items:
            isbn, available = item['book']['isbn'], item['book']['available']
            query = ("insert into order_detail"
                     " (isbn,order_id, item_id, total, discount, shipment_id )"
                     " values('{}',{},'{}',{},{},{})").format(isbn, self.order_id,item['item_id'],  item['total'], 0, shipment_id)
            super(OrderDao,self).read(query= query)    
        
             
    def insert_into_order(self, timestamp= None):
        self.order_id = random.randint(0, 9999999)
        current_dt= datetime.datetime.utcnow()
        query= ("insert into orders"
                " (timestamp, login_id, status)"
                " values ('{}','{}', '{}')").format(current_dt, userid, "Processing payment")
        super(OrderDao,self).read(query= query)
        query =("select LAST_INSERT_ID() as id from orders")
        result= super(OrderDao,self).read(query=query)
        self.order_id= result[0]['id']
        return self.order_id