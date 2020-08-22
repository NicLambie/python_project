import json
from datetime import datetime

import json with open(filepath) as json_file:
jason_data=json.load(json_file)

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

temp = #input from json

def __init__(self, temp):
        self.temp = temp

def format_temperature(temp):
    temp = 
    DEGREE_SYBMOL = "degrees celcius."
    return f"{temp}{DEGREE_SYBMOL}"
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

temp(format_temperature)



def convert_date(iso_string):
    iso_string = x
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    result = float((self.temp - 32) * 5 / 9)
    return result

    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    pass




def calculate_mean(total, num_items):
    total = x
    num_items = y
    return total / num_items
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    
    return total / num_items


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
    # print(json_data["DailyForecasts"]["Temperature"]["Minimum"])

    weather = json_data["DailyForecasts"]

    for forecast in weather:
        daily_date = forecast["Date"]
        formatted_date = convert_date(daily_date)
        print(formatted_date)
    
        # formatted data


process_weather("data/forecast_5days_a.json")

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





