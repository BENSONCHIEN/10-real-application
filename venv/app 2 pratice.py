import folium
# map = folium.Map(location = [80,-100])
#
# map = folium.Map(location = [80,-100],zoom_start= 6)
# fg = folium.FeatureGroup(name = "My Map")

#adding multiple point
# fg.add_child(folium.Marker(location = [38.2,-99.1],popup = "Hi I am a Marker",icon = folium.Icon(color = 'green')))
# fg.add_child(folium.Marker(location = [37.2,-97.1],popup = "Hi I am a Marker",icon = folium.Icon(color = 'green')))

#更方便
# for coordinates in [[38.2,-99.1],[39.2,-97.1]]:
#     fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

#adding points ftom files
import pandas as pd
data = pd.read_csv("Volcanoes.txt")
print(data.columns)
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

map = folium.Map(location = [38.58,-99.09],zoom_start=6)

# for lt,ln in zip(lat,lon):
#     fg.add_child(folium.Marker(location=[lt,ln], popup=el, icon=folium.Icon(color='green')))

#Improve popup

def elev_color(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 3000:
        return "orange"
    else :
        return "red"

fgv = folium.FeatureGroup(name = "Volcanoes")

#volcanoes
#Marker to CircleMarker
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=str(el)+"m",
    fill_color=elev_color(el),color = 'grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name ="Population")

#Geojson Data
fgp.add_child(folium.GeoJson(data = (open('World.json','r',encoding = 'utf-8-sig').read()),
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if x['properties']['POP2005']<20000000 else 'red '}))

map.add_child(fgv) # Volcanoes
map.add_child(fgp)         #population
map.add_child(folium.LayerControl())

map.save("Map1.html")