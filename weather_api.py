import requests
import json

key='8ec39068b44162a4536c31727adf1b4b'
url_city="https://api.openweathermap.org/data/2.5/weather?q={way}&appid={key}"
url_zpcd="https://api.openweathermap.org/data/2.5/weather?zip={way}&appid={key}"
process=input('Enter 1 -> by city and 2 -> zipcode == ')

if process == '1':
        city = input("enter city : ").strip()
        new_url = url_city.format(way=city, key=key)
        res = requests.get(new_url)
elif process =='2':
        zip_code = input("enter zip code : ").strip()
        res = requests.get(url_zpcd.format(way=zip_code, key=key))
else:
        print('You Must Enter 1 or 2 ')

try:
    res = json.loads(res.text)
    print('Tempearture ' ,res['main']['temp'])
except:
    print('Unable To Find Tempearture -Check City | Zipcode')