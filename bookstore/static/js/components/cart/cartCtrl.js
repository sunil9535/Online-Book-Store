angular.module("bookStore").controller("cartCtrl", ['$scope','CartService','$routeParams',function($scope, CartService, $routeParams){
	var init= function(){
		CartService.getCartWithDetails().then(function(res){
			$scope.cartData = res.data.cart
		})
	}
	$scope.getImageLocation= function(location){
		return decodeURIComponent(location)
	}
	
	init()
}])