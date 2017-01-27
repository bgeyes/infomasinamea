(function() {
	'use strict';

	angular.module('home.demo', [])
		.controller('HomeController', 
			['$scope', '$http', HomeController]);

		function HomeController($scope, $http) {
			$scope.add = function(list, new_model) {
				var card = {
					make_id: list.id,
					model_name: new_model,
				};
				$http.post('/model/', card)
					.then(function(response){
						list.model.push(response.data);
					},
					function(){
						alert('Could not create new model');
					});
			};

			/*$scope.add_review = function(review, new_review){
				var card = {
					review: new_review,
					model_id: review.id
				};
				$http.post('/review/', card)
					.then(function(response){
						list.model.review.push(response.data);
					},
					function(){
						alert('Could not add new review');
					});
			};*/

			$scope.data = [];
			$http.get('/make/').then(function(response){
				$scope.data = response.data;
			});
		}
}());