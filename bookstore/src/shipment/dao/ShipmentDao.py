'''
Created on Mar 30, 2016

@author: Dell
'''
from bookstore.src.dao.DataAccessor import DataAccessor

class ShipmentDao(DataAccessor):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(ShipmentDao,self).__init__()
        
    def add_user_addr(self, address):
        try:
            qry = ("insert into address(country, state, city, zipcode, street, building, room_no) "
            "values('{}', '{}', '{}', {}, '{}', '{}', {})").format(address['country'], address['state'], address['city'], int(address['zipcode']), address['street'], address['building'], int(address['room_no']))
            qry_c = """select LAST_INSERT_ID() as id from address"""
            super(ShipmentDao,self).read(query= qry)
            address_id= super(ShipmentDao,self).read(query= qry_c)
            qry_update = ("""update customer set address = {}""").format(address_id[0]['id'])
            super(ShipmentDao,self).read(query=qry_update)
            return address_id[0]['id']
        except Exception as e:
            pass    
            
            
            
            
            
            