$('#search').change(function(){
  $.ajax({
    url: "search/json",
    type: "get",
    data: { 'id' :  'pri'},
    success: function(data){
            console.log(data);
        },
  });
});

