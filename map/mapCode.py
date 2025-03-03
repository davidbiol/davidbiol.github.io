import folium
from branca.element import Template, MacroElement

m = folium.Map(location = [4.57, -74.29], zoom_start = 4)

#Thismia andicola
tooltip1 = "<div><p><i><b>Thismia andicola</b></i> \n Click to see more </p></div>"
icon1 = folium.Icon(color = "green", prefix = "fa")
popup1 = folium.Popup("<div> <p><i><b>Thismia andicola </b></i> Aguilar-Cano, S. Guzman-Guzman & Lopera-Toro <br>Year of publication: 2023 <br> sect. <i>Ophiomeris</i> <br> <a href='../thismia_andicola.html' target = '_blank'> More information about this species </a> <br> <a href='https://www.biotaxa.org/Phytotaxa/article/view/phytotaxa.579.2.4' target = '_blank'> Orignial publication</a><br> </p> <img src='image.jpeg'> </div>", max_width=500)

marker1 = folium.Marker(location = [7.22805, -72.31172777777778], popup = popup1,tooltip = tooltip1, icon = icon1).add_to(m)

#Thismia calcarata
tooltip2 = "<div><p><i><b>Thismia calcarata</b></i> \n Click to see more </p></div>"
icon2 = folium.Icon(color = "green", prefix = "fa")
popup2 = folium.Popup("<div> <p><i><b>Thismia calcarata </b></i> D.F.Silva, Honório & J.M.A.Braga <br>Year of publication: 2023 <br> sect. <i>Ophiomeris</i> <br> <a href='../thismia_calcarata.html' target = '_blank'> More information about this species </a> <br> <a href='https://www.biotaxa.org/Phytotaxa/article/view/phytotaxa.587.3.5' target = '_blank'> Orignial publication</a><br> </p> <img src='image_thismia_calcarata.png' width = '300'> </div>", max_width=500)

marker2 = folium.Marker(location = [-9.3902778, -69.91972222222223], popup = popup2,tooltip = tooltip2, icon = icon2).add_to(m)

#Thismia variabilis
tooltip3 = "<div><p><i><b>Thismia variabilis</b></i> \n Click to see more </p></div>"
icon3 = folium.Icon(color = "green", prefix = "fa")
popup3 = folium.Popup("<div> <p><i><b>Thismia variabilis </b></i> D.F.Silva, Honório & J.M.A.Braga <br>Year of publication: 2023 <br> sect. <i>Ophiomeris</i> <br> <a href='../thismia_variabilis.html' target = '_blank'> More information about this species </a> <br> <a href='https://www.biotaxa.org/Phytotaxa/article/view/phytotaxa.587.3.5' target = '_blank'> Orignial publication</a><br> </p> <img src='image_thismia_variabilis.png' width = '250'> </div>", max_width=500)

marker3 = folium.Marker(location = [-9.75125, -67.67108333333334], popup = popup3,tooltip = tooltip3, icon = icon3).add_to(m)

#Thismia petasiformis
tooltip4 = "<div><p><i><b>Thismia petasiformis</b></i> \n Click to see more </p></div>"
icon4 = folium.Icon(color = "orange", prefix = "fa")
popup4 = folium.Popup("<div> <p><i><b>Thismia petasiformis </b></i> D.F.Silva & J.M.A.Braga <br>Year of publication: 2022 <br> sect. <i>Pyramidalis</i> <br> <a href='../thismia_petasiformis.html' target = '_blank'> More information about this species </a> <br> <a href='https://www.biotaxa.org/Phytotaxa/article/view/phytotaxa.564.2.5' target = '_blank'> Orignial publication</a><br> </p> <img src='image_thismia_petasiformis.png' width = '250'> </div>", max_width=500)

marker4 = folium.Marker(location = [-9.9944444, -57.82166666666667], popup = popup4,tooltip = tooltip4, icon = icon4).add_to(m)

#Thismia mantiqueiriensis, En duda la localidad, se aproxima a Sierra de la Mantiqueira
tooltip5 = "<div><p><i><b>Thismia mantiqueirensis</b></i> \n Click to see more </p></div>"
icon5 = folium.Icon(color = "green", prefix = "fa")
popup5 = folium.Popup("<div> <p><i><b>Thismia mantiqueirensis </b></i> Engels & E.C.Smidt <br>Year of publication: 2022 <br> sect. <i>Ophiomeris</i> <br> <a href='../thismia_mantiqueirensis.html' target = '_blank'> More information about this species </a> <br> <a href='https://www.biotaxa.org/Phytotaxa/article/view/phytotaxa.570.2.8' target = '_blank'> Orignial publication</a><br> </p> <img src='image_thismia_mantiqueirensis.png' width = '175'> </div>", max_width=500)

marker5 = folium.Marker(location = [-21.998159821631155, -44.747458250117866], popup = popup5,tooltip = tooltip5, icon = icon5).add_to(m)

#Thismia cordata
tooltip6 = "<div><p><i><b>Thismia cordata</b></i> \n Click to see more </p></div>"
icon6 = folium.Icon(color = "green", prefix = "fa")
popup6 = folium.Popup("<div> <p><i><b>Thismia cordata </b></i> D.F.Silva & J.M.A.Braga <br>Year of publication: 2022 <br> sect. <i>Ophiomeris</i> <br> <a href='../thismia_cordata.html' target = '_blank'> More information about this species </a> <br> <a href='https://www.biotaxa.org/Phytotaxa/article/view/phytotaxa.571.1.6' target = '_blank'> Orignial publication</a><br> </p> <img src='image_thismia_cordata.png' width = '175'> </div>", max_width=500)

marker6 = folium.Marker(location = [-25.5122222, -48.98888888888889], popup = popup6,tooltip = tooltip6, icon = icon6).add_to(m)

#Thismia prataensis, sale la localidad en el oceano, tal vez ubicarlo en Serra da Prata
tooltip7 = "<div><p><i><b>Thismia prataensis</b></i> \n Click to see more </p></div>"
icon7 = folium.Icon(color = "gray", prefix = "fa")
popup7 = folium.Popup("<div> <p><i><b>Thismia prataensis </b></i> Mancinelli, C. T. Blum and E. C. Smidt <br>Year of publication: 2012 <br> sect. <i>Unknown</i> <br> <a href='../thismia_prataensis.html' target = '_blank'> More information about this species </a> <br> <a href='https://bioone.org/journals/systematic-botany/volume-37/issue-4/036364412X656545/Thismia-prataensis-Thismiaceae-a-New-Species-from-the-Brazilian-Atlantic/10.1600/036364412X656545.short' target = '_blank'> Orignial publication</a><br> </p> <img src='image_thismia_prataensis.png' width = '250'> </div>", max_width=500)

marker7 = folium.Marker(location = [-25.38, -48.43], popup = popup7,tooltip = tooltip7, icon = icon7).add_to(m)

#Thismia ribeiroi, no hay corrdenadas en el original, ubico la corrdenada en la Comunidade Sagrada Familia en Mato Grosso, Brazil
tooltip8 = "<div><p><i><b>Thismia ribeiroi</b></i> \n Click to see more </p></div>"
icon8 = folium.Icon(color = "orange", prefix = "fa")
popup8 = folium.Popup("<div> <p><i><b>Thismia ribeiroi </b></i> Engels, D. Ferreira-da-Silva & Soares-Lopes <br>Year of publication: 2020 <br> sect. <i>Pyramidalis</i> <br> <a href='../thismia_ribeiroi.html' target = '_blank'> More information about this species </a> <br> <a href='https://bioone.org/journals/systematic-botany/volume-37/issue-4/036364412X656545/Thismia-prataensis-Thismiaceae-a-New-Species-from-the-Brazilian-Atlantic/10.1600/036364412X656545.short' target = '_blank'> Orignial publication</a><br> </p> <img src='image_thismia_ribeiroi.png' width = '250'> </div>", max_width=500)

marker8 = folium.Marker(location = [-9.96920437016841, -57.82678718897943], popup = popup8,tooltip = tooltip8, icon = icon8).add_to(m)


template = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
     
<div class='legend-title'>Sections</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:green;opacity:1;'></span><i>Ophiomeris</i></li>
    <li><span style='background:orange;opacity:1;'></span><i>Pyramidalis</i></li>
    <li><span style='background:gray;opacity:1;'></span><i>Unknown</i></li>

  </ul>
</div>
</div>
 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template)

m.get_root().add_child(macro)

template2 = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Draggable - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; left: 20px; bottom: 20px;'>
     
<div class='legend-title'>Map view</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><a href='map.html'> Open street</a></li>
    <li><a href='map_stamenTerrain.html'> Terrain</a></li>

  </ul>
</div>
</div>
 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template2)

m.get_root().add_child(macro)


m.save("map.html")

