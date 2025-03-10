import geopandas as gpd
import folium
import requests
from shapely.geometry import box, Point
from django.shortcuts import render
from .models import WeatherData  # Import the model to store data

# Define the bounding box (World map or specific region)
MIN_LON, MIN_LAT, MAX_LON, MAX_LAT = -180, -90, 180, 90  # Full world grid
GRID_SIZE = 10  # Adjust the grid size (degrees)

def create_grid():
    """Generate grid cells over the map using GeoPandas."""
    grid_cells = []
    for lon in range(MIN_LON, MAX_LON, GRID_SIZE):
        for lat in range(MIN_LAT, MAX_LAT, GRID_SIZE):
            cell = box(lon, lat, lon + GRID_SIZE, lat + GRID_SIZE)
            grid_cells.append(cell)

    # Convert to GeoDataFrame
    grid = gpd.GeoDataFrame(geometry=grid_cells, crs="EPSG:4326")
    return grid

def fetch_weather(lat, lon):
    """Fetch weather data from OpenWeatherMap API."""
    API_KEY = "your_api_key_here"  # Replace with your API key
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Returns weather JSON response
    return None

from .models import WeatherData

def load_map(request):
    """Load grid map and stored weather data for display."""
    weather_data = WeatherData.objects.all()  # Fetch stored weather data

    return render(request, "maps/map.html", {"weather_data": weather_data})


