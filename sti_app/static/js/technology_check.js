$(document).ready(function(){
    var HOST = window.location.origin;

    $('a').on('click', function() {
        event.stopPropagation()
            var check = $(this);
            var name = $(this).attr('name');
            var techDiv1 = document.getElementById("tech-1");
            var techDiv2 = document.getElementById("tech-2");
            var techDiv3 = document.getElementById("tech-3");
            var techDiv4 = document.getElementById("tech-4");
            var techDiv5 = document.getElementById("tech-5");

            if (name == "Agriculture")
            {
                techDiv1.style.backgroundColor = "#dff3ee";
                techDiv2.style.backgroundColor = "#FFFFFF";
                techDiv3.style.backgroundColor = "#FFFFFF";
                techDiv4.style.backgroundColor = "#FFFFFF";
                techDiv5.style.backgroundColor = "#FFFFFF";

            }
            else if (name == "Food Technology")
            {
                techDiv2.style.backgroundColor = "#dff3ee";
                techDiv1.style.backgroundColor = "#FFFFFF";
                techDiv3.style.backgroundColor = "#FFFFFF";
                techDiv4.style.backgroundColor = "#FFFFFF";
                techDiv5.style.backgroundColor = "#FFFFFF";
            }
            else if (name == "Healthcare & Pharmaceuticals")
            {
                techDiv3.style.backgroundColor = "#dff3ee";
                techDiv2.style.backgroundColor = "#FFFFFF";
                techDiv1.style.backgroundColor = "#FFFFFF";
                techDiv4.style.backgroundColor = "#FFFFFF";
                techDiv5.style.backgroundColor = "#FFFFFF";
            }
            else if (name == "Manufacturing")
            {
                techDiv4.style.backgroundColor = "#dff3ee";
                techDiv2.style.backgroundColor = "#FFFFFF";
                techDiv3.style.backgroundColor = "#FFFFFF";
                techDiv1.style.backgroundColor = "#FFFFFF";
                techDiv5.style.backgroundColor = "#FFFFFF";
            }
            else if (name == "Environment & Climate Change")
            {
                techDiv5.style.backgroundColor = "#dff3ee";
                techDiv2.style.backgroundColor = "#FFFFFF";
                techDiv3.style.backgroundColor = "#FFFFFF";
                techDiv4.style.backgroundColor = "#FFFFFF";
                techDiv1.style.backgroundColor = "#FFFFFF";
            }
            else
            {
                techDiv5.style.backgroundColor = "#FFFFFF";
                techDiv2.style.backgroundColor = "#FFFFFF";
                techDiv3.style.backgroundColor = "#FFFFFF";
                techDiv4.style.backgroundColor = "#FFFFFF";
                techDiv1.style.backgroundColor = "#FFFFFF";
            }

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
                        var template = '<tr style="font-size:14px;"><td width="15%">'+technology_name +'</td><td>'+inventor_detail +'</td><td>'+institute +'</td><td width="45%">'+technology_abstract +'</td><td>'+technology_status +'</td><td>'+technology_transferred +'</td></tr>';

                           // technology_area.style.display = "block";
                             $("#tbody").append(template);

                    });
                }
            });
        });
})
