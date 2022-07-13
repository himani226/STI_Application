$(document).ready(function(){
    var HOST = window.location.origin;

    $('input.test').on('change', function() {
        event.stopPropagation()
            var check = $(this);
            var name = parseInt($(this).attr('name'));
            $.ajax({
                type: "GET",
                url: HOST+'/indicatorslist/',
                data: {
                    'name': name
                },
                success: function(context){
                   // process on data
                    $.each(pillar,function(index,value){
                        var checkbox_label = value;
                        var checkbox_value =value;
                        var checkbox_name = value;
                        var template = '<input type="checkbox" name="'+checkbox_name+'" value="'+checkbox_value+'">'+checkbox_label;

                      $("#append").append(template);
                    });
                }
            })
        $('input.test').not(this).prop('checked', false);
    });

    $('input.test1').on('change', function() {
        $('input.test1').not(this).prop('checked', false);
    });
})