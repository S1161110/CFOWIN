import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
st.set_page_config(layout="wide")
st.title("Leafmap - Uß (Vector) + | (Raster)")
# --- 1. | (COG) ---
# Ï:Nö SRTM DEM (|ß)
cog_url = "https://github.com/opengeos/leafmap/raw/master/examples/data/cog.tif"
# --- 2. Uß (GDF) ---
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
gdf = gpd.read_file(url)
# --- 3. W ---
m = leafmap.Map(center=[0, 0], zoom=2)
# --- 4. ò/W ---
# ò/|W (COG)
m.add_raster(
cog_url,
palette="terrain", # o "terrain" () 
layer_name="Global DEM (Raster)"
)
# ò/UßW (GDF)
m.add_gdf(
gdf,
layer_name="_} (Vector)",
style={"fillOpacity": 0, "color": "black", "weight": 0.5} # ún,}
)
# --- 5. ×v ---
m.add_layer_control()
m.to_streamlit(height=700)