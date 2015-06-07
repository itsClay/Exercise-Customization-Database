exerciseApp.controller('exercisesController', function ($scope, $http) {

	var exerciseList;

    $http.get('/api/exercises')
        .then(function(data) {
            $scope.exerciseList = data;
          

        });
    console.log(exerciseList);

	// $http.get('/api/exercises')
	// 	.then(function(response) {
	// 		$scope.exerciseList = response.data;
	// 			console.log($scope.exerciseList)
	// 	});

	// console.log($scope.exerciseList)

	// console.log(exerciseList.data)
	// console.log(exerciseList.name)
});