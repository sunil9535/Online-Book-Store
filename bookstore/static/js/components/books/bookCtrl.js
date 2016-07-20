angular.module("bookStore").controller("booksCtrl", ['$scope','$rootScope','BookService',
	'$routeParams','CartService','$sce','$compile','WishlistService',
	function($scope, $rootScope, BookService, $routeParams,CartService,$sce,$compile,WishlistService){
	
	$scope.ratings = []
	$scope.avgRatings = [false,false,false,false,false]

	var calculateRatings = function(){
		var avg =0;
		var total =10;
		if($scope.ratings.length>0){
			$scope.ratings.forEach( function(element, index) {
				avg+=element.Score
			});

			avg = parseInt(avg/$scope.ratings.length)
		}
		for(i=0;i<avg;i++){
			$scope.avgRatings[i] = true
		}
	}


	var initBookInfo = function(){
		BookService.getBookInfo({'isbn':$scope.isbn}).then(function(res){
			$scope.book = res.data.bookData.book;
			$scope.ratings = res.data.bookData.ratings
			calculateRatings()
		})
	}

	
	var initBookList = function(){
		BookService.getBookBycategory([parseInt($routeParams.categoryid),$routeParams.categoryName]).then(function(res){
			$scope.bookList = res.data.books;
		})
	}

	$scope.getDescr= function(row){
		return $sce.trustAsHtml(row);
	}

	var init= function(){
		if($routeParams.isbn){
			$scope.isbn = $routeParams.isbn
			
			initBookInfo()
		}
		else{
			initBookList()
		}
		
	}

	
	$scope.getImageLocation= function(location){
		return decodeURIComponent(location)
	}
	$scope.addItemToCart= function(book){
		var data ={'operationType':'add','item':{"isbn":book.isbn, "price":book.price, "quantity":1}}
		CartService.addItemToCart(data).then(function(res){
			data = res;
			$rootScope.$broadcast("refreshCart")
		})
		
	}
	
	$scope.addToWishlist = function(book){
		WishlistService.addToWishList({'isbn':isbn}).then(function(res){
			data = res;
			//$rootScope.$broadcast("refreshCart")
		})
	}
	init()

	
}])