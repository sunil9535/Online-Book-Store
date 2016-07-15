'''
Created on Mar 30, 2016

@author: Dell
'''
from flask_restful import Resource
from flask import request, jsonify
from bookstore.src.order.OrderDao import OrderDao


dao = OrderDao()
class OrderApi(Resource):
    '''
    classdocs
    '''

        
       
    def post(self):
        order_data= dao.get_order_details();
        return jsonify({"pd":pd, "order_id":oi})