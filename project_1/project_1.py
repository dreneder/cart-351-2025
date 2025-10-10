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

Enjoy!
'''

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

# to give user feedback while 
loading = 0

def prograss_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' (100 - int(percent))
    print(f"\r|{bar}|{percent:.2f}%", end = "\r")

numbers = [x * 5 for x in range(2000, 3000)]

while question == 0:
    answer = input().strip().lower()

    if answer in ["play", "y", "yes"]:
        question += 1
        print(f'[bold white]Loading [/bold white][bold red]{loading}%[/bold red]')
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
randomCities = random.sample(range(len(cities)), 4)

# this one will be used for question 2
randomCity2 = random.sample(range(len(cities)), 1)

# this one, well, you guessed it...
randomCities3 = random.sample(range(len(cities)), 4)

# lists for each question
q1option = []
q2option = []
q3option = []

for item in randomCities:
    # get the city from the random selection
    randomCity = cities[item]['city']
    randomCountry = cities[item]['country']

    # personal API token
    token = '857f95d7ebcf73e281afac1f85325761f53404a5'

    # url string used to get the request
    url = "https://api.waqi.info/search/"

    try:
        # this is the get request for the API, which takes the url and fills the rest in with my API key and the keyword request
        response = requests.get(url, params={"token": token, "keyword": randomCity})

        # after getting the response from the API, we will convert it into json so that we can access the data
        results = response.json()

        # access the relevant data
        responseData = results['data']

        # filter out stations with no AQI
        responseData = [s for s in responseData if s['aqi'] != '-']

        # prefer stations with city key if possible
        preferred_stations = [s for s in responseData if 'city' in s['station']]

        # picks the first preferred station, fallback to first available
        if preferred_stations:
            station = preferred_stations[0]
        elif responseData:
            station = responseData[0]
        else:
            print("Error fetching AQI data")
            continue

        # get the unique city ID for detailed feed
        city_id = station['uid']
        url_feed = f"https://api.waqi.info/feed/@{city_id}"

        # request the detailed feed for the city
        response_feed = requests.get(url_feed, params={"token": token})
        results_feed = response_feed.json()
        response_data_feed = results_feed['data']

        # extract the AQI
        aqi = response_data_feed['aqi']

        # store city, country, AQI, and top pollutants in the list
        q1option.append({
            "city": randomCity,
            "country": randomCountry,
            "aqi": aqi
        })

        # this prints a loading percentages because the program takes a while to fetch all the data
        loading += 25
        if loading == 100:
            print(randomCity2)
            print(f'[bold white]Loading [/bold white][bold green]{loading}%[/bold green]')
        else:
            print(f'[bold white]Loading [/bold white][bold red]{loading}%[/bold red]')

    # print error if data fetch fails
    except Exception as e:
        print("Error fetching AQI data")
        question = 4


# calculates the higest AQI
def get_aqi(q1option):
    return q1option['aqi']

q1answer = max(q1option, key=get_aqi)

# loops question 1
while question == 1:
    # prints question 1 in a table from rich
    console.print(text2art("Question  ONE"), style = "bold yellow", highlight=False)
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

    q1table.add_row(f'[bold black on blue] 1 [/bold black on blue][bold blue on white]  {q1option[0]['city']} [/bold blue on white]',f'[bold black on blue] 2 [/bold black on blue][bold blue on white] {q1option[1]['city']} [/bold blue on white]')
    q1table.add_row(f'[bold black on blue] 3 [/bold black on blue][bold blue on white] {q1option[2]['city']} [/bold blue on white]',f'[bold black on blue] 4 [/bold black on blue][bold blue on white] {q1option[3]['city']} [/bold blue on white]')

    print(Padding(q1table, (0,0,0,15))) # the table

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
        question = 4
        break

# loops question 2
while question == 2:
    # prints question 2 in a table from rich
    console.print(text2art("Question  TWO"), style = "bold yellow", highlight=False)
    q1table = Table(
        title = '[bold]What is the highest pollutant of (blank) city?[/bold]',
        show_header = False,
        pad_edge = True,
        padding = (1,2),
        style = None,
        box = None,
        expand = False
                    )
    q1table.add_column("", style = None)
    q1table.add_column("", style = None)

    q1table.add_row(f'[bold black on blue] 1 [/bold black on blue][bold blue on white]  {q1option[0]['city']} [/bold blue on white]',f'[bold black on blue] 2 [/bold black on blue][bold blue on white] {q1option[1]['city']} [/bold blue on white]')
    q1table.add_row(f'[bold black on blue] 3 [/bold black on blue][bold blue on white] {q1option[2]['city']} [/bold blue on white]',f'[bold black on blue] 4 [/bold black on blue][bold blue on white] {q1option[3]['city']} [/bold blue on white]')

    print(Padding(q1table, (0,0,0,15)))

    answer = input().strip().lower()

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
        question = 4
        break

while question == 4:
    print('Q4')
    break