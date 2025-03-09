import folium
from branca.element import Template, MacroElement
import pandas as pd

data = pd.read_excel("Map_info_Megalastrum.xlsx")

m = folium.Map(location = [4.57, -74.29], tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', zoom_start = 3, attr = "D. Gutiérrez-Duque 2025 &copy;")

for ID in range(0,len(data.index)):
  tooltip1 = "<div><p><i><b>"+data["species"][ID]+"</b></i> \n Click to see more </p></div>"
  icon1 = folium.Icon(color = data["color"][ID], prefix = "fa")
  popup1 = folium.Popup("<div> <p><i><b>"+data["species"][ID]+" </b></i> "+data["author"][ID]+" <br>Year of publication: "+str(data["year"][ID])+" <br> Region "+data["region"][ID]+" <br> <a href='"+data["speciesLink"][ID]+"' target = '_blank'> More information about this species </a> <br> <a href='"+data["originalPublication"][ID]+"' target = '_blank'> Original publication</a><br> </p> <img src=''> </div>", max_width=500)
  marker1 = folium.Marker(location = [data["lat"][ID], data["long"][ID]], popup = popup1,tooltip = tooltip1, icon = icon1).add_to(m)


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
     
<div class='legend-title'>Regions</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:#73b127;opacity:1;'></span><i>Andes</i></li>
    <li><span style='background:orange;opacity:1;'></span><i>Brazil, Paraguay and Uruguay</i></li>
    <li><span style='background:gray;opacity:1;'></span><i>Central America</i></li>
    <li><span style='background:rgb(64, 173, 251);opacity:1;'></span><i>West Indies</i></li>
    <li><span style='background:rgb(197, 8, 218);opacity:1;'></span><i>Circumaustral</i></li>
    <li><span style='background:rgb(211, 2, 2);opacity:1;'></span><i>Paleotropics</i></li>

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


m.save("map_stamenTerrain.html")

