from flask import Flask,send_file,jsonify,url_for,request
from flask_cors import CORS
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster,Fullscreen
from prim import prim,calculate_distance
from GraphPrim import GraphPrim
import os
import gpxpy
import gpxpy.gpx
import osmnx as ox
import networkx as nx

class Hydrant:
    def __init__(self, districtId, lon, lat,index):
        self.districtId = districtId
        self.lon = lon
        self.lat = lat
        self.index = index

    def getIndex(self):
        return self.index

    def getLocation(self):
        return [self.lat, self.lon]

    def getDistrictId(self):
        return self.districtId

    def isNear(self, other):
        return calculate_distance(self.getLocation(), other.getLocation()) <= 600

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

def find_variable_name(html, prefix):
    pattern = f"var {prefix}"
    start_index = html.find(pattern) + 4
    tmp_html = html[start_index:]
    end_index = tmp_html.find(" =") + start_index
    return html[start_index:end_index]

def find_popup_slice(html):
    pattern = "function latLngPop(e)"
    starting_index = html.find(pattern)
    tmp_html = html[starting_index:]
    found = 0
    index = 0
    opening_found = False
    while not opening_found or found > 0:
        if tmp_html[index] == "{":
            found += 1
            opening_found = True
        elif tmp_html[index] == "}":
            found -= 1
        index += 1

    ending_index = starting_index + index

    return starting_index, ending_index


def custom_code(popup_variable_name, map_variable_name):
    return '''
           // custom code

           var marker;  // Variable para almacenar el marcador
           function latLngPop(e) {
               if (marker) {
                   marker.remove();  // Eliminar el marcador anterior
               }

               marker = L.marker(
                   [e.latlng.lat, e.latlng.lng],
                   {}
               ).addTo(%s);
           }

           // end custom code
    ''' % (map_variable_name)

@app.route('/api/v1.0/hydrants_map')
def hydrants_map():
    geojson_url = "HIDRANTES_PROVCALLAO.geojson"
    gdf = gpd.read_file(geojson_url)
    num_hydrants = 1500
    num_hydrants = min(num_hydrants, len(gdf))
    sampled_gdf = gdf.sample(n=num_hydrants, random_state=1)  # Ensure reproducibility with random_state
    sampled_gdf = sampled_gdf.reset_index(drop=True)
    m = folium.Map(location=[-12.050, -77.120], zoom_start=13)
    marker_cluster = MarkerCluster().add_to(m)
    Fullscreen(position='topright').add_to(m)

    hydrant_icon_url = 'https://raw.githubusercontent.com/diegooo01/FindU-Images/00588368ea06164b6fae1447896d8e1c208cbac5/hidrante-de-incendio%20(1).svg'
    hydrants_cola = []
    graph = GraphPrim(num_hydrants)

    for index, row in sampled_gdf.iterrows():
        lon, lat = row['geometry'].coords[0]
        districtId = row['DISTRICT']
        hydrant = Hydrant(districtId, lon, lat, index)

        icon = folium.CustomIcon(hydrant_icon_url, icon_size=(30, 30))  # Adjust size as needed

        folium.Marker(location=hydrant.getLocation(),
                      popup=f'Hydrant {row["FID"]}',
                      icon=icon).add_to(marker_cluster)

        for other in hydrants_cola:
            if hydrant.isNear(other):
                graph.addEdge(index, other.getIndex(), calculate_distance(hydrant.getLocation(), other.getLocation()))

        hydrants_cola.append(hydrant)

    connections,cost = graph.PrimMST()

    for edge in connections:
        u, v, distance = edge
        folium.PolyLine(locations=[hydrants_cola[u].getLocation(), hydrants_cola[v].getLocation()], color='blue', weight=1, opacity=0.5).add_to(m)

    map_path = "hydrants_map.html"
    m.save(map_path)

    return jsonify({
            "map_url": "http://127.0.0.1:5000/api/v1.0/map_prim",
            "total_cost": round(cost,2),
       })

@app.route('/api/v1.0/map_prim')
def map_prim():
     map_path = "hydrants_map.html"
     return send_file(map_path)

@app.route('/api/v1.0/nearHydrants_map' , methods=['GET'])
def nearHydrants_map(coords= None):

   if coords:
       print(coords)
       current_hydrant = Hydrant(0, coords['lat'], coords['lng'], 0)

   geojson_url = "HIDRANTES_PROVCALLAO.geojson"
   map_filepath = "nearHydrants_map.html"
   gdf = gpd.read_file(geojson_url)
   num_hydrants = 1500
   num_hydrants = min(num_hydrants, len(gdf))
   sampled_gdf = gdf.sample(n=num_hydrants, random_state=1)  # Ensure reproducibility with random_state
   sampled_gdf = sampled_gdf.reset_index(drop=True)
   m = folium.Map(location=[-12.050, -77.120], zoom_start=13)
   m.get_root().html.add_child(folium.Element('''<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.min.js"></script>'''))
   marker_cluster = MarkerCluster().add_to(m)
   Fullscreen(position='topright').add_to(m)
   hydrants_cola = []

   hydrant_icon_url = 'https://raw.githubusercontent.com/diegooo01/FindU-Images/00588368ea06164b6fae1447896d8e1c208cbac5/hidrante-de-incendio%20(1).svg'

   for index, row in sampled_gdf.iterrows():
       lon, lat = row['geometry'].coords[0]
       districtId = row['DISTRICT']
       hydrant = Hydrant(districtId, lon, lat, index)
       hydrants_cola.append(hydrant)


       icon = folium.CustomIcon(hydrant_icon_url, icon_size=(30, 30))  # Adjust size as needed

       folium.Marker(location=hydrant.getLocation(),
                     popup=f'Hydrant {row["FID"]}',
                     icon=icon).add_to(marker_cluster)

       if coords:
            if hydrant.isNear(current_hydrant):
                print(current_hydrant.getLocation())
                folium.PolyLine(locations=[hydrant.getLocation(), current_hydrant.getLocation()], color='blue').add_to(m)

   folium.LatLngPopup().add_to(m)


   m.save(map_filepath)

   html = None
   with open(map_filepath, 'r') as mapfile:
       html = mapfile.read()


   map_variable_name = find_variable_name(html, "map_")
   popup_variable_name = find_variable_name(html, "lat_lng_popup_")
   button_html = '''
    <button id="calcularRutasBtn" style="position: absolute; top: 10px; left: 10px; z-index: 999;" onclick="sendCoordinates()">Calcular Rutas</button>
    <script>
            // Función para enviar las coordenadas al backend
            function sendCoordinates() {
                if (marker) {
                    const coords = {
                        latitude: marker.getLatLng().lat,
                        longitude: marker.getLatLng().lng
                    };
                    // Llamada a Flask
                    fetch('/api/v1.0/current_point', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(coords)
                    })
                    .then(response => response.json())
                    .then(data => {
                       document.getElementById('{map_variable_name}').innerHTML = data.mapUrl;
                    })
                    .catch(error => console.error('Error:', error));
                } else {
                    alert("No has creado un nuevo marcador.");
                }
            }
        </script>
        '''

   html = html.replace('<body>', f'<body>{button_html}')


   pstart, pend = find_popup_slice(html)

   with open(map_filepath, 'w') as mapfile:
       mapfile.write(
           html[:pstart] + \
           custom_code(popup_variable_name, map_variable_name) + \
           html[pend:]
       )

   return  send_file(map_filepath)


@app.route('/api/v1.0/current_point', methods=['POST'])
def current_point():
    data = request.get_json()
    lng, lat = data['longitude'], data['latitude']

    return nearHydrants_map({'lat': lat, 'lng': lng})


if __name__ == '__main__':
    app.run(debug=True)