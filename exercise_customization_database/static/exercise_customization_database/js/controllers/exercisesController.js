exerciseApp.controller('exercisesController', function ($scope, $http) {

    $http.get('/api/exercises')
        .then(function(data) {
            $scope.exerciseList = data.data;
		    console.log($scope.exerciseList);
        });
});