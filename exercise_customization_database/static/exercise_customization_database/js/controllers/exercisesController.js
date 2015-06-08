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

    $scope.addExerciseToWorkout = function (clickEvent) {
    	$scope.currentWorkoutView.push($scope.exerciseList);
    };

    $scope.removeExerciseFromWorkout = function() {
    	$scope.currentWorkoutView.remove(this.element)
    };

});

exerciseApp.run(function($rootScope, $log){
	$rootScope.$log = $log;
});