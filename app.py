from flask import Flask
import folium
# from folium.plugins import Search
from env import API_KEY

app = Flask(__name__)


@app.route('/')
def map():
    m = folium.Map(location=[7, 10],
                   zoom_start=4,
                   id='global_monthly',
                   max_zoom=20,
                   tiles='https://tiles.planet.com/basemaps/v1/planet-tiles/nicfi_sample_raw_toa_reflectance/gmap/{{z}}/{{x}}/{{y}}.png?api_key={}'.format(API_KEY),
                   attr='My Data Attribution')
    return m._repr_html_()

# tiles='https://tiles.planet.com/basemaps/v1/planet-tiles/global_monthly_2020_01_mosaic/gmap/{{z}}/{{x}}/{{y}}.png?api_key={}'.format(API_KEY),
# Use commented out tile for full basemap. NICFI is limited and confined to tropical regions.
