angular.module("bookStore").controller("paymentCtrl", ['$scope','PaymentService','CheckoutService','$routeParams','CartService','$uibModal',function($scope, PaymentService,CheckoutService, $routeParams, CartService, $uibModal){
	var init= function(){
		$scope.cardValidator = /^(?:3[47][0-9]{13})$/; 
		$scope.payment = {
			"total":CartService.cart.total.toFixed(2)
		}
		$scope.expMonths = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
		$scope.expYear =[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
		
	}
	$scope.getImageLocation= function(location){
		return decodeURIComponent(location)
	}
	/* $scope.open = function (size, alertMessage ) {

		    var modalInstance = $uibModal.open({
		      templateUrl: '/static/js/modal/modal.html',
		      controller: 'ModalInstanceCtrl',
		      size: size,
		      windowClass: 'center-modal',
		      resolve: {
		        message : function () {
		          return alertMessage;
		        }
		      }
		    });
	 }*/
	$scope.open= function(id, message, header){
		$scope.modal ={
				"id":id,
				"message":message,
				"header":header
		}
		$(id).modal()
	}
	$scope.pay = function(){
		data = {"cart":CartService.cart, "address":CheckoutService.shipment.address, "contact":CheckoutService.shipment.contact}
		PaymentService.pay(data).then(function(res){
			data = res.data
			//$scope.open('small',"Success: Congratulations you have successfully placed an order with us your order id is");
			$scope.open("#myModal","Congratulations! you have successfully placed an order for the following item order id is:"+data.order_id + "\nyour item will be arriving by "+data.pd, "Sucess! Thank you for shopping with us.")
		})
	}
	init()
}])