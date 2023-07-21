function ChangeFar3y(id){
    flag = false
    var select = document.getElementById('tamam_asasy_'+id).value
    $.ajax({
      url:'get_far3y/'+select+"/",
      type:'GET',
      success: function(data){
        let far3y_select = document.getElementById("tamam_far3y_"+id)
        far3y_select.innerHTML = '<option value=""></option>';
        data.tamam_far3y.forEach(t => {
          var option = document.createElement("option")
          option.innerText = t.name;
          option.value = t.id
          far3y_select.appendChild(option)
        });
      },
      error: function(errs){
        console.error("errors=>", errs);
      }
    })
  }

  function addOptions( fromId, toId ) {
    var fromEl = document.getElementById( fromId ),
        toEl = document.getElementById( toId );

    if ( fromEl.selectedIndex >= 0 ) {
        var index = toEl.options.length;

        for ( var i = 0; i < fromEl.options.length; i++ ) {
            if ( fromEl.options[ i ].selected ) {
                toEl.options[ index ] = fromEl.options[ i ];
                i--;
                index++
            }
        }
    }
}