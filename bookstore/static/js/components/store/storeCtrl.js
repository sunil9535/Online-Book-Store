angular.module("bookStore").controller("storeCtrl",['$scope','BookService',function($scope,BookService){
	$scope.interval = 2000;
	var init= function(){
		BookService.getPopularBooks().then(function(res){
			$scope.popularBooks = res.data.books;
		});
		
	}
	init();
	
}])