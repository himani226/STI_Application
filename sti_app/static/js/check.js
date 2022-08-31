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
                        var template = '<a href="#" class="row"><div class="col-lg-9 col-md-9 pillar-title-clr">'+ checkbox_label + '</div> <div class="col-lg-3 col-md-3 stageDiv"> <input type="checkbox" id="'+checkbox_id+'" name="'+checkbox_name+'" value="'+checkbox_value+'" class ="pillar" > </div><hr style="width:85%;text-align:left;margin-left:0;margin-top:10px;"></a>';
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
                                    var template = '<a href="#" class="row"><div class="col-lg-9 col-md-9">'+ indicator_label + '</div> <div class="col-lg-3 col-md-3 stageDiv"> <input type="checkbox" id="'+indicator_id+'" name="'+indicator_label+'" value="'+indicator_label+'" class ="indicator" > </div><hr style="width:85%;text-align:left;margin-left:0;margin-top:10px;"></a>';
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
                                    var template = '<div class="col-lg-12 col-md-12"><strong>'+indicator_label+'</strong></div><div class="col-lg-12 col-md-12">'+indicator_def+'</div>';
                                    indicator2.style.display = "flex";
                                    $("#indicator2").append(template);
                                    var myDiv = document.getElementById("chart-container");
                                    var highBarChart = document.getElementById("highsecondarychart-container");
                                    var divBarChart = document.getElementById("barchart-container");
                                    var divNestedChart = document.getElementById("nestedchart-container");
                                    var ictBarChartIndia = document.getElementById("ict-india-chart-container");
                                    var ictBarChartPunjab= document.getElementById("ict-pb-chart-container");
                                    if(myDiv){
                                        const dataSource = {
                                        chart: {
                                        baseFont:"Roboto",
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
                                        color: "#094BA4",
                                        value: "2070"
                                        },
                                        {
                                        label: "New LLP's Registered",
                                        toolText: "$dataValue",

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
                                            baseFont:"Roboto",
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
                                    else if(divNestedChart)
                                    {
                                    const dataSource = {
                                        chart: {
                                        showplotborder: "1",
                                        plotfillalpha: "80",
                                        useHoverColor :"0",
                                        baseFont:"Roboto",
                                        autoRotateLabels :"0",
                                        useEllipsesWhenOverflow :"0",
                                        skipOverlapLabels:"0",
                                        pieRadius : "240",

                                        plottooltext:
                                        " $DataValue $Label",
                                        theme: "fusion"
                                        },
                                        category: [
                                        {
                                        label: "Degree",
                                        tooltext: "No. of Degrees",
                                        color: "#ffffff",

                                        value: "150",
                                        category: [
                                        {
                                        label: "Post Graduate",
                                        color: "#dc6200",

                                        category: [
                                        {
                                        label: "Engineering",
                                        color: "#e27700",
                                        value: "010"
                                        },
                                        {
                                        label: "Medical",
                                        color: "#ff9117",
                                        value: "005"
                                        },
                                        {
                                        label: "Applied Sciences",
                                        color: "#ffa542",
                                        value: "201"
                                        },

                                        ]
                                        },
                                        {
                                        label: "Under Graduate",
                                        color: "008080",

                                        category: [
                                        {
                                        label: "Engineering",
                                        color: "#1cadad",
                                        value: "87"
                                        },
                                        {
                                        label: "Medical",
                                        color: "#2cc0c0",
                                        value: "94"
                                        },
                                        {
                                        label: "Applied Sciences",
                                        color: "#33d2d2",
                                        value: "307"
                                        }
                                        ]
                                        }
                                        ]
                                        }
                                        ]
                                        };
                                        FusionCharts.ready(function() {
                                        var myChart = new FusionCharts({
                                        type: "multilevelpie",
                                        renderAt: "nestedchart-container",
                                        width: "100%",
                                        height: "100%",
                                        dataFormat: "json",
                                        dataSource
                                        }).render();
                                        });
                                    }
                                    else if(highBarChart){
                                    const dataSource = {
                                        chart: {
                                        baseFont:"Roboto",
                                        yaxisname: "No. of Schools",
                                        formatnumberscale: "1",
                                        numvisibleplot: "8",
                                        labeldisplay: "auto",
                                        theme: "fusion",
                                        drawcrossline: "1",

                                        },
                                        categories: [
                                        {
                                        category: [
                                        {
                                        label: "2017-18"
                                        },
                                        {
                                        label: "2018-19"
                                        },
                                        {
                                        label: "2019-20"
                                        },
                                        {
                                        label: "2020-21"
                                        }

                                        ]
                                        }
                                        ],
                                        dataset: [
                                        {
                                        seriesname: "Total no. of Higher Sec. Schools ",
                                        color: "#094BA4",
                                        data: [
                                        {
                                        value: "5084",
                                        },
                                        {
                                        value: "5159",
                                        },
                                        {
                                        value: "5201",
                                        },
                                        {
                                        value: "00.00"
                                        }
                                        ]
                                        },
                                        {
                                        seriesname: "Higher Sec. Schools offering Science Streams",
                                        data: [
                                        {
                                        value: "2207"
                                        },
                                        {
                                        value: "2304"
                                        },
                                        {
                                        value: "2335"
                                        },
                                        {
                                        value: "00.00"
                                        }
                                        ]
                                        }
                                        ]
                                        };

                                        FusionCharts.ready(function() {
                                        var myChart = new FusionCharts({
                                        type: "scrollcolumn2d",
                                        renderAt: "highsecondarychart-container",
                                        width: "90%",
                                        height: "100%",
                                        dataFormat: "json",
                                        dataSource
                                        }).render();
                                        });
                                    }
                                    else if(ictBarChartIndia){
                                    const dataSource = {
                                        chart: {
                                        baseFont:"Roboto",
                                        caption: "ICT Enabled Schools",
                                        subcaption: "2017 - 2020",
                                        pyaxisname: "ICT Enabled Schools in India",
                                        syaxisname: "% of ICT Labs",
                                        snumbersuffix: "%",
                                        syaxismaxvalue: "25",
                                        theme: "fusion",
                                        showvalues: "0",
                                        drawcrossline: "1",
                                        divlinealpha: "20"
                                        },
                                        categories: [
                                        {
                                        category: [
                                        {
                                        label: "2017-18"
                                        },
                                        {
                                        label: "2018-19"
                                        },
                                        {
                                        label: "2019-20"
                                        }
                                        ]
                                        }
                                        ],
                                        dataset: [
                                        {
                                        dataset: [
                                        {
                                        seriesname: "Total No. of Schools in the Country",
                                        color:"#094BA4",
                                        data: [
                                        {
                                        value: "1558903"
                                        },
                                        {
                                        value: "1551000"
                                        },
                                        {
                                        value: "1507708"
                                        }
                                        ]
                                        },
                                        {
                                        seriesname: "Number of Schools with ICT Labs",
                                        data: [
                                        {
                                        value: "487443"
                                        },
                                        {
                                        value: "506483"
                                        },
                                        {
                                        value: "587656"
                                        }
                                        ]
                                        }
                                        ]
                                        },

                                        ],
                                        lineset: [
                                        {
                                        seriesname: "Percentage %",
                                        plottooltext:
                                        "Total ICT Labs in $label is <b>$dataValue</b> in India",
                                        showvalues: "0",
                                        data: [
                                        {
                                        value: "31.02"
                                        },
                                        {
                                        value: "33.41"
                                        },
                                        {
                                        value: "38.09"
                                        }
                                        ]
                                        }
                                        ]
                                        };

                                        FusionCharts.ready(function() {
                                        var myChart = new FusionCharts({
                                        type: "msstackedcolumn2dlinedy",
                                        renderAt: "ict-india-chart-container",
                                        width: "100%",
                                        height: "100%",
                                        dataFormat: "json",
                                        dataSource
                                        }).render();
                                        });
                                    }
                                    else if(ictBarChartPunjab){
                                    const dataSource = {
                                        chart: {
                                        baseFont:"Roboto",
                                        caption: "ICT Enabled Schools in Punjab",
                                        subcaption: "2017 - 2020",
                                        pyaxisname: "ICT Enabled Schools in Punjab",
                                        syaxisname: "% of ICT Labs",
                                        snumbersuffix: "%",
                                        syaxismaxvalue: "25",
                                        theme: "fusion",
                                        showvalues: "0",
                                        drawcrossline: "1",
                                        divlinealpha: "20"
                                        },
                                        categories: [
                                        {
                                        category: [
                                        {
                                        label: "2017-18"
                                        },
                                        {
                                        label: "2018-19"
                                        },
                                        {
                                        label: "2019-20"
                                        }
                                        ]
                                        }
                                        ],
                                        dataset: [
                                        {
                                        dataset: [
                                        {
                                        seriesname: "Total No. of Schools in Punjab",
                                        data: [
                                        {
                                        value: "28926"
                                        },
                                        {
                                        value: "28637"
                                        },
                                        {
                                        value: "28775"
                                        }
                                        ]
                                        },
                                        {
                                        seriesname: "Number of Schools with ICT Labs",
                                        data: [
                                        {
                                        value: "21979"
                                        },
                                        {
                                        value: "19112"
                                        },
                                        {
                                        value: "20269"
                                        }
                                        ]
                                        }
                                        ]
                                        },

                                        ],
                                        lineset: [
                                        {
                                        seriesname: "Percentage %",
                                        plottooltext:
                                        "Total ICT Labs in $label is <b>$dataValue</b> in India",
                                        showvalues: "0",
                                        data: [
                                        {
                                        value: "75.98"
                                        },
                                        {
                                        value: "66.73"
                                        },
                                        {
                                        value: "70.43"
                                        }
                                        ]
                                        }
                                        ]
                                        };

                                        FusionCharts.ready(function() {
                                        var myChart = new FusionCharts({
                                        type: "msstackedcolumn2dlinedy",
                                        renderAt: "ict-pb-chart-container",
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
