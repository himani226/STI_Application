$('input[type="checkbox"]').change(function(){
  console.log($(this).is(':checked'));
  if($(this).is(':checked')){
    $(this).siblings('input[type="checkbox"]').attr('checked', false);
  }
});