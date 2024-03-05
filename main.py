import requests, os, sys
from rich import print
from rich.table import Table
from datetime import datetime
from helpers import beautify, menu, getInput

# API base url
URL = "https://api.weatherapi.com/v1/"

# API key
with open(".key.txt") as file:
    KEY = file.read()

# Main Function
def main():

    # Print welcoming menu
    os.system("cls")
    print("[cyan]Welcome to my Weather App! ^^")

    while True:
        
        menu("base")
        option = getInput("option")

        match option:
            # Current Temp
            case 1:
                getCurrentTemp()
            case 2:
                dayForecast()
            case 3:
                sevenDaysForecast()
            case 4:
                sys.exit()
                
# Function for current temperature
@beautify
def getCurrentTemp(KEY=KEY, URL=URL):

    # Altering url to get current data
    URL += ("current.json")

    city = input("City: ")

    # Call API
    response = requests.get(URL, params={"key": KEY, "q": city})
    if response:
        # Extract relevant data from JSON object
        temp = response.json()["current"]["temp_c"]

        print(f"\n[cyan]It's currently {temp} C degrees in {city}[/cyan]\n")
    else:
        print("[red]Invalid city name, use only english letters")

@beautify
def dayForecast(KEY=KEY, URL=URL):
    # Altering url to get current data
    URL += ("forecast.json")

    city = input("City: ")

    currentDate = datetime.today().date()
    
    # Call API
    response = requests.get(URL, params={"key": KEY, "q": city})
    if response:
        hours = {}
        
        # Extract relevant data from JSON object
        for x in range(24):
            hours[str(x)] = response.json()["forecast"]["forecastday"][0]["hour"][x]["temp_c"]
        
        table = Table(title = f"\nDate: {currentDate}")

        table.add_column("Hour", justify="center", style="cyan", no_wrap=True)
        table.add_column("Degrees", justify="center", style="cyan", no_wrap=True)

        for id in hours:
            hour = id
            if int(id) < 10:
                hour = '0' + id
            table.add_row(hour, f"{hours[id]} C")
        
        print(table)
    else:
        print("[red]Invalid city name, use only english letters")

@beautify
def sevenDaysForecast(KEY=KEY, URL=URL):
    # Altering url to get current data
    URL += ("forecast.json")

    city = input("City: ")
    
    # Call API
    response = requests.get(URL, params={"key": KEY, "q": city, "days": 7})
    if response:
        response = response.json()["forecast"]["forecastday"]
        avgTemp = {}

        for day in range(7):
            avgTemp[response[day]["date"]] = response[day]["day"]["avgtemp_c"]

        table = Table(title="\nAverage Temp for next 7 days")
                
        table.add_column("Day", justify = "center", style = "cyan", no_wrap = True)
        table.add_column("Average Temperature", justify = "center", style = "cyan", no_wrap = True)

        for day in avgTemp:
            table.add_row(day, f"{avgTemp[day]} C")
        
        print(table)
    else:
        print("[red]Invalid city name, use only english letters")

if __name__ == "__main__":
    main()