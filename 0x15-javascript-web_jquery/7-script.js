$.ajax({
   url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
   type: "GET",
   dataType: "json",
})
  .done(function(data) {
     $('DIV#character').html(data.name);
  })
  .fail(function(xhr, status, errorthrown) {})
  .always(function(xhr, status){});
