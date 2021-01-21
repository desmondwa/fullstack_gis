from flask import Flask
import folium
from final.env import API_KEY

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


@app.route('/')
def map():
    m = folium.Map(location=[30, -1],
                   zoom_start=10,
                   id='global_monthly',
                   max_zoom=20,
                   tiles='https://tiles.planet.com/basemaps/v1/planet-tiles/global_monthly_2020_01_mosaic/gmap/{{z}}/{{x}}/{{y}}.png?api_key={}'.format(API_KEY),
                   attr='My Data Attribution')
    return m._repr_html_()
