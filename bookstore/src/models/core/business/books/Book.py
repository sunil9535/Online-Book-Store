'''
Created on 14-Mar-2016

@author: parkar_s
'''
from bookstore.src.models.core.business.category.ParentCategory import Category

class Book(object):
    '''
    classdocs
    '''


    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        cat= Category()
        for key,val in kwargs.items():
            if key =="sub_cat_id" or key=="category_id" or key=="sub_name" or key =="name":
                cat[key]= val   
            else:
                setattr(self, key, val)
            self.category = cat
    
