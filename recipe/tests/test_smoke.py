import folium
from folium.plugins import HeatMap

def test_basic_map_renders_div():
    m = folium.Map(location=[0, 0], zoom_start=1)
    html = m.get_root().render()
    assert '<div class="folium-map"' in html


def test_heatmap_plugin_renders():
    m = folium.Map(location=[0, 0], zoom_start=1)
    HeatMap([[0, 0, 1], [10, 10, 2]]).add_to(m)
    html = m.get_root().render().lower()
    assert "leaflet_heat.min.js" in html or "leaflet.heat" in html
    assert "heatlayer(" in html


def test_geojson_empty_ok():
    gj = folium.GeoJson({"type": "FeatureCollection", "features": []})
    m = folium.Map(location=[0, 0], zoom_start=1)
    gj.add_to(m)
    html = m.get_root().render()
    assert "featurecollection" in html.lower()
