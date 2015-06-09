exerciseApp.controller('exercisesController', function ($scope, $http) {

     $scope.exerciseList =
    	$http.get('/api/exercises')
        .then(function(data) {
            $scope.exerciseList = data.data;
		    console.log($scope.exerciseList);
        });

    $scope.currentWorkoutView = [
    	{'name':'Pull-Up','guide':'do some pullups'},
    	{'name':'Push-Up','guide':'do some pushups'},    	
    ];

    $scope.addExerciseToWorkout = function (item) {
        if (item    )
    	$scope.currentWorkoutView.push(item);
        //need to handle reapeats.
    };

    $scope.removeExerciseFromWorkout = function(view) {
    	$scope.currentWorkoutView.splice(view, 1)
    };

});

exerciseApp.run(function($rootScope, $log){
	$rootScope.$log = $log;
});