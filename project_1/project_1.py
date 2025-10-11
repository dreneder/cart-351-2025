'''
CART 351 - Project 1: CREATIVE CODING IN THE TERMINAL
"Who Wants to Breath a Million Air"
By André Neder
Student ID: 40208953

This is a minigame in the terminal using the World Air Quality Index API to quiz the player on a few questions that mimics the game show "How to Be a Millionaire".
The game uses:
The WAQI API: https://aqicn.org/api/
ASCII Art Library for python: https://pypi.org/project/art/
Rich Library for python: https://pypi.org/project/rich/
Colorama: https://pypi.org/project/colorama/

Progress bar adapted from NeuralNine: https://www.youtube.com/watch?v=x1eaT88vJUA

Chat GPT 5o was used two times to mass diversify variables

Enjoy!
'''

# personal API token
token = '857f95d7ebcf73e281afac1f85325761f53404a5'

# url string used to get the request
url = "https://api.waqi.info/search/"

# prints the title of the game
# importing libraries from python
import random
import math

# importing art library
from art import text2art

# importing colorama

# importing parameters from the rich library
from rich import print
from rich import box
from rich.padding import Padding
from rich.table import Table
from rich.console import Console
console = Console()

# importing the from the WAQI APIllibraries
import requests
console.print(text2art("Who  Wants  to  Breath  a"), style = "bold yellow", highlight=False)
console.print(text2art("MILLION  AIR", font = "univers"), style = "bold bright_green", highlight=False)

# prints welcome message
print("""
      [bold]Welcome to[/bold] [bold yellow] Who Wants to Breath a[/bold yellow] [bold white on green] Million Air [/bold white on green]
      
      [bold white]In this is a game you have to answer questions to win your [/bold white][bold yellow]prize[/bold yellow]

      To answer the questions, either input the answer or option number and [bold blue on white]ENTER[/bold blue on white]


      Please insert [bold blue on white]PLAY[/bold blue on white] to start or [bold white on red]EXIT[/bold white on red] or [bold white on red]QUIT[/bold white on red] at any moment to leave

      """)

# a variable for the points
score = 0

# and a variable for questions
question = 0

# to give user feedback while it loads
loading = 0
loading_steps = 7 # number of items loaded

# function to calculate the percentage loaded, this took way longer than anticipated...
def show_loading_bar(loading, loading_steps):
    bar_length = 50 
    filled_length = int(bar_length * loading // loading_steps)
    percent = (loading / loading_steps) * 100
    bar = '█' * filled_length + '-' * (bar_length - filled_length) 
    if loading == loading_steps:
        print(f'\r[bold white]Loading [/bold white][bold green]{bar} {percent:.2f}%[/bold green]', end="\n")
    else:
        print(f'\r[bold white]Loading [/bold white][bold red]{bar} {percent:.2f}%[/bold red]', end="\r")

# if there is a fetching error, the program will terminate
fetchError = False

while question == 0:
    answer = input().strip().lower()

    if answer in ["play", "y", "yes"]:
        break
    elif answer in ["exit", "quit", "n", "no"]:
        print("Good bye!")
        question = 4
        break
    else:
        print("[bold white on red]Invalid input[/bold white on red]")

# imports a dictionary of 50 cities
import json

with open("project_1/cities.json", "r", encoding="utf-8") as f:
    cities = json.load(f)

# generating random number for four cities
randomCities_Q1 = random.sample(range(len(cities)), 4)

# this ones will be used for question 2
randomCities_Q2 = random.randint(1, len(cities) - 1)
randomCity_Q2 = cities[randomCities_Q2]['city']
randomCountry_Q2 = cities[randomCities_Q2]['country']

# this one, well, you guessed it...
randomCities_Q3 = random.sample(range(len(cities)), 4)

# lists for each question
q1option = []
q2option = []
q3option = []

# QUESTION 1------------------------------------------------------------------------------------------------------------------------------------

for item in randomCities_Q1:
    # get the city from the random selection
    randomCity_Q1 = cities[item]['city']
    randomCountry_Q1 = cities[item]['country']

    try:
        # this is the get request for the API, which takes the url and fills the rest in with my API key and the keyword request
        response_Q1 = requests.get(url, params={"token": token, "keyword": randomCity_Q1})

        # after getting the response from the API, we will convert it into json so that we can access the data
        results_Q1 = response_Q1.json()

        # access the relevant data
        responseData_Q1 = results_Q1['data']

        # filter out stations with no AQI
        responseData_Q1 = [s for s in responseData_Q1 if s['aqi'] != '-']

        # prefer stations with city key if possible
        preferred_stations_Q1 = [s for s in responseData_Q1 if 'city' in s['station']]

        # picks the first preferred station, fallback to first available
        if preferred_stations_Q1:
            station_Q1 = preferred_stations_Q1[0]
        elif responseData_Q1:
            station_Q1 = responseData_Q1[0]
        else:
            print("Error fetching AQI data")
            continue

        # get the unique city ID for detailed feed
        city_id_Q1 = station_Q1['uid']
        url_feed_Q1 = f"https://api.waqi.info/feed/@{city_id_Q1}"

        # request the detailed feed for the city
        response_feed_Q1 = requests.get(url_feed_Q1, params={"token": token})
        results_feed_Q1 = response_feed_Q1.json()
        response_data_feed_Q1 = results_feed_Q1['data']

        # extract the AQI
        aqi_Q1 = response_data_feed_Q1['aqi']

        # store city, country, AQI, and top pollutants in the list
        q1option.append({
            "city": randomCity_Q1,
            "country": randomCountry_Q1,
            "aqi": aqi_Q1
        })

        # this prints a loading percentages because the program takes a while to fetch all the data
        loading += 1
        if loading > loading_steps:
            loading = loading_steps
        show_loading_bar(loading, loading_steps)
        


    # print error if data fetch fails
    except Exception as e:
        print("Error fetching AQI data")
        question = 4
        fetchError = True


# calculates the higest AQI
def get_aqi(q1option):
    return q1option['aqi']

q1answer = max(q1option, key=get_aqi)


# QUESTION 2------------------------------------------------------------------------------------------------------------------------------------

try:
    # get request for the API with token and city keyword
    response_Q2 = requests.get(url, params={"token": token, "keyword": randomCity_Q2})
    results_Q2 = response_Q2.json()

    # access the relevant data
    responseData_Q2 = results_Q2['data']

    # filter out stations with no AQI
    responseData_Q2 = [s for s in responseData_Q2 if s['aqi'] != '-']

    # prefer stations with city key if possible
    preferred_stations_Q2 = [s for s in responseData_Q2 if 'city' in s['station']]

    # picks the first preferred station, fallback to first available
    if preferred_stations_Q2:
        station_Q2 = preferred_stations_Q2[0]
    elif responseData_Q2:
        station_Q2 = responseData_Q2[0]
    else:
        print("Error fetching AQI data")
        question = 4
        raise Exception("No valid station found")

    # get the unique city ID for detailed feed
    city_id_Q2 = station_Q2['uid']
    url_feed_Q2 = f"https://api.waqi.info/feed/@{city_id_Q2}"

    # request the detailed feed for the city
    response_feed_Q2 = requests.get(url_feed_Q2, params={"token": token})
    results_feed_Q2 = response_feed_Q2.json()
    response_data_feed_Q2 = results_feed_Q2['data']

    # extract dominant pollutant
    q2answer = response_data_feed_Q2.get('dominentpol', '').strip().lower()

    # dictionary of pollutants available in the iaqi
    pollutants_Q2 = {
        'co': 'Carbon Monoxide',
        'no2': 'Nitrogen Dioxide',
        'o3': 'Ozone',
        'pm25': 'Particulate Matter (≤ 2.5 µm)',
        'pm10': 'Particulate Matter (≤ 10 µm)',
        'so2': 'Sulfur Dioxide'
    }

    # verify pollutant exists
    if q2answer not in pollutants_Q2:
        print("Error fetching AQI data")
        question = 4
        fetchError = True
    else:
        # build options list
        q2option = [q2answer]
        other_options_Q2 = [p for p in pollutants_Q2.keys() if p != q2answer]
        q2option.extend(random.sample(other_options_Q2, 3))
        random.shuffle(q2option)

        show_loading_bar(loading_steps, loading_steps)
        question += 1

# print error if data fetch fails
except Exception as e:
    print("Error fetching AQI data")
    question = 4
    fetchError = True


# QUESTION 3------------------------------------------------------------------------------------------------------------------------------------



# QUESTION LOOPS------------------------------------------------------------------------------------------------------------------------------------


#--------------- loops question 1
while question == 1:
    # prints question 1 in a table from rich
    console.print(text2art("Question  1"), style = "bold yellow", highlight=False)
    q1table = Table(
        title = '[bold]Which of the following cities has the current worst (highest) Air Quality Index?[/bold]',
        show_header = False,
        pad_edge = True,
        padding = (1,2),
        style = None,
        box = None,
        expand = False
                    )
    q1table.add_column("", style = None)
    q1table.add_column("", style = None)

    q1table.add_row(f'[bold black on blue] 1 [/bold black on blue][bold blue on white]  {q1option[0]['city']} [/bold blue on white]',
                    f'[bold black on blue] 2 [/bold black on blue][bold blue on white] {q1option[1]['city']} [/bold blue on white]')
    q1table.add_row(f'[bold black on blue] 3 [/bold black on blue][bold blue on white] {q1option[2]['city']} [/bold blue on white]',
                    f'[bold black on blue] 4 [/bold black on blue][bold blue on white] {q1option[3]['city']} [/bold blue on white]')

    print(Padding(q1table, (0,0,0,10))) # the table

    answer = input().strip().lower()

    # statement to evaluate the answer
    if answer == q1answer['city'].strip().lower() or (
        answer.isdigit() and int(answer) - 1 == q1option.index(q1answer)
    ):
        print(f'''
                        [bold white on green]Correct![/bold white on green]
              
              The city with the worst AQI is
              [bold white on blue]{q1answer['city']}, {q1answer['country']}[/bold white on blue] with [bold white on blue]{q1answer['aqi']}[/bold white on blue] AQI
              ''')
        question += 1
        score += 1
        break
    elif answer in ["exit", "quit"]:
        print("Good bye!")
        question = 4
        break
    else:
        print(f'''
                        [bold white on red]Wrong![/bold white on red]
              
              The city with the worst AQI is
              [bold white on blue]{q1answer['city']}, {q1answer['country']}[/bold white on blue] with [bold white on blue]{q1answer['aqi']}[/bold white on blue] AQI
              ''')
        question += 1
        break

#--------------- loops question 2
while question == 2:
    # prints question 2 in a table from rich
    console.print(text2art("Question  2"), style = "bold yellow", highlight=False)
    q2table = Table(
        title = f'[bold]What is the highest pollutant of [/bold][bold blue]{randomCity_Q2}, {randomCountry_Q2}[/bold blue][bold]?[/bold]',
        show_header = False,
        pad_edge = True,
        padding = (1,2),
        style = None,
        box = None,
        expand = False
                    )
    q2table.add_column("", style = None)
    q2table.add_column("", style = None)

    q2table.add_row(f'[bold black on blue] 1 [/bold black on blue][bold blue on white]  {q2option[0].strip().upper()} [/bold blue on white]',
                    f'[bold black on blue] 2 [/bold black on blue][bold blue on white] {q2option[1].strip().upper()} [/bold blue on white]')
    q2table.add_row(f'[bold black on blue] 3 [/bold black on blue][bold blue on white] {q2option[2].strip().upper()} [/bold blue on white]',
                    f'[bold black on blue] 4 [/bold black on blue][bold blue on white] {q2option[3].strip().upper()} [/bold blue on white]')

    print(Padding(q2table, (0,0,0,10)))

    answer = input().strip().lower()

    if answer == q2answer.strip().lower() or (
        answer.isdigit() and int(answer) - 1 == q2option.index(q2answer)
    ):
        print(f'''
                        [bold white on green]Correct![/bold white on green]
              
              The highest pollutant in [bold blue]{randomCity_Q2}[/bold blue] is
              [bold white on blue]{q2answer.upper()} - {pollutants_Q2[q2answer]}[/bold white on blue]
              ''')
        question += 1
        score += 1
        break
    elif answer in ["exit", "quit"]:
        print("Good bye!")
        question = 4
        break
    else:
        print(f'''
                        [bold white on red]Wrong![/bold white on red]
              
              The highest pollutant in [bold blue]{randomCity_Q2}[/bold blue] is
              [bold white on blue]{q2answer.upper()} - {pollutants_Q2[q2answer]}[/bold white on blue]
              ''')
        question += 1
        break

#--------------- loops question 3
while question == 3:
    # prints question 2 in a table from rich
    console.print(text2art("Question  3"), style = "bold yellow", highlight=False)
    q2table = Table(
        title = f'[bold]What is the highest pollutant of [/bold][bold blue]{randomCity_Q2}, {randomCountry_Q2}[/bold blue][bold]?[/bold]',
        show_header = False,
        pad_edge = True,
        padding = (1,2),
        style = None,
        box = None,
        expand = False
                    )
    q2table.add_column("", style = None)
    q2table.add_column("", style = None)

    q2table.add_row(f'[bold black on blue] 1 [/bold black on blue][bold blue on white]  {q2option[0].strip().upper()} [/bold blue on white]',
                    f'[bold black on blue] 2 [/bold black on blue][bold blue on white] {q2option[1].strip().upper()} [/bold blue on white]')
    q2table.add_row(f'[bold black on blue] 3 [/bold black on blue][bold blue on white] {q2option[2].strip().upper()} [/bold blue on white]',
                    f'[bold black on blue] 4 [/bold black on blue][bold blue on white] {q2option[3].strip().upper()} [/bold blue on white]')

    print(Padding(q2table, (0,0,0,10)))

    answer = input().strip().lower()

    if answer == q2answer.strip().lower() or (
        answer.isdigit() and int(answer) - 1 == q2option.index(q2answer)
    ):
        print(f'''
                        [bold white on green]Correct![/bold white on green]
              
              The highest pollutant in [bold blue]{randomCity_Q2}[/bold blue] is
              [bold white on blue]{q2answer.upper()} - {pollutants_Q2[q2answer]}[/bold white on blue]
              ''')
        question += 1
        score += 1
        break
    elif answer in ["exit", "quit"]:
        print("Good bye!")
        question = 4
        break
    else:
        print(f'''
                        [bold white on red]Wrong![/bold white on red]
              
              The highest pollutant in [bold blue]{randomCity_Q2}[/bold blue] is
              [bold white on blue]{q2answer.upper()} - {pollutants_Q2[q2answer]}[/bold white on blue]
              ''')
        question += 1
        break

while question == 4:
    if score == 3:
            console.print(text2art("CONGRATULATIONS", font="starwars"), style = "bold yellow", highlight=False)        
            print('''
                        You guessed all the answers right.
                  Now go outside and breath all the air you won!


                  ''')
            console.print(text2art("GOOD BYE", font="straight"), style = "bold blue", highlight=False)        
    elif score :
            console.print(text2art("CONGRATULATIONS", font="starwars"), style = "bold yellow", highlight=False)        
            print('''
                        You guessed some of the answers.
                  You can go outside and breath the air you won,
                                nothing more!


                  ''')
            console.print(text2art("GOOD BYE", font="straight"), style = "bold blue", highlight=False)        
    break