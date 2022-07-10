import folium
from folium.plugins import MousePosition

def create_map(ERB, DESTINY, radius):
    radius = radius * 1e3 #Conversão para KM
    map_folium = folium.Map(location=ERB, zoom_start=11.3)

    folium.Marker(location=ERB,
              popup='ERB',
              icon=folium.Icon(color='red', icon='globe')
    ).add_to(map_folium)

    folium.Marker(location=DESTINY,
              popup='Destino',
              icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(map_folium)

    points = (ERB, DESTINY)
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map_folium)

    folium.Circle(
        location=ERB,
        radius=radius,
        color='blue',
        fill=True,
        opacity=0.1,
        fill_color='green'
    ).add_to(map_folium)

    folium.Circle(
        location=ERB,
        radius=radius/2,
        color='red',
        fill=True,
        opacity=0.5,
        fill_color='yellow'
    ).add_to(map_folium)

    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"

    MousePosition(
        position="bottomleft",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(map_folium)

    popup_lat_long = folium.LatLngPopup()
    map_folium.add_child(popup_lat_long)

    return map_folium
