
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
						$scope.navigationList.submenu[1].submenu = categories;
					}
					
					var init = function() {
						$scope.populateNavigationList([ {
							"name" : "dfg",
							"submenu" : [ {
								"name" : "kjsd",
								"submenu" : []
							} ]
						}, {
							"name" : "asdas",
							"submenu" : [ {
								"name" : "ads",
								"submenu" : []
							} ]
						}, {
							"name" : "uio",
							"submenu" : [ {
								"name" : "kgjjsd",
								"submenu" : []
							} ]
						}, {
							"name" : "vbn",
							"submenu" : [ {
								"name" : "vbnbvn",
								"submenu" : []
							} ]
						}, {
							"name" : "aertvb",
							"submenu" : [ {
								"name" : "mhgz",
								"submenu" : []
							} ]
						}, {
							"name" : "tyreaws",
							"submenu" : [ {
								"name" : "xcvf",
								"submenu" : []
							} ]
						}, {
							"name" : "werv",
							"submenu" : [ {
								"name" : "mlkjiyu",
								"submenu" : []
							} ]
						} ])
						CategoryService.getAllCategories().then(function(res){
							console.log(res)
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
