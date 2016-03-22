angular.module("bookStore").controller("booksCtrl", ['$scope','BookService','$routeParams',function($scope, BookService, $routeParams){
	var init= function(){
		BookService.getBookBycategory($routeParams.categoryid).then(function(res){
			$scope.bookList = res.data.books;
		})
	}
	$scope.getImageLocation= function(location){
		return decodeURIComponent(location)
	}
	
	init()
}])