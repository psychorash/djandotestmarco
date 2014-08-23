
var productos = new Bloodhound({
 datumTokenizer: function (datum) {
        return Bloodhound.tokenizers.whitespace(datum.value);
    },
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  remote:  {
          url: '../search/json/?id=%QUERY',
          filter: function(data) {
               return $.map(data, function (item) {
               return {
                    value: item.fields.settings_name
               };
            });
        }
        },
});

productos.initialize();

$('#search').typeahead(null, {
  name: 'productos',
  displayKey: 'value',
  source: productos.ttAdapter()
});

