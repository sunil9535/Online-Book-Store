angular.module("bookStore").factory("OrderService",
		function($q, $http, DataService) {
			var endPoint = "order"
			var dataService = DataService
			var cart = {}
			var cs = {}

			/*
			 * @param offset: page number: for example if offset is 0 records
			 * fetched will be 0 - 4 ,if offset is 1 records fetched will be 5-
			 * 9 @return: promise for api @description :cs method will get the
			 * records from audit log according to the offset
			 * 
			 */
			cs.getOrderDetails = function() {
				var deferred = $q.defer();
				dataService.getOrderDetails().then(function(response) {
					if (response) {
						deferred.resolve(response);
					} else {
						deferred.reject;
					}
				});
				return deferred.promise;
			}

			

			return cs;

		})
