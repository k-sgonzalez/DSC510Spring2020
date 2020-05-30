"""
File DSC510_T303 Week 12 Final Programming Assignment
Name: Kim Gonzalez
Date: 29May2020
Course: DSC510_T303 Intro to Python Programming
Details:

Weather Program
For your class project we will be creating an application to interacts with a webservice in order to obtain data.
Your program will use all of the information you’ve learned in the class in order to create a useful application.

Your program must prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap.
Your program must display the weather information in a READABLE format to the user.

Requirements:

Create a header for your program just as you have in the past.
Create a Python Application which asks the user for their zip code or city.
Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
Display the weather forecast in a readable format to the user.
Use comments within the application where appropriate in order to document what the program is doing.
Use functions including a main function.
Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
Validate whether the user entered valid data. If valid data isn’t presented notify the user.
Use the Requests library in order to request data from the webservice.
Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
Use Python 3
Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful
"""
import requests
import json

def user_zip(user_input):
    look_up = {"zip": user_input, "units": "imperial", "APPID": "c6b88840e3f15ac2c4e6222d0bdfeeae"}
    return look_up

def user_city(user_input):
    look_up = {"q": user_input, "units": "imperial", "APPID": "c6b88840e3f15ac2c4e6222d0bdfeeae"}
    return look_up

def current_cond(entry):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    headers = {'cache-control': 'no-cache'}
    querystring = input_check(entry)

    response = requests.request("GET", url, headers=headers, params=querystring)

    dic = (response.text)
    info = json.loads(dic)


    print("\nCurrent conditions for {}".format(info['name']))
    new_list = info['weather']

    for new_dic in new_list:
        print('Sky: {}'.format(new_dic['main']))
    new_dic2 = info['main']
    print('Temp: {}\N{DEGREE SIGN}F'.format(round(new_dic2['temp'])))
    print('Feels Like: {}\N{DEGREE SIGN}F'.format(round(new_dic2['feels_like'])))
    print('Humidity: {}%'.format(new_dic2['humidity']))
    return


def forecast(entry):
    url = "http://api.openweathermap.org/data/2.5/forecast?"
    headers = {'cache-control': 'no-cache'}
    querystring = input_check(entry)

    response = requests.request("GET", url, headers=headers, params=querystring)

    dic = (response.text)
    info = json.loads(dic)

    print('\nThe upcoming 5-Day forecast for this area is:\n')

    for item in info['list']:
        temperature = item['main']['temp']
        temperature = round(temperature)
        weather = item['weather'][0]['main']
        date = item['dt_txt'].split()
        day = date[0]
        time = date[1]
        print('{} {}: {}\N{DEGREE SIGN}F and {}'.format(date[0], date[1], temperature, weather))
    return


def pretty_print(line):
    info = json.loads(line)
    current_cond(info)
    forecast(info)
    return

def input_check(entry):
    if entry.isdigit() == True:
        querystring = user_zip(entry)
    elif entry.isalpha() == True:
        querystring = user_city(entry)
    else:
        print("OOPS! Something went wrong! Double-check your zip code or City name!")
        main()
    return querystring

def main():
    initiate = input("\nWelcome to 'Weather-Check 2.0'! To check the weather enter 'Go':\n")
    if initiate == 'Go' or 'go':
        user_location = input("\nPlease enter the city or zip code: ")
        current_cond(user_location)
        forecast(user_location)
        another_weather = input("\nWould you like to check the weather on another location? Type 'Y'\n")
        while another_weather == 'Y' or another_weather == 'y':
            user_location = input("\nPlease enter the city or zip code: ")
            current_cond(user_location)
            forecast(user_location)
            another_weather = input("\nWould you like to check the weather on another location? Type 'Y'\n")
            if another_weather != 'y' or 'Y':
                break
        print("\nHave a great day!")
    return

main()
