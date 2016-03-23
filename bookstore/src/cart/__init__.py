from flask.blueprints import Blueprint
from flask_restful import Api
from .CartApi import CartApi

cart_manager = Blueprint("cart", __name__)
api = Api(cart_manager)

api.add_resource(CartApi,"/api/v1.0/cart/getCartByUser")