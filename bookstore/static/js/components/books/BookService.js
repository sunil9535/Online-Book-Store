angular.module("bookStore").service("BookService",function($q, $http, DataService){
	endPoint="books"
		dataService= DataService
		bookRepository = []
	/*
	 	@param offset: page number: for example if offset is 0 records fetched will be 0 - 4 ,if offset is 1 records fetched will be 5- 9
	 	@return: promise for api 
	 	@description :this method will get the records from audit log according to the offset
	 	
	 */
	this.getPopularBooks =  function(){
		var deferred = $q.defer();
		dataService.getPopularBooks().then(function(response){
			if(response){
				deferred.resolve(response);
			}
			else {
				deferred.reject;
			}
		});
		return deferred.promise;
	}
	
	this.getBookBycategory = function(category){
		var deferred = $q.defer();
		dataService.getBooksByCategory(category).then(function(response){
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
	

	this.getBookInfo = function(params){
		var deferred = $q.defer();
		dataService.getBookInfo(params).then(function(response){
			if(response){
				deferred.resolve(response);
			}
			else {
				deferred.reject;
			}
		});
		return deferred.promise;
	}
	


	this.getBookRepository= function(){
		return this.bookRepository
	}


})
