var exerciseApp = angular.module('exerciseApp', ['ngRoute']);

exerciseApp.config(function ($routeProvider, $httpProvider) { 
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

	$routeProvider
		.when('/', {
			templateUrl: 'static/exercise_customization_database/js/views/todo.html',
			controller: 'todoController'
		})
		.when('/workouts', {
			templateUrl: 'static/exercise_customization_database/js/views/workouts.html',
			controller: 'workoutController'
		})
		.when('/exercises', {
			templateUrl: 'static/exercise_customization_database/js/views/exercises.html',
			controller: 'exercisesController'
		})

});



// $interpolateProvider.startSymbol('[[').endSymbol(']]')
// $resourceProvider.defaults.stripTrailingSlashes = false;