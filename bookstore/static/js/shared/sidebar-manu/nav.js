
angular.module("bookStore").controller(
		'navCtrl',
		[
				'$scope',
				'SideMenu',
				'CategoryService',
				function($scope, SideMenu, CategoryService) {
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
					$scope.loadBooksByCategory = function(categoryType,
							category) {

					}
					init()

				} ])
.directive("collapseList", function(RecursionHelper) {
	return {
		restrict : 'EA',
		scope : {
			navigationList : "=navigationList"
		},
		templateUrl : "/static/js/shared/sidebar-manu/collapse-list.html",
		compile : function(element) {
			return RecursionHelper.compile(element);
		}
	}
}).controller(
		'collapseListCtrl',
		[ '$scope', 'SideMenu', 'CategoryService',
				function($scope, SideMenu, CategoryService) {

} ])
