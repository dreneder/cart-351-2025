import requests
import random

# imports a dictionary of 50 cities
import json

with open("project_1/cities.json", "r", encoding="utf-8") as f:
    cities = json.load(f)

# this one will be used for question 2
randomCities2 = random.randint(1, len(cities) - 1)
randomCity2 = cities[randomCities2]['city']
randomCountry2 = cities[randomCities2]['country']

# personal API token
token = '857f95d7ebcf73e281afac1f85325761f53404a5'

    # url string used to get the request
url = "https://api.waqi.info/search/"


# this is the get request for the API, which takes the url and fills the rest in with my API key and the keyword request
response = requests.get(url, params={"token": token, "keyword": randomCity2})

# after getting the response from the API, we will convert it into json so that we can access the data
results = response.json()
# access the relevant data
responseData = results['data']
# get the unique city ID for detailed feed
city_id = responseData[0]['uid']
# city_id = 3307
url_feed = f"https://api.waqi.info/feed/@{city_id}"
# request the detailed feed for the city
response_feed = requests.get(url_feed, params={"token": token})
results_feed = response_feed.json()
response_data_feed = results_feed['data']

# print(f'{randomCity2}, {randomCountry2}')
print(randomCity2,response_data_feed['iaqi'])

q3answer = response_data_feed['dominentpol']
q3option = [q3answer]

# dictionary of pollutants available in the iaqi
pollutants = {
    'co': 'Carbon Monoxide',
    'no2': 'Nitrogen Dioxide',
    'o3': 'Ozone',
    'pm25': 'Particulate Matter (≤ 2.5 µm)',
    'pm10': 'Particulate Matter (≤ 10 µm)',
    'so2': 'Sulfur Dioxide'
}

# adds 3 random pollutants that are not the dominant one
other_options = [p for p in pollutants.keys() if p != q3answer.strip().lower()]
q3option.extend(random.sample(other_options, 3))

# shuffles the list
random.shuffle(q3option)

print(q3option[0].strip().upper())
print(q3answer)
print(f'{q3answer.upper()} - {pollutants[q3answer]}')


# print(response_data_feed['dominentpol'])



# # filter only real pollutants
# filtered = {k: v['v'] for k, v in data.items() if k in pollutants}

# # get 4 largest
# top4 = sorted(filtered.items(), key=lambda x: x[1], reverse=True)[:4]


# for pol, val in top4:
#     print(f"{pol}: {val}")












# import requests

# randomCity = "new york"

# # personal API token
# token = '857f95d7ebcf73e281afac1f85325761f53404a5'

# # base URL for the search
# url = "https://api.waqi.info/search/"

# # 1. make the search request
# response = requests.get(url, params={"token": token, "keyword": randomCity})
# results = response.json()

# # 2. get the list of all stations for that city
# responseData = results["data"]

# # 3. go through each station until we find one that actually has pollutant data
# city_id = None
# for item in responseData:
#     uid = item["uid"]
#     url_feed = f"https://api.waqi.info/feed/@{uid}"
#     feed = requests.get(url_feed, params={"token": token}).json()
    
#     # if the feed has pollutant data, use this one
#     if "iaqi" in feed.get("data", {}):
#         city_id = uid
#         response_data_feed = feed["data"]
#         break  # stop once we find the first valid one

# if city_id is None:
#     print("No data found for this city.")
# else:
#     # 4. get AQI
#     aqi = response_data_feed.get("aqi", "N/A")

#     # 5. extract pollutant data safely
#     pollutants = response_data_feed.get("iaqi", {})
#     pollutant_values = {}

#     for p, v in pollutants.items():
#         if "v" in v:
#             pollutant_values[p] = v["v"]

#     # 6. sort by value, get top 4
#     top4 = sorted(pollutant_values.items(), key=lambda x: x[1], reverse=True)[:4]

#     # 7. print results
#     print(f"{randomCity.title()} AQI: {aqi}")
#     print("Top pollutants:")
#     for name, value in top4:
#         print(f" - {name}: {value}")
