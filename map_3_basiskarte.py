import folium
from folium.features import DivIcon

# Grundkarte: zentriert auf Deutschland (Übersicht)
m = folium.Map(location=[51.1657, 10.4515], zoom_start=6, tiles="OpenStreetMap")
folium.TileLayer("CartoDB positron", name="Carto Light").add_to(m)

# Reiseroute (in Reihenfolge) - Schaidt -> Sölden -> Leogang -> zurück Schaidt
route = [
    ("Schaidt", (49.1167, 8.2833)),
    ("Sölden", (46.9680, 11.0074)),
    ("Leogang", (47.4626, 12.6364)),
    ("Schaidt (Ende)", (49.1167, 8.2833))
]

# Polyline einzeichnen
coords = [pt for name, pt in route]
folium.PolyLine(coords, color="blue", weight=4, opacity=0.8).add_to(m)

bounds = []
for i, (name, (lat, lon)) in enumerate(route, start=1):
    bounds.append([lat, lon])

    # nummeriertes Icon (DivIcon)
    icon = DivIcon(
        icon_size=(30, 30),
        icon_anchor=(15, 15),
        html=f'''<div style="background:#fff;border:1px solid #2b7be4;color:#0b5bd7;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:700">{i}</div>'''
    )

    folium.Marker(
        location=[lat, lon],
        icon=icon,
        tooltip=f"{i}. {name}",
        popup=folium.Popup(f"<strong>{i}. {name}</strong><br>Koordinaten: {lat:.5f}, {lon:.5f}", max_width=300)
    ).add_to(m)

# Ansicht an alle Marker anpassen — aber erzwungen auf Deutschland-Übersicht
germany_bbox = [[55.1, 5.8], [47.2, 15.2]]
m.fit_bounds(germany_bbox, padding=(30, 30))

folium.LayerControl(collapsed=False).add_to(m)

# Karte speichern
m.save("map_3_reiseroute.html")
print("Gespeichert: map_3_reiseroute.html")