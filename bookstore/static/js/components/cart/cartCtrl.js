angular.module("bookStore").controller("cartCtrl", ['$scope','CartService','$routeParams',function($scope, BookService, $routeParams){
	var init= function(){
		BookService.getBookBycategory(parseInt($routeParams.categoryid)).then(function(res){
			$scope.bookList = res.data.books;
		})
	}
	$scope.getImageLocation= function(location){
		return decodeURIComponent(location)
	}
	
	init()
}])