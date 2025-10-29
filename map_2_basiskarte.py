import folium
from folium import Popup, Icon

# Grundkarte: zentriert auf Deutschland (Übersicht)
m = folium.Map(location=[51.1657, 10.4515], zoom_start=6, tiles="OpenStreetMap")
folium.TileLayer("CartoDB positron", name="Carto Light").add_to(m)

# Marker: Titel, (lat, lon), Farbe, Icon, Popup-HTML
punkte = [
    ("Geburtsort", (49.0069, 8.4037), "red", "info-sign", "<strong>Geburtsort</strong><br>Karlsruhe"),
    ("Heimat", (49.06119, 8.0799), "blue", "info-sign", "<strong>Heimat</strong><br>Schaidt"),
    ("Studienort", (50.0, 8.16), "green", "info-sign", "<strong>Studienort</strong><br>Mainz")
]

bounds = []
for titel, (lat, lon), farbe, icon_name, html in punkte:
    marker = folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(html, max_width=300),
        icon=folium.Icon(color=farbe, icon=icon_name)
    )
    marker.add_to(m)
    bounds.append([lat, lon])

# Immer Deutschland als Übersicht anzeigen (BBox)
germany_bbox = [[55.1, 5.8], [47.2, 15.2]]
m.fit_bounds(germany_bbox, padding=(20, 20))

folium.LayerControl(collapsed=False).add_to(m)

# Karte speichern
m.save("map_2_punkte.html")
print("Gespeichert: map_2_punkte.html")