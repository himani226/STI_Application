$(document).ready(function(){
    var HOST = window.location.origin;

    $('input.test').on('change', function() {
        event.stopPropagation()
            var check = $(this);
            var name = parseInt($(this).attr('name'));
            $.ajax({
                type: "POST",
                url: HOST+'/indicatorslist/',
                data: {
                    'name': name
                },
                success: function(context){
                   // process on data
                   var tr = "Hello"
                    document.write(tr)
                }
            })
        $('input.test').not(this).prop('checked', false);
    });

    $('input.test1').on('change', function() {
        $('input.test1').not(this).prop('checked', false);
    });
})