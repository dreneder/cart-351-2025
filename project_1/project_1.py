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

Enjoy!
'''

# importing art library
from art import text2art

# importing parameters from the rich library
from rich import print
from rich.console import Console
console = Console()

# importing the from the WAQI APIllibraries
import requests

#city argument
city = "montreal"

# personal API token
token = '857f95d7ebcf73e281afac1f85325761f53404a5'

# url string used to get the request
url = "https://api.waqi.info/search/"

# this is the get request for the API, which takes the url and fills the rest in with my API key and the keyword request
response = requests.get(url, params={"token": token, "keyword": city})

#after getting the response from the API, we will convert it into json so that we can access the data
results = response.json()

#this prints the entire response from the API
# print(type(results))

# prints the title of the game
console.print(text2art("Who  Wants  to  Breath  a"), style = "bold yellow", highlight=False)
console.print(text2art("MILLION  AIR", font = "univers"), style = "bold bright_green", highlight=False)

# prints welcome message
print("""
      [bold]Welcome to[/bold] [bold yellow] Who Wants to Breath a[/bold yellow] [bold white on green] Million Air [/bold white on green]
      
      [bold white]In this is a game you have to answer questions to win your [/bold white][bold yellow]prize[/bold yellow]

      To answer the questions, either input the answer or option number


      Press [bold blue on white]SPACEBAR[/bold blue on white] to start or [bold white on red]ESCAPE[/bold white on red] to exit

      """)