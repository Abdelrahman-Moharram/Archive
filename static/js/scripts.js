$.ajax({
    url:'get_far3y/',
    type:'GET',
    success: function(data){
      let options = '';
      data.tamam_far3y.forEach(t => {
        options += '<option value='+t.id+'>'+t.name+'</option>'
      });
      console.log(data.tamam_far3y);
      $("#daily_tamam select[name='tamam_asasy']").find('.EmptyValue').after(options);
    },
    error: function(errs){
      console.log("errors=>", errs);
    }
  })