exerciseApp.controller('exercisesController', function($http) {

	console.log('exercises controller working');

	$http.get('/api/exercises')
		.then(function(data) {
			console.log(data)
		})

});