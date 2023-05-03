$.ajax({
   url: "https://swapi-api.alx-tools.com/api/films/?format=json",
   type: "GET",
   dataType: "json",
})
  .done(function(data) {
     $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
  })
  .fail(function(xhr, status, errorthrown) {})
  .always(function(xhr, status){});
