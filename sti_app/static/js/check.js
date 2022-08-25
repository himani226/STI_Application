$(document).ready(function(){
    var HOST = window.location.origin;

    $('input.stage').on('change', function() {
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
                   $("#pillarDiv").empty();
                   $("#indicator1").empty();
                   $("#indicator2").empty();
                   indicator2.style.display = "none";
                    $.each(pillar,function(index,value){
                        var checkbox_label = value["pillar_title"];
                        var checkbox_id = value["id"];
                        var checkbox_value =value["pillar_title"];
                        var checkbox_name = value["pillar_title"];
                        var template = '<div class="col-lg-9 col-md-9">'+ checkbox_label + '</div> <div class="col-lg-3 col-md-3"> <input type="checkbox" id="'+checkbox_id+'" name="'+checkbox_name+'" value="'+checkbox_value+'" class ="pillar" > </div>';
                            $("#pillarDiv").append(template);
                    });
                    $('input.pillar').on('change', function() {
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
                                    var template = '<div class="col-lg-9 col-md-9">'+ indicator_label + '</div> <div class="col-lg-3 col-md-3"> <input type="checkbox" id="'+indicator_id+'" name="'+indicator_label+'" value="'+indicator_label+'" class ="indicator" > </div>';
                                    indicator1.style.display = "flex";
                                    $("#indicator1").append(template);
                                });
                    $('input.indicator').on('change', function() {
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
                                    var indicator_id = value["id"];
                                    var template = '<div class="col-lg-12 col-md-12 text-center"><strong>'+indicator_label+'</strong></div><div class="col-lg-12 col-md-12">'+indicator_def+'</div>';

                                    indicator2.style.display = "flex";
                                    $("#indicator2").append(template);
                                });
                            }

                        })
                        $('input.indicator').not(this).prop('checked', false);
                        })

                        }
                    })
                    $('input.pillar').not(this).prop('checked', false);
                    })
                }
            })
        $('input.stage').not(this).prop('checked', false);
    });

})