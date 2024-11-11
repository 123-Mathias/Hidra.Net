from flask import Flask,send_file,jsonify,url_for,request,send_from_directory
from flask_cors import CORS
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster,Fullscreen
from prim import prim,calculate_distance
from GraphPrim import GraphPrim
from GraphDijkstra import GraphDijkstra
import os
import gpxpy
import gpxpy.gpx
import osmnx as ox
import networkx as nx
import random
ox.settings.log_console = True
ox.settings.use_cache = False
random.seed(45)
class Hydrant:
    def __init__(self, level, lon, lat,index):
        self.level = level
        self.lon = lon
        self.lat = lat
        self.index = index

    def getIndex(self):
        return self.index

    def getLocation(self):
        return [self.lat, self.lon]

    def isLevelRequired(self, level):
        return self.level == level

    def isNear(self, other,range):
        return calculate_distance(self.getLocation(), other.getLocation()) <= range

app = Flask(__name__,
            static_folder = "../dist",)
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

        hydrant = Hydrant(0, lon, lat, index)

        icon = folium.CustomIcon(hydrant_icon_url, icon_size=(30, 30))  # Adjust size as needed

        folium.Marker(location=hydrant.getLocation(),
                      popup=f'Hydrant {row["FID"]}',
                      icon=icon).add_to(marker_cluster)

        for other in hydrants_cola:
            if hydrant.isNear(other,600):
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

@app.route('/api/v1.0/nearHydrants_map', methods=['GET'])
def nearHydrants_map(lat=None, lng=None):

    if coordinates['lat'] and coordinates['lng']:
        current_hydrant = Hydrant(None, coordinates['lng'], coordinates['lat'], None)
        hydrants_near = [current_hydrant]

    else:
        current_hydrant = None

    geojson_url = "HIDRANTES_PROVCALLAO.geojson"
    map_filepath = "nearHydrants_map.html"
    gdf = gpd.read_file(geojson_url)
    num_hydrants = 1500
    num_hydrants = min(num_hydrants, len(gdf))
    sampled_gdf = gdf.sample(n=num_hydrants, random_state=1)  # Ensure reproducibility with random_state
    sampled_gdf = sampled_gdf.reset_index(drop=True)
    if(current_hydrant): m = folium.Map(location=current_hydrant.getLocation(), zoom_start=18)
    else: m = folium.Map(location=[-12.050, -77.120], zoom_start=16)
    m.get_root().html.add_child(folium.Element('''<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.min.js"></script>'''))
    marker_cluster = MarkerCluster().add_to(m)
    if current_hydrant:
       custom_icon = folium.CustomIcon(icon_image='../public/map-icons/fire-alert-icon.png', icon_size=(32, 32))
       folium.Marker(
           location=[current_hydrant.getLocation()[0], current_hydrant.getLocation()[1]],
           popup='Current Hydrant',
           icon=custom_icon
       ).add_to(m)

    Fullscreen(position='topright').add_to(m)


    hydrant_icon_url = [
    '../public/map-icons/hidrant-icon-low-level.png',
    '../public/map-icons/hidrant-icon-mid-level.png',
    '../public/map-icons/hidrant-icon-high-level.png',
    ]

    for index, row in sampled_gdf.iterrows():
        lon, lat = row['geometry'].coords[0]
        level = random.randint(0, 2)
        hydrant = Hydrant(level, lon, lat, index)


        icon = folium.CustomIcon(hydrant_icon_url[level], icon_size=(30, 30))  # Adjust size as needed

        folium.Marker(location=hydrant.getLocation(),
                     popup=f'Hydrant {row["FID"]}',
                     icon=icon).add_to(marker_cluster)

        if current_hydrant:
            if hydrant.isNear(current_hydrant,300):
                hydrants_near.append(hydrant)

    if current_hydrant:
        G = ox.graph_from_point((current_hydrant.getLocation()[0],current_hydrant.getLocation()[1]), dist=1000, network_type='drive')
        graph = GraphDijkstra(len(hydrants_near))

        for i in range(len(hydrants_near)):
            for j in range(i+1, len(hydrants_near)):

                orig_node = ox.distance.nearest_nodes(G, hydrants_near[i].getLocation()[1], hydrants_near[i].getLocation()[0])
                dest_node = ox.distance.nearest_nodes(G, hydrants_near[j].getLocation()[1], hydrants_near[j].getLocation()[0])
                if(nx.has_path(G, orig_node, dest_node)):
                    shortest_path = nx.shortest_path(G, source=orig_node, target=dest_node, weight='length')
                    shortest_distance = nx.shortest_path_length(G, source=orig_node, target=dest_node, weight='length')
                    route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in shortest_path]
                    graph.addEdge(i, j, shortest_distance)
                    graph.addRouteCoords(i,j,route_coords)
                else:
                    print(f"No hay camino entre {i} y {j}")

        mat = graph.getMatrix()
        for line in mat: print(line)
        path ,cost = graph.Dijkstra(0)
        colors = ["blue", "green", "red", "purple", "orange", "darkblue", "darkgreen", "darkred", "darkpurple", "cadetblue"]
        i = 0

        for v,u in enumerate(path):
            if u !=-1:
                color = colors[i]
                folium.PolyLine(graph.getRouteCoords(u,v), color=color, weight=5, opacity=0.7).add_to(m)
                i = i + 1
                if(i>=len(colors)): i = 0


    folium.LatLngPopup().add_to(m)

    m.save(map_filepath)

    html = None
    with open(map_filepath, 'r') as mapfile:
        html = mapfile.read()

    map_variable_name = find_variable_name(html, "map_")
    popup_variable_name = find_variable_name(html, "lat_lng_popup_")
    button_html = '''
    <button id="calcularRutasBtn" style="position: absolute; top: 10px; left: 10px; z-index: 999;" onclick="sendCoordinates()">Guardar coordenadas</button>
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
                         alert(data);
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
    coordinates['lat'] = data['latitude']
    coordinates['lng'] = data['longitude']
    print(coordinates)

    return "Coordenadas recibidas correctamente."
coordinates = { 'lat': None, 'lng': None }


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)