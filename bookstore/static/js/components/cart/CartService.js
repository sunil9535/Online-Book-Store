angular.module("bookStore").service("CartService",function($q, $http, DataService){
	endPoint="books"
		dataService= DataService
		cart = {}
	/*
	 	@param offset: page number: for example if offset is 0 records fetched will be 0 - 4 ,if offset is 1 records fetched will be 5- 9
	 	@return: promise for api 
	 	@description :this method will get the records from audit log according to the offset
	 	
	 */
	this.getCartByUser =  function(userId){
		var deferred = $q.defer();
		dataService.getCartByUser(userId).then(function(response){
			if(response){
				deferred.resolve(response);
			}
			else {
				deferred.reject;
			}
		});
		return deferred.promise;
	}
	
	this.addItemToCart = function(item){
		var deferred = $q.defer();
		dataService.addItemToCart({"cart_id":this.cart.cart_id ,"item":item}).then(function(response){
			bookRepository = response.data;
			if(response){
				deferred.resolve(response);
			}
			else {
				deferred.reject;
			}
		});
		return deferred.promise;
	}
	this.getCartWithDetails = function(item){
		var deferred = $q.defer();
		dataService.getCartWithDetails().then(function(response){
			if(response){
				deferred.resolve(response);
			}
			else {
				deferred.reject;
			}
		});
		return deferred.promise;
	}
	
	

})
