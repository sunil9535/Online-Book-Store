angular.module("bookStore").controller("cartCtrl", ['$scope','CartService','$routeParams','$location',function($scope, CartService, $routeParams, $location){
	var init= function(){
		CartService.getCartWithDetails().then(function(res){
			
			$scope.cartData  = CartService.cart =  res.data.cart
		})
	}
	$scope.getImageLocation= function(location){
		return decodeURIComponent(location)
	}
	$scope.checkout = function(){
		$location.path("/checkout/shipment")
	}
	init()
}])