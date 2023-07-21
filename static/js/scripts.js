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
    var fromEl = document.getElementById( fromId );
    var toEl = document.getElementById( toId );
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

let Nadafa = document.getElementById("Nadafa-Form")
Nadafa.addEventListener("submit", (e)=>{
  let ids = []
  let qs = []
  e.preventDefault();
  uIn = document.getElementById("users-in")
  qIn = document.getElementById("qeta3-in")
  for (var i = 0; i < uIn.options.length; i++){
    ids.push(uIn.options[i].value)
  }
  for (var i = 0; i < qIn.options.length; i++){
    qs.push(qIn.options[i].value)
  }
  $.ajax({
      url:'',
      type:'POST',
      data:{
        csrfmiddlewaretoken:document.getElementById("csrf").value,
        users_ids:ids,
        qeta3_ids:qs
      },
      success: function(data){
        // console.log(data);
      },
      error: function(errs){
        console.error("errors=>", errs);
      }
    })
})