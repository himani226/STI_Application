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
                    $.each(pillar,function(index,value){
                        var checkbox_label = value["pillar_title"];
                        var checkbox_id = value["id"];
                        var checkbox_value =value["pillar_title"];
                        var checkbox_name = value["pillar_title"];
                        var template = '<div class="col-lg-9 col-md-9">'+ checkbox_label + '</div> <div class="col-lg-3 col-md-3"> <input type="checkbox" id="'+checkbox_id+'" name="'+checkbox_name+'" value="'+checkbox_value+'" class ="test1" > </div>';

                        if (value["stage_title"] == "STI Education")
                        {
                              append.style.display = "flex";
                              $("#append").append(template);
                              $("#append1").empty();
                              $("#append2").empty();
                        }
                        else if (value["stage_title"] == "Research"){
                            $("#append").empty();
                            append1.style.display = "flex";
                            $("#append1").append(template);
                            $("#append2").empty();
                        }

                        else if (value["stage_title"] == "Innovation and Commercialization"){
                            $("#append").empty();
                            $("#append1").empty();
                            append2.style.display = "flex";
                            $("#append2").append(template);

                        }
                        else {
                             $("#append").empty();
                             $("#append1").empty();
                             $("#append2").empty();
                        }
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
                                    $.each(indicators,function(index,value){
                                        var indicator_label = value["indicator_title"];
                                        var indicator_id = value["id"];
                                        var template = '<div class="col-lg-12 col-md-12" id="'+ indicator_id +'">'+ indicator_label + '</div> <div class="col-lg-12 col-md-12"> </div>';
                                        $("#indicator1").show();



                                    })
                                }
                            })
                            $('input.test1').not(this).prop('checked', false);
                        });
                    })
                }
            })
        $('input.test').not(this).prop('checked', false);
    });
})