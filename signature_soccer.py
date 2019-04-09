import pandas

    
def sign(player, volume="absolute", maxdist=35, mindist=4, minwidth=0, miny=-.25, maxdif=.15, sector="rectangle",
		season_first=2014, season_last=2017, lines="true", sample="false", width=600, height=200, label="true") :
        

    russia = ["Lokomotiv Moscow","CSKA Moscow","Spartak Moscow","FC Krasnodar","Zenit St. Petersburg","FC Ufa","Arsenal Tula","Dinamo Moscow","FK Akhmat","Rubin Kazan","FC Rostov","Ural",
            "Amkar","Anzhi Makhachkala","Tosno","SKA-Khabarovsk","Krylya Sovetov Samara","FC Orenburg","Tom Tomsk","Mordovya","Kuban Krasnodar","Torpedo Moscow",]

    allshots = pandas.read_csv("allshots.csv")
    allshots = allshots[~allshots.h_team.isin(russia)]

    shots_ = allshots[(allshots.situation=="OpenPlay")&~(allshots.result=="OwnGoal")&(allshots.season>=season_first)&(allshots.season<=season_last)]
    shots = shots_[shots_.player==player] if player != "allplayers" else shots_

    season = "{}{}".format(season_first,"-"+str(season_last+1)[2:] if season_first!=season_last else "")

    field_width = 75
    field_length = 104.347826
    x1 = field_width - shots.Y*field_width
    y1 = shots.X*field_length
    x0 = field_width/2
    y0 = field_length
    distance = ((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0))**.5
    x1_ = field_width - shots_.Y*field_width
    y1_ = shots_.X*field_length
    distance_ = ((x1_-x0)*(x1_-x0)+(y1_-y0)*(y1_-y0))**.5

    

    sectors =  {30: [4208, 61, 0.01449619771863118], 29: [5040, 98, 0.019444444444444445], 28: [5381, 116, 0.02155733135104999], 27: [5478, 132, 0.024096385542168676],
                26: [5277, 149, 0.028235740003790033], 25: [5226, 201, 0.038461538461538464], 24: [4908, 199, 0.04054604726976365], 23: [4665, 225, 0.04823151125401929],
                22: [4362, 194, 0.044475011462631824], 21: [4976, 258, 0.05184887459807074], 20: [5717, 356, 0.06227042154976386], 19: [5222, 416, 0.07966296438146304], 
                18: [5264, 434, 0.08244680851063829], 17: [6614, 644, 0.09736921681282129], 16: [7175, 868, 0.12097560975609756], 15: [6638, 947, 0.14266345284724313], 
                14: [5796, 860, 0.14837819185645273], 13: [4945, 781, 0.15793731041456016], 12: [4348, 737, 0.16950321987120515], 11: [4180, 790, 0.18899521531100477], 
                10: [3919, 793, 0.20234753763715232], 9: [3645, 842, 0.2310013717421125], 8: [2739, 871, 0.31799926980649873], 7: [1657, 580, 0.3500301750150875], 
                6: [1472, 680, 0.46195652173913043], 5: [938, 539, 0.5746268656716418], 4: [479, 336, 0.7014613778705637], 3: [221, 188, 0.8506787330316742],
                2: [59, 56, 0.9491525423728814], 1: [7, 7, 1.0]}

    # avgs extracted from OpenPlay, ~OwnGoals, for allplayers from the Big Five leagues 
    avgs = {30: 0.01449619771863118, 29: 0.019444444444444445, 28: 0.02155733135104999, 27:0.024096385542168676, 26: 0.028235740003790033,
            25: 0.038461538461538464, 24: 0.04054604726976365, 23: 0.04823151125401929, 22: 0.044475011462631824, 21: 0.05184887459807074,
            20: 0.06227042154976386, 19: 0.07966296438146304, 18: 0.08244680851063829, 17: 0.09736921681282129, 16: 0.12097560975609756,
            15: 0.14266345284724313, 14: 0.14837819185645273, 13: 0.15793731041456016, 12: 0.16950321987120515, 11: 0.18899521531100477,
            10: 0.20234753763715232, 9: 0.2310013717421125, 8: 0.31799926980649873, 7: 0.3500301750150875, 6: 0.46195652173913043,
            5: 0.5746268656716418,4: 0.7014613778705637, 3: 0.8506787330316742, 2: 0.9491525423728814, 1: 1.0}

    avgs_vol = {30: 0.03490494044261588, 29: 0.04180629748830419, 28: 0.044634858489000964, 27: 0.04543946381764491, 26: 0.04377218885828992,
                25: 0.0433491489432297, 24: 0.04071137064932479, 23: 0.03869570987756727, 22: 0.03618235508809184, 21: 0.04127542386940509,
                20: 0.04742194498822124, 19: 0.04331596934204851, 18: 0.043664355154451044, 17: 0.054862470553103955, 16: 0.059515909618766384, 
                15: 0.05506154816019111, 14: 0.04807724211154982, 13: 0.04101828196025084, 12: 0.036066226483957665, 11: 0.03467268323434752, 
                10: 0.032507714257274625, 9: 0.030234911576362853, 8: 0.022719731908822455, 7: 0.013744649789309532, 6: 0.01221009323467932, 
                5: 0.007780616476989946, 4: 0.003973257241447958, 3: 0.0018331729652609576, 2: 0.0004893991174226086, 1: 5.8064302067089154e-05}



    ## creating variables dictionary

    k = 2 # smooth factor
    var_data = []
    #for dist in range(1,maxdist+1) : # focusing on shot distances from 0 to maxdist yards
    for dist in range(mindist,maxdist+1) : # focusing on shot distances from mindist to maxdist yards
        k2 = k if min(maxdist-dist,dist)>=k else k+2-abs(min(maxdist-dist,dist)) # to assure 4 areas averaged also in extremes
        
        if sector == "wedge" :
            # wedges
            if len(shots[(distance>=dist-k)&(distance<dist+k)]) != 0 :
                per_s = (len(shots[(distance>=dist-k2)&(distance<dist+k2)&(shots.result=="Goal")])
                        /len(shots[(distance>=dist-k2)&(distance<dist+k2)])
                        )
                avg_s = (len(shots_[(distance_>=dist-k2)&(distance_<dist+k2)&(shots_.result=="Goal")])
                        /len(shots_[(distance_>=dist-k2)&(distance_<dist+k2)])
                        )
            else :
                per_s = "not available"
        
        if sector == "rectangle" :
            if len(shots[((x1>=x0-4-dist-k2)&(x1<=x0+4+dist+k2)&(y1>=y0-dist-k2))&~((x1>=x0-4-dist+k2)&(x1<=x0+4+dist-k2)&(y1>=y0-dist+k2))]) != 0 :
                per_s = (len(shots[((x1>=x0-4-dist-k2)&(x1<=x0+4+dist+k2)&(y1>=y0-dist-k2))&~((x1>=x0-4-dist+k2)&(x1<=x0+4+dist-k2)&(y1>=y0-dist+k2))&(shots.result=="Goal")])
                        /len(shots[((x1>=x0-4-dist-k2)&(x1<=x0+4+dist+k2)&(y1>=y0-dist-k2))&~((x1>=x0-4-dist+k2)&(x1<=x0+4+dist-k2)&(y1>=y0-dist+k2))])
                        )
                avg_s = (len(shots_[((x1_>=x0-4-dist-k2)&(x1_<=x0+4+dist+k2)&(y1_>=y0-dist-k2))&~((x1_>=x0-4-dist+k2)&(x1_<=x0+4+dist-k2)&(y1_>=y0-dist+k2))&(shots_.result=="Goal")])
                        /len(shots_[((x1_>=x0-4-dist-k2)&(x1_<=x0+4+dist+k2)&(y1_>=y0-dist-k2))&~((x1_>=x0-4-dist+k2)&(x1_<=x0+4+dist-k2)&(y1_>=y0-dist+k2))])
                        )
            else :
                per_s = "not available"

        if per_s != "not available" :
            #vol = len(shots[(distance>=dist-1)&(distance<dist)])
            k2 = k if min(maxdist-dist,dist)>=k else k+2-abs(min(maxdist-dist,dist)) # to assure 4 areas averaged also in extremes
            # rectangles
            #vol_s = len(shots[(distance>=dist-k2)&(distance<dist+k2)])/(2*k)
            # wedges       
            vol_s = len(shots[((x1>=x0-4-dist-k2)&(x1<=x0+4+dist+k2)&(y1>=y0-dist-k2))&~((x1>=x0-4-dist+k2)&(x1<=x0+4+dist-k2)&(y1>=y0-dist+k2))])/(2*k)
            vol_per = vol_s/len(shots)
            #avg = avgs[dist]
            #avg_vol = avgs_vol[dist]
            #var = {"x":dist, "y":per_s, "widthValue":vol, "colorValue":per_s-avg}
            #var = {"x":dist, "y":per_s, "widthValue":vol_s, "colorValue":per_s-avg}
            #var = {"x":dist, "y":per_s, "widthValue":vol_s, "colorValue":(per_s-avg_s)/avg_s}
            var = {"x":dist, "y":per_s, "widthValue":vol_s if volume=="absolute" else vol_per, "colorValue":per_s-avg_s}
            #var = {"x":dist, "y":per_s, "widthValue":vol_per, "colorValue":per_s-avg}
            #var = {"x":dist, "y":per_s, "widthValue":(vol_per-avg_vol)*len(shots), "colorValue":per_s-avg} # w domain must be set to 20
            var_data.append(var)

    #print(var_data)

    #width = 600
    #height = 200


    html_str = """

    <!DOCTYPE html>
    <html>
    <head>
      <title>player=%s seasons=%s</title>
    </head>
    <body>
      <div id="signature"></div>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"></script>
      <script>
    // get your data

    var data = %s
    ;


    // initialize SVG
    var width = %s, height = %s;
    var svg = d3.select("#signature").append("svg")
      .attr("width", width)
      .attr("height", height);


    // x = distance in shooting signatures
    var x = d3.scale.linear()
      .domain([%s, %s])
      .range([0, width]);

    // for gradient offset (needs %% - so map x domain to 0-100%%)
    var offset = d3.scale.linear()
      .domain(x.domain())
      .range([0, 100]);

    // y = Field Goal percentage in shooting signatures
    var y = d3.scale.linear()
      .domain([%s, 1])
      .range([height, 0]);


    // scale for the width of the signature
    var minWidth = %s;
    var maxWidth = height / 4;

    var w = d3.scale.linear()
      .domain([0, %s])
      .range([minWidth, maxWidth]);

    // NOTE: if you want maxWidth to truly be the maximum width of the signature,
    // you'll need to add .clamp(true) to w.



    // need two area plots to make the signature extend in width in both directions around the line
    var areaAbove = d3.svg.area()
      .x(function(d) { return x(d.x); })
      .y0(function (d) { return y(d.y) - w(d.widthValue); })
      .y1(function(d) { return Math.ceil(y(d.y)); }) // ceil and floor prevent line between areas
      .interpolate("basis");

    var areaBelow = d3.svg.area()
      .x(function(d) { return x(d.x); })
      .y0(function (d) { return y(d.y) + w(d.widthValue); })
      .y1(function(d) { return Math.floor(y(d.y)); }) // ceil and floor prevent line between areas
      .interpolate("basis");


    // add the areas to the svg
    var gArea = svg.append("g").attr("class", "area-group");
    gArea.append("path")
      .datum(data)
      .attr("class", "area area-above")
      .attr("d", areaAbove)
      .style("fill", "url(#area-gradient)"); // specify the linear gradient #area-gradient as the colouring

      // NOTE: the colouring won't work if you have multiple signatures on the same page.
      // In this case, you'll need to generate unique IDs for each gradient.

    gArea.append("path")
      .datum(data)
      .attr("class", "area area-below")
      .attr("d", areaBelow)
      .style("fill", "url(#area-gradient)");

    // ? auxiliar lines
    var lines = %s;
    var lines_wedge = %s;
    var lines_rectangle = %s;
    var sample_wedge = %s;
    var sample_rectangle = %s;
    var sample = %s;
    var label = %s;
    var zeroline = %s;

    // ? sample arrow ha
    if (sample) {
      gArea.append("line")
        .attr("x1", width*1/600)
        .attr("x2", width)
        .attr("y1", height*199/200)
        .attr("y2", height*199/200)
        .style("stroke", "black")
        .style("stroke-width", "1")
      }

    // ? sample arrow ha
    if (sample) {
      gArea.append("line")
        .attr("x1", width*590/600)
        .attr("x2", width)
        .attr("y1", height*195/200)
        .attr("y2", height*199/200)
        .style("stroke", "black")
        .style("stroke-width", "1")
      }

    // ? sample arrow ha
    if (sample) {
      gArea.append("line")
        .attr("x1", width*590/600)
        .attr("x2", width*590/600)
        .attr("y1", height*195/200)
        .attr("y2", height*199/200)
        .style("stroke", "black")
        .style("stroke-width", "1")
      }

    // ? sample arrow va
    if (sample) {
      gArea.append("line")
        .attr("x1", width*1/600)
        .attr("x2", width*1/600)
        .attr("y1", height*30/200)
        .attr("y2", height*199/200)
        .style("stroke", "black")
        .style("stroke-width", "1")
      }

    // ? sample arrow va
    if (sample) {
      gArea.append("line")
        .attr("x1", width*1/600)
        .attr("x2", width*5/600)
        .attr("y1", height*30/200)
        .attr("y2", height*40/200)
        .style("stroke", "black")
        .style("stroke-width", "1")
      }

    // ? sample arrow va
    if (sample) {
      gArea.append("line")
        .attr("x1", width*1/600)
        .attr("x2", width*5/600)
        .attr("y1", height*40/200)
        .attr("y2", height*40/200)
        .style("stroke", "black")
        .style("stroke-width", "1")
      }


    // ? 6-yard box
    if (lines_rectangle) {
      gArea.append("line")
        .attr("x1", %s)
        .attr("x2", %s)
        .attr("y1", height*40/200)
        .attr("y2", height)
        .style("stroke", "%s")
        .style("stroke-width", %s)
        .style("stroke-dasharray", ("3, 3"))
      }


    // ? 15-yard
    if (sample_rectangle) {
      gArea.append("line")
        .attr("x1", %s)
        .attr("x2", %s)
        .attr("y1", height*40/200)
        .attr("y2", height)
        .style("stroke", "#ff3300")
        .style("stroke-width", "2")
      }

    // ? 15-yard
    if (sample_wedge) {
      gArea.append("line")
        .attr("x1", %s)
        .attr("x2", %s)
        .attr("y1", height*40/200)
        .attr("y2", height)
        .style("stroke", "#ff3300")
        .style("stroke-width", "2")
      }

    // ? penalty area
    if (lines_rectangle) {
      gArea.append("line")
        .attr("x1", %s)
        .attr("x2", %s)
        .attr("y1", height*40/200)
        .attr("y2", height)
        .style("stroke", "%s")
        .style("stroke-width", %s)
        .style("stroke-dasharray", ("3, 3"))
      }

    // ? 6 yard wedge
    if (lines_wedge) {
      gArea.append("line")
        .attr("x1", %s)
        .attr("x2", %s)
        .attr("y1", height*40/200)
        .attr("y2", height)
        .style("stroke", "%s")
        .style("stroke-width", %s)
        .style("stroke-dasharray", ("3, 3"))
      }

    // ? 12 yard wedge
    if (lines_wedge) {
      gArea.append("line")
        .attr("x1", %s)
        .attr("x2", %s)
        .attr("y1", height*40/200)
        .attr("y2", height)
        .style("stroke", "%s")
        .style("stroke-width", %s)
        .style("stroke-dasharray", ("3, 3"))
      }

    // ? 18 yard wedge
    if (lines_wedge) {
      gArea.append("line")
        .attr("x1", %s)
        .attr("x2", %s)
        .attr("y1", height*40/200)
        .attr("y2", height)
        .style("stroke", "%s")
        .style("stroke-width", %s)
        .style("stroke-dasharray", ("3, 3"))
      }

    // ? 28.425 yard wedge (outside penalty area)
    if (lines_wedge) {
      gArea.append("line")
        .attr("x1", %s)
        .attr("x2", %s)
        .attr("y1", height*40/200)
        .attr("y2", height)
        .style("stroke", "%s")
        .style("stroke-width", %s)
        .style("stroke-dasharray", ("3, 3"))
      }

    // ? .30 fgp line
    if (lines) {
      gArea.append("line")
        .attr("x1", 0)
        .attr("x2", width)
        .attr("y1", %s)
        .attr("y2", %s)
        .style("stroke", "orange")
        .style("stroke-width", "0.3")
      }

    // ? .20 fgp line
    if (lines) {
      gArea.append("line")
        .attr("x1", 0)
        .attr("x2", width)
        .attr("y1", %s)
        .attr("y2", %s)
        .style("stroke", "orange")
        .style("stroke-width", "0.3")
      } 

    // ? .10 fgp line
    if (lines) {
      gArea.append("line")
        .attr("x1", 0)
        .attr("x2", width)
        .attr("y1", %s)
        .attr("y2", %s)
        .style("stroke", "orange")
        .style("stroke-width", "0.3")
      }

    // ? .00 fgp line
    if (lines) {
      gArea.append("line")
        .attr("x1", 0)
        .attr("x2", width)
        .attr("y1", %s)
        .attr("y2", %s)
        .style("stroke", "black")
        .style("stroke-width", "0.3")
      }

    // ? player label
    if (label) {
        gArea.append("text")
            .attr("x", width*575/600)
            .attr("y", height*40/200)
            .text("%s")
            .attr("fill","k")
            .attr("text-anchor","end")
            .attr("alignment-baseline","hanging")
            .style("font-size", "30px")
            .style("font-family", "Arial");
        }
    
    if (lines) {
      // you can draw the line the signature is based around using the following code:
      var line = d3.svg.line()
        .x(function(d) { return x(d.x); })
        .y(function(d) { return y(d.y); })
        .interpolate("basis");

      gArea.append("path")
        .datum(data)
        .attr("d", line)
        .style("stroke", "#fff")
        .style("fill", "none")
        .style("stroke-width", "0.25") // ?
      }

    // set-up colours
    var colorSchemes = {
      buckets: {
        domain: [-0.15, 0.15],
        range: ["#405A7C", "#7092C0", "#BDD9FF", "#FFA39E", "#F02C21", "#B80E05"]
      },
      goldsberry: {
        domain: [-%s, %s],
        range: ["#5357A1", "#6389BA", "#F9DC96", "#F0825F", "#AE2A47"]
      }
    };
    var activeColorScheme = colorSchemes.goldsberry;

    // Note that the quantize scale does not interpolate between colours
    var colorScale = d3.scale.quantize()
      .domain(activeColorScheme.domain)
      .range(activeColorScheme.range);


    // generate colour data
    var colorData = [];
    var stripe = true; // set stripe to true to prevent linear gradient fading
    for (var i = 0; i < data.length; i++) {
      var prevData = data[i - 1];
      var currData = data[i];
      if (stripe && prevData) {
        colorData.push({
          offset: offset(currData.x) + "%%",
          stopColor: colorScale(prevData.colorValue)
        });
      }
    }

    // generate the linear gradient used by the signature
    gArea.append("linearGradient")
      .attr("id", "area-gradient")
      .attr("gradientUnits", "userSpaceOnUse")
      .attr("y1", 0)
      .attr("y2", 0)
      .selectAll("stop")
        .data(colorData)
        .enter().append("stop")
          .attr("offset", function(d) { return d.offset })
          .attr("stop-color", function (d) { return d.stopColor; });
    </script>
    </body>
    </html>

    """ % (player,season,var_data
           ,width,height 
           ,mindist,maxdist,miny,minwidth
           ,str(12.5*(season_last+1-season_first)) if volume=="absolute" else ".1"
           ,lines # var lines
           ,"true" if sector=="wedge" and lines=="true" else "false" # var lines_wedge
           ,"true" if sector=="rectangle" and lines=="true" else "false" # var lines_rectangle
           ,"true" if (sector=="wedge" and lines=="true" and sample=="true") else "false" # var sample_wedge
           ,"true" if (sector=="rectangle" and lines=="true" and sample=="true") else "false" # var sample_rectangle
           ,sample # var sample
           #,"true" if sample=="false" and labeled==True else "false" # var label
           ,label # var label
           ,"true" if lines=="true" and sample=="false" else "false" # var zeroline
           ,(6-mindist)*width/(maxdist-mindist),(6-mindist)*width/(maxdist-mindist)
           ,"black" if not sample else "#666666"
           ,".3" if not sample else "1"
           ,(15-mindist)*width/(maxdist-mindist),(15-mindist)*width/(maxdist-mindist)
           ,(15-mindist)*width/(maxdist-mindist),(15-mindist)*width/(maxdist-mindist)
           ,(18-mindist)*width/(maxdist-mindist),(18-mindist)*width/(maxdist-mindist)
           ,"black" if not sample else "#666666"
           ,".3" if not sample else "1"
           ,(6-mindist)*width/(maxdist-mindist),(6-mindist)*width/(maxdist-mindist)
           ,"black" if not sample else "#666666"
           ,".3" if not sample else "1"
           ,(12-mindist)*width/(maxdist-mindist),(12-mindist)*width/(maxdist-mindist)
           ,"black" if not sample else "#666666"
           ,".3" if not sample else "1"
           ,(18-mindist)*width/(maxdist-mindist),(18-mindist)*width/(maxdist-mindist)
           ,"black" if not sample else "#666666"
           ,".3" if not sample else "1"
           ,(28.425-mindist)*width/(maxdist-mindist),(28.425-mindist)*width/(maxdist-mindist)
           ,"black" if not sample else "#666666"
           ,".3" if not sample else "1"
           ,height-((abs(miny)+.3)*height/(1+abs(miny))),height-((abs(miny)+.3)*height/(1+abs(miny)))
           ,height-((abs(miny)+.2)*height/(1+abs(miny))),height-((abs(miny)+.2)*height/(1+abs(miny)))
           ,height-((abs(miny)+.1)*height/(1+abs(miny))),height-((abs(miny)+.1)*height/(1+abs(miny)))
           ,height-((abs(miny)+.0)*height/(1+abs(miny))),height-((abs(miny)+.0)*height/(1+abs(miny)))
           ,player
           ,maxdif,maxdif)


    #""".format(var_data) not working this kind of formatting

    # if saving signature in html file
    """
    html_file = open("{}signature_{}_{}{}_volume={}_maxdist={}_mindist={}_miny={}_minwidth={}_maxdif={}_sector={}_dim={}x{}.html".format("sample_" if sample=="true" else "",player,season,
                     "_lined" if lines == "true" else "",volume,maxdist,mindist,miny,minwidth,maxdif,sector,width,height),"w")
    html_file.write(html_str)
    html_file.close()
    """
    # if rendering in jupyter notebook
    return html_str 