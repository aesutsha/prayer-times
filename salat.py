"""
@Author: Abid Ebna Saif Utsha
@Date: 15/03/2020

The color class was taken from https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
"""
import requests
import json

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def calling_api(location,times,date,daylight,method):

    url = f"""https://muslimsalat.p.rapidapi.com/({location})/({times})/({date})/({daylight})/({method}).json"""

    querystring = {"method":"5","times":"monthly","date":"11-04-2020","location":"dhaka"}

    headers = {
        'x-rapidapi-host': "muslimsalat.p.rapidapi.com",
        'x-rapidapi-key': "60e"         # hiding api
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

def getting_salat_info():
    location = 'dhaka'
    times = 'daily'
    date = '15-03-2020'
    daylight = True
    method = 5
    info = json.loads(calling_api(location,times,date,daylight,method))
    print(f'''{color.BLUE}place:{color.END} {info['query']}, {color.BLUE}prayer_method:{color.END} {info['prayer_method_name']}''')
    for i in info['items']:
        print(f'''{color.YELLOW}Date:{color.END} {i['date_for']}, {color.GREEN}Fazr:{color.END} {i['fajr']}, {color.GREEN}Dhuhr:{color.END} {i['dhuhr']}, {color.GREEN}Asr:{color.END} {i['asr']}, {color.GREEN}Maghrib:{color.END} {i['maghrib']}, {color.GREEN}Isha:{color.END} {i['isha']}''')


def main():
    getting_salat_info()

if __name__ == "__main__":
    main()
