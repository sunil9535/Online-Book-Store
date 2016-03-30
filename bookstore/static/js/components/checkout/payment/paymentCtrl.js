angular.module("bookStore").controller("paymentCtrl", ['$scope','PaymentService','$routeParams','CartService',function($scope, PaymentService, $routeParams, CartService){
	var init= function(){
		$scope.cardValidator = /^(?:3[47][0-9]{13})$/; 
		$scope.payment = {
			"total":CartService.cart.total.toFixed(2)
		}
		$('#my-modal').modal({
		    show: 'false'
		});
	}
	$scope.getImageLocation= function(location){
		return decodeURIComponent(location)
	}
	$scope.pay = function(){
		PaymentService.pay().then(function(){
			$('#my-modal').modal({
			    show: 'true'
			});
		})
	}
	init()
}])