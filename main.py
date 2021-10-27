import folium
import requests

m = folium.Map(location=[39.8283, -98.5795], zoom_start=5, tiles="Stamen Terrain")
list_of_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
api_key = "b35f7aab2174724aefd87f94cddd0571"

state_info_dict = {}

for state in list_of_states:
  api_link = f"https://api.openweathermap.org/data/2.5/weather?q={state},%20US&appid={api_key}"
  # There are cities in the US named Kentucky and California that confuse the API, this accounts for it
  if state == "Kentucky":
    api_link = f"https://api.openweathermap.org/data/2.5/weather?q=Lexington,%20Kentucky,%20US&appid={api_key}"
  elif state == "California":
      api_link = f"https://api.openweathermap.org/data/2.5/weather?q=Merced,%20California,%20US&appid={api_key}"

  response = requests.get(api_link).json()
  # Checks to make sure open weather map has the city/state
  state_coords = response["coord"]
  state_weather = response["weather"]
  state_main = response["main"]
  folium.Marker([state_coords["lat"], state_coords["lon"]], popup=state).add_to(m)

m.save("weather_map.html")
