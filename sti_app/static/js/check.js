$(document).ready(function(){
    var HOST = window.location.origin;

    $('input.test').on('change', function() {
        event.stopPropagation()
            var check = $(this);
            var name = $(this).attr('name');
            $.ajax({
                type: "GET",
                url: HOST+'/pillarlist/',
                data: {
                    'name': name
                },
                success: function(context){
                   // process on data
                   var data = JSON.parse(context);
                   pillar = data["pillar"];
                   $("#append").empty();
                   $("#indicator1").empty();
                   $("#indicator2").empty();
                   indicator2.style.display = "none";
                    $.each(pillar,function(index,value){
                        var checkbox_label = value["pillar_title"];
                        var checkbox_id = value["id"];
                        var checkbox_value =value["pillar_title"];
                        var checkbox_name = value["pillar_title"];
                        var template = '<div class="col-lg-9 col-md-9">'+ checkbox_label + '</div> <div class="col-lg-3 col-md-3"> <input type="checkbox" id="'+checkbox_id+'" name="'+checkbox_name+'" value="'+checkbox_value+'" class ="test1" > </div>';
                            $("#append").append(template);
                    });
                    $('input.test1').on('change', function() {
                        event.stopPropagation()
                        var check = $(this);
                        var id = $(this).attr('id');

                        $.ajax({
                            type: "GET",
                            url: HOST+'/indicatorslist/',
                            data: {
                                'id': id
                            },
                            success: function(context){
                               // process on data
                               var data = JSON.parse(context);
                               indicators = data["indicators"];
                               $("#indicator1").empty();
                               $("#indicator2").empty();
                                $.each(indicators,function(index,value){

                                    var indicator_label = value["indicator_title"];
                                    var indicator_id = value["id"];
                                    var template = '<div class="col-lg-10 col-md-10">'+ indicator_label + '</div> <div class="col-lg-2 col-md-2"> <input type="checkbox" id="'+indicator_id+'" name="'+indicator_label+'" value="'+indicator_label+'" class ="test2" > </div>';
                                    indicator1.style.display = "flex";
                                    $("#indicator1").append(template);
                                });
                    $('input.test2').on('change', function() {
                        event.stopPropagation()
                        var check = $(this);
                        var id = $(this).attr('id');

                        $.ajax({
                            type: "GET",
                            url: HOST+'/indicatorsdef/',
                            data: {
                                'id': id
                            },
                            success: function(context){
                                var data = JSON.parse(context);
                               indi_def= data["indi_def"];
                                $("#indicator2").empty();
                                $.each(indi_def,function(index,value){
                                    var indicator_label = value["indicator_title"];
                                    var indicator_def = value["indicator_description"];
                                    var indicator_image = value["indicator_image"];
                                    var indicator_id = value["id"];
                                    var template = '<div class="col-lg-12 col-md-12 text-center"><strong>'+indicator_label+'</strong></div><div class="col-lg-12 col-md-12">'+indicator_def+'</div><div class="col-lg-12 col-md-12"><img src="/media/'+indicator_image+'"/></div>';
                                    indicator2.style.display = "flex";
                                    $("#indicator2").append(template);
                                });
                            }

                        })
                        $('input.test2').not(this).prop('checked', false);
                        })

                        }
                    })
                    $('input.test1').not(this).prop('checked', false);
                    })
                }
            })
        $('input.test').not(this).prop('checked', false);
    });
})