/**
 * 
 */
angular.module("bookStore").factory("DataService",function($q, $http){
	endPoint="books"
	/*
	 	@param offset: page number: for example if offset is 0 records fetched will be 0 - 4 ,if offset is 1 records fetched will be 5- 9
	 	@return: promise for api 
	 	@description :this method will get the records from audit log according to the offset
	 	
	 */
	var getPopularBooks =  function(){
		return $http.get(config.baseUrl+ 'books/getPopularBooks',{headers: {'Content-Type': 'application/json'}});
	}
	
	
	/*
 	@param offset: page number: for example if offset is 0 records fetched will be 0 - 4 ,if offset is 1 records fetched will be 5- 9
 	@return: promise for api 
 	@description :this method will get the records from audit log according to the offset
 	
	 */
	var getAllCategories =  function(){
		return $http.get(config.baseUrl+ 'categories/getallCategories',{headers: {'Content-Type': 'application/json'}});
	}
	
	/*
 	@param offset: page number: for example if offset is 0 records fetched will be 0 - 4 ,if offset is 1 records fetched will be 5- 9
 	@return: promise for api 
 	@description :this method will get the records from audit log according to the offset
 	
	 */
	var getBooksByCategory =  function(category){
		return $http.post(config.baseUrl+ 'books/getBooksByCategory',angular.toJson(category),{headers: {'Content-Type': 'application/json'}});
	}
	
	/*
 	@param offset: page number: for example if offset is 0 records fetched will be 0 - 4 ,if offset is 1 records fetched will be 5- 9
 	@return: promise for api 
 	@description :this method will get the records from audit log according to the offset
 	
	 */
	var getCartByUser =  function(userId){
		return $http.post(config.baseUrl+ 'cart/getCartByUser',angular.toJson({"userId":userId}),{headers: {'Content-Type': 'application/json'}});
	}
	
	var addItemToCart =  function(data){
		return $http.post(config.baseUrl+ 'cart/addItem',angular.toJson(data),{headers: {'Content-Type': 'application/json'}});
	}
	
	var getCartWithDetails = function(data){
	
		return $http.post(config.baseUrl+ 'cart/getCartDetails',angular.toJson({}),{headers: {'Content-Type': 'application/json'}});
	}
	
	var saveAddress= function(data){
		return $http.post(config.baseUrl+ 'shipment/addAddress',angular.toJson(data),{headers: {'Content-Type': 'application/json'}})
	}
	var pay= function(data){
		return $http.post(config.baseUrl+ 'payment/processPayment',data,{headers: {'Content-Type': 'application/json'}})
	}
	var getOrderDetails = function(){
		return $http.post(config.baseUrl+ 'order/getOrders',{headers: {'Content-Type': 'application/json'}})
	}
	return {
		"getPopularBooks":getPopularBooks,
		"getAllCategories":getAllCategories,
		"getBooksByCategory":getBooksByCategory,
		"getCartByUser":getCartByUser,
		"addItemToCart":addItemToCart,
		"getCartWithDetails":getCartWithDetails,
		"saveAddress":saveAddress,
		"pay":pay,
		"getOrderDetails":getOrderDetails
	}
	
})
