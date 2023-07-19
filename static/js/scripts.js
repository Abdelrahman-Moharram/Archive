  function ChangeFar3y(id){
    var select = document.getElementById('tamam_asasy_'+id).value
    $.ajax({
      url:'get_far3y/'+select+"/",
      type:'GET',
      success: function(data){
        let far3y_select = document.getElementById("tamam_far3y_"+id)
        data.tamam_far3y.forEach(t => {
          var option = document.createElement("option")
          option.innerText = t.name;
          option.value = t.id
          far3y_select.appendChild(option)
        });
      },
      error: function(errs){
        console.log("errors=>", errs);
      }
    })
  }