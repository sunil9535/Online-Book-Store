angular.module("bookStore").controller('headerCtrl',['$scope',function($scope){
	$scope.toggleSideBar= function(e){
		$("#book-store-container").toggleClass("toggle-sidebar");
	}
}])