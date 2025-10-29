import folium

# Grundkarte: zentriert auf Deutschland (Übersicht)
m = folium.Map(location=[51.1657, 10.4515], zoom_start=6, tiles="OpenStreetMap")
folium.TileLayer("CartoDB positron", name="Carto Light").add_to(m)

# Erzwinge passende Ansicht für Deutschland (BBox: N,E / S,W)
germany_bbox = [[55.1, 5.8], [47.2, 15.2]]
m.fit_bounds(germany_bbox, padding=(20,20))

# Beispielmarker / Inhalt...
# ...existing code...

# Karte speichern
m.save("map_1_basiskarte.html")
print("Gespeichert: map_1_basiskarte.html")