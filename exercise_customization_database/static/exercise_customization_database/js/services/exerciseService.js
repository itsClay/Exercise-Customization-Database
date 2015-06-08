exerciseApp.service('exerciseHttpService', ['$http', '$scope', 
	function($http, $scope) {
		// Our "get" is in relation to where our indext.html is - so in this case Base.html
		$http.get('api/exercises/')
			.then(function(response) {
				$scope.exerciseJsonResponse = response.data;
			});
	};
]);

