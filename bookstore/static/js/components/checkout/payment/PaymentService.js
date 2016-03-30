angular.module("bookStore").service("PaymentService",function($q, $http, DataService){
	endPoint="books"
		dataService= DataService
	
	this.pay =  function(){
		
		var deferred = $q.defer();
		return dataService.pay().then(function(response){
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
