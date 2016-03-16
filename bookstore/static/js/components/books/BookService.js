angular.module("bookStore").service("BookService",function($q, $http, DataService){
	endPoint="books"
		dataService= DataService
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
	


})
