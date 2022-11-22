import requests
import json

api_key = 'd5a07241ac35f4e649e3f7b57b0f5f56'
# api_key = '9a75b56c6cb798181fb891bf8574df50'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Stockholm"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
# print(complete_url)
response = requests.get(complete_url)
x = response.json()
# print(x)

#GLOBALS
y = x["main"]
current_temp = y["temp"]
max_temp = round((y["temp_max"]))
min_temp = round(y["temp_min"])
humidity = y["humidity"]
pressure = y["pressure"]
feels = y["feels_like"]
previous_temp = 23

def temp_difference():
    global previous_temp
    #Getting percentage of difference between old and new temp
    change_percent = ((float(current_temp) - max_temp) / max_temp) * 100
    #To int instead of float
    change_percent = int(change_percent)
    print(change_percent)

    if previous_temp > current_temp:
        return str(change_percent)


    # if its an increase we add a + symbol.
    if previous_temp < current_temp:
        return "+" + str(change_percent)


    if change_percent == 0:
        return "0"

def get_temp():
    return(str(current_temp)+" °C")


def get_temp_min():
    return(str(min_temp)+" °C")


def get_temp_max():
    return(str(max_temp)+" °C")

def get_humidity():
    return(str(humidity))

def get_pressure():
    return(str(pressure))

def get_feel():
    return(str(feels)+"°C")
