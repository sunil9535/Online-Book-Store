angular.module("bookStore").controller("booksCtrl", ['$scope','$rootScope','BookService','$routeParams','CartService',function($scope, $rootScope, BookService, $routeParams,CartService){
	var init= function(){
		BookService.getBookBycategory(parseInt($routeParams.categoryid)).then(function(res){
			$scope.bookList = res.data.books;
		})
	}
	$scope.getImageLocation= function(location){
		return decodeURIComponent(location)
	}
	$scope.addItemToCart= function(book){
		var data ={"isbn":book.isbn, "price":book.price, "quantity":1}
		CartService.addItemToCart(data).then(function(res){
			data = res;
		})
		$rootScope.$broadcast("refreshCart")
	}
	init()
}])