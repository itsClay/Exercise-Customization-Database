exerciseApp.controller('exercisesController', function ($scope, $http) {

    $http.get('/api/exercises')
        .then(function(data) {
            $scope.exerciseList = data.data;
		    console.log($scope.exerciseList);
        });

    $scope.currentWorkoutView = [
    	{'name':'Pull-Up','guide':'do some pullups'}
    ];

    $scope.addExerciseToWorkout = function () {
    	$scope.currentWorkoutView.push($scope.exerciseList);
    };

    $scope.removeExerciseFromWorkout = function() {
    	$scope.currentWorkoutView.remove(exerciseList)
    };

});