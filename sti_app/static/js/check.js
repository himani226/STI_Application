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
                                    var myDiv = document.getElementById("chart-container");
                                    var divBarChart = document.getElementById("barchart-container");
                                    if(myDiv){
                                        const dataSource = {
                                        chart: {
                                        caption: "New Companies Registered <br> Year 2020-21",
                                        subCaptionFontSize:"20",
                                        plottooltext: "<b>$dataValue</b> of Firms/Companies Registered",
                                        showlegend: "1",
                                        showpercentvalues: "1",
                                        legendposition: "bottom",
                                        usedataplotcolorforlabels: "1",
                                        labelFontSize: "20",
                                        showPercentValues: "0",
                                        theme: "fusion"
                                        },
                                        data: [
                                        {
                                        label: "New Indian Firms Registered",
                                        toolText: "$dataValue",
                                        color: "#483a75",
                                        value: "2070"
                                        },
                                        {
                                        label: "New LLP's Registered",
                                        toolText: "$dataValue",
                                        color: "#1cadad",
                                        value: "519"
                                        },
                                        {
                                        label: "New Foreign Firms Registered ",
                                        toolText: "$dataValue",
                                        color: "#de6172",
                                        value: "0"
                                        },
                                        {
                                        label: "New Companies Registered",
                                        toolText: "$dataValue",
                                        Color: "#ff9117",
                                        value: "2589"
                                        }
                                        ]
                                        };

                                        FusionCharts.ready(function() {
                                        var myChart = new FusionCharts({
                                        type: "pie2d",
                                        renderAt: "chart-container",
                                        width: "100%",
                                        height: "100%",
                                        dataFormat: "json",
                                        dataSource
                                        }).render();
                                        });
                                    }
                                    else if(divBarChart)
                                    {
                                        const dataSource = {
                                          chart: {
                                            caption: "Ease of Doing Business",
                                            xaxisname: "Year",
                                            yaxisname: "Ranking of State",

                                            theme: "fusion"
                                          },
                                          data: [
                                            {
                                              label: "2017-18",
                                              value: "20",
                                              color: "#1cadad",
                                            },
                                            {
                                              label: "2018-19",
                                              value: "NA"
                                            },
                                            {
                                              label: "2019-20",
                                              value: "19",
                                              color: "#ff9117",
                                            },
                                            {
                                              label: "2020-21",
                                              value: "NA"
                                            },
                                          ]
                                        };

                                        FusionCharts.ready(function() {
                                          var myChart = new FusionCharts({
                                            type: "column2d",
                                            renderAt: "barchart-container",
                                            width: "100%",
                                            height: "100%",
                                            dataFormat: "json",
                                            dataSource
                                          }).render();
                                        });
                                    }
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
