angular.module("bookStore").controller("orderCtrl", ['$scope','OrderService','$routeParams','$location',function($scope, OrderService, $routeParams, $location){
	var init= function(){
		OrderService.getOrderDetails().then(function(res){
			$scope.orders= res.data;
		})
	}
	$scope.getImageLocation= function(location){
		return decodeURIComponent(location)
	}
	
	init()
}])