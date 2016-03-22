
angular.module("bookStore").controller('navCtrl',['$scope','SideMenu','CategoryService',function($scope, SideMenu, CategoryService) {
	$scope.navigationList = []
	
	$scope.populateNavigationList = function(categories) {
		$scope.navigationList = SideMenu;
	}
	
	var populateCategories= function(list){
		$scope.navigationList.submenu[1].submenu = list
	}
	
	var init = function() {
		$scope.populateNavigationList()
		CategoryService.getAllCategories().then(function(res){
				populateCategories(res.data.categoryList)
		})
	}
	$scope.filterByCategory= function(event, index, category){
		arr= {"cat_id":category.id , sub_cat_ids:[] }
		angular.forEach(category.submenu,function(value, key){ 
			arr.sub_cat_ids.push(value.id)
		})
		BookService.getBookBycategory(arr).then(function(res){
			$location.path("/store/books/byCategory/"+arr.cat_id)
		})
}
	init()

}])
.directive("collapseList", function(RecursionHelper) {
	return {
		restrict : 'EA',
		scope : {
			navigationList : "=navigationList"
		},
		templateUrl : "/static/js/shared/sidebar-manu/collapse-list.html",
		compile : function(element) {
			return RecursionHelper.compile(element);
		},
		controller:"collapseListCtrl"
	}
}).controller('collapseListCtrl',[ '$scope', 'SideMenu', 'BookService','$location',function($scope, SideMenu, BookService, $location) {
	
	$scope.filterByCategory= function(event, index, category){
		arr= {"cat_id":category.id , sub_cat_ids:[] }
		angular.forEach(category.submenu,function(value, key){ 
			arr.sub_cat_ids.push(value.id)
		})
		$location.path("/store/books/category/"+arr.cat_id)
	}
	
} ])
