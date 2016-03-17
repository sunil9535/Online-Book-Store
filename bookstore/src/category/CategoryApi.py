'''
Created on 17-Mar-2016

@author: parkar_s
'''
from flask_restful import Resource
from bookstore.src.Database.DBConnection import DBConnect


from flask import jsonify, request
from bookstore.src.category.dao.CategoryDao import CategoryDao

dao= CategoryDao()
class CategoryApi(Resource):
    '''
    classdocs
    '''
   

    def get(self):
        
        try:
            return jsonify({"books":dao.get_books_by_id(request.get_json()['cat_id'])})
        except Exception as e:
            print("CategoryApi",e )
            
class AllCategoryApi(Resource):
    

    def get(self):
        
        try:
            return jsonify({"categoryList":dao.get_all_categories()})
        except Exception as e:
            print("AllCategoryApi",e )
        