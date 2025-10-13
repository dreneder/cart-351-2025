import requests
import random
import json

from rich import print
from rich import box
from rich.padding import Padding
from rich.table import Table
from rich.console import Console
console = Console()

# load local cities file
with open("project_1/cities.json", "r", encoding="utf-8") as f:
    cities = json.load(f)

# this one, well, you guessed it...
randomCities_Q3 = random.sample(range(len(cities)), 4)

# personal API token
token = '857f95d7ebcf73e281afac1f85325761f53404a5'
url = "https://api.waqi.info/search/"

# dictionary of pollutants available in the iaqi
pollutants = {
    'co': 'Carbon Monoxide',
    'no2': 'Nitrogen Dioxide',
    'o3': 'Ozone',
    'pm25': 'Particulate Matter (≤ 2.5 µm)',
    'pm10': 'Particulate Matter (≤ 10 µm)',
    'so2': 'Sulfur Dioxide'
}



randomCity_Q3 = "montreal"

# this is the get request for the API, which takes the url and fills the rest in with my API key and the keyword request
response_Q3 = requests.get(url, params={"token": token, "keyword": randomCity_Q3})

# after getting the response from the API, we will convert it into json so that we can access the data
results_Q3 = response_Q3.json()

# access the relevant data
responseData_Q3 = results_Q3['data']

# # filter out stations with no AQI
# responseData_Q3 = [s for s in responseData_Q3 if s['iaqi'][randomPol] != '-']

# # prefer stations with city key if possible
# preferred_stations_Q3 = [s for s in responseData_Q3 if 'city' in s['station']]

# # get the unique city ID for detailed feed
city_id_Q3 = responseData_Q3[0]['uid']
url_feed_Q3 = f"https://api.waqi.info/feed/@{city_id_Q3}"

# # request the detailed feed for the city
response_feed_Q3 = requests.get(url_feed_Q3, params={"token": token})
results_feed_Q3 = response_feed_Q3.json()
response_data_feed_Q3 = results_feed_Q3['data']
# extract the AQI
print(response_data_feed_Q3['aqi'])










if question != 4:
    for item in randomCities_Q3:
        # get the city from the random selection
        randomCity_Q3 = cities[item]['city']
        randomCountry_Q3 = cities[item]['country']

        # gets a random pollutant
        randomPol = random.choice(list(pollutants.keys()))


        try:
            # this is the get request for the API, which takes the url and fills the rest in with my API key and the keyword request
            response_Q3 = requests.get(url, params={"token": token, "keyword": randomCity_Q3})

            # after getting the response from the API, we will convert it into json so that we can access the data
            results_Q3 = response_Q3.json()

            # access the relevant data
            responseData_Q3 = results_Q3['data']

            # filter out stations with no AQI
            responseData_Q3 = [s for s in responseData_Q3 if s['iaqi'][randomPol] != '-']

            # prefer stations with city key if possible
            preferred_stations_Q3 = [s for s in responseData_Q3 if 'city' in s['station']]

            # picks the first preferred station, fallback to first available
            if preferred_stations_Q3:
                station_Q3 = preferred_stations_Q3[0]
            elif responseData_Q3:
                station_Q3 = responseData_Q3[0]
            else:
                print("Error fetching AQI data")
                continue

            # get the unique city ID for detailed feed
            city_id_Q3 = station_Q3['uid']
            url_feed_Q3 = f"https://api.waqi.info/feed/@{city_id_Q3}"

            # request the detailed feed for the city
            response_feed_Q3 = requests.get(url_feed_Q3, params={"token": token})
            results_feed_Q3 = response_feed_Q3.json()
            response_data_feed_Q3 = results_feed_Q3['data']

            # extract the AQI
            iaqi_Q3 = response_data_feed_Q3['iaqi'][randomPol]

            # store city, country, AQI, and top pollutants in the list
            Q3option.append({
                "city": randomCity_Q3,
                "country": randomCountry_Q3,
                "poll": iaqi_Q3
            })

            # this prints a loading percentages because the program takes a while to fetch all the data
            loading += 1
            if loading > loading_steps:
                loading = loading_steps
            show_loading_bar(loading, loading_steps)  
        

        # print error if data fetch fails
        except Exception as e:
            print("Error fetching AQI data")

    # calculates the higest AQI
    def get_q3pol(Q3option):
        return q3option['iaqi'][randomPol]

    q3answer = max(q3option, key=get_q3pol)
