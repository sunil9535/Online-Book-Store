'''
Created on Mar 30, 2016

@author: Dell
'''
from flask_restful import Resource
from flask import request
from bookstore.src.payment.dao.PaymentDao import PaymentDao

dao = PaymentDao()
class PaymentApi(Resource):
    '''
    classdocs
    '''

        
       
    def post(self):
        dao.process_payment(request.json) 