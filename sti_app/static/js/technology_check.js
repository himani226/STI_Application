$(document).ready(function(){
    var HOST = window.location.origin;

    $('a').on('click', function() {
        event.stopPropagation()
            var check = $(this);
            var name = $(this).attr('name');

            $.ajax({
                type: "GET",
                url: HOST+'/techlist/',
                data: {
                    'name': name
                },
                success: function(context){
                   // process on data
                   console.log("here");
                   var data = JSON.parse(context);
                   all_tech_name = data["all_tech_name"];

                   technology_area.style.display = "block";
                   //heading_table.style.display = "block";
                   $("#tbody").empty();
                    $.each(all_tech_name,function(index,value){
                        var technology_name = value["technology_name"];
                        var inventor_detail = value["inventor_detail"];
                        var institute =value["institute"];
                        var technology_abstract = value["technology_abstract"];
                        var technology_status = value["technology_status"];
                        var technology_transferred = value["technology_transferred"];
                        var template = '<tr style="font-size:14px;"><td>'+technology_name +'</td><td>'+inventor_detail +'</td><td>'+institute +'</td><td>'+technology_abstract +'</td><td>'+technology_status +'</td><td>'+technology_transferred +'</td></tr>';

                           // technology_area.style.display = "block";
                             $("#tbody").append(template);

                    });
                }
            });
        });
})
