import pandas as pd
import requests
from api_key import api_key

df =pd.read_csv("Data/mrgdata.csv")
df.head()

lat = []
lng = []

for x in df["Lat_bp"]:
    lat.append(x)
for y in df["Lng_bp"]:
    lng.append(y)

lat_lng_str = []
lat_lng = zip(lat, lng)
list(lat_lng)[0][0]

    
for index, row in df.iterrows():
    lat = row["Lat_bp"]
    lng = row["Lng_bp"]
    lat_lng_str.append(f"{lat}, {lng}")

lat_lng_str

fast_food_data = []
for x in lat_lng_str: 
    try:
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json", params={
            "location": x,
            "radius": 800,
            "keyword": "fast food",
            "key": api_key})
        
        fast_food_data.append(len(r.json()["results"]))
    except: 
        fast_food_data.append(0)
        
df["Number of Fast Food"] = fast_food_data

df.to_csv("Data/mrgdata_food.csv")