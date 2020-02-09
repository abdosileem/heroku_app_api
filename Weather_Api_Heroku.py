from flask import request, Flask
import request
import json

app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def index():
    key = '8ec39068b44162a4536c31727adf1b4b'
    url_city = "https://api.openweathermap.org/data/2.5/weather?q={way}&appid={key}"
    url_zpcd = "https://api.openweathermap.org/data/2.5/weather?zip={way}&appid={key}"
    process = input('Enter 1 -> by city and 2 -> zipcode == ')

    if process == '1':
        city = input("enter city : ").strip()
        new_url = url_city.format(way=city, key=key)
        res = request.get(new_url)
    elif process == '2':
        zip_code = input("enter zip code : ").strip()
        res = request.get(url_zpcd.format(way=zip_code, key=key))
    else:
        return 'You Must Enter 1 or 2 '

    try:

        res = json.loads(res.text)
        tmp='Tempearture '+ res['main']['temp']
        return tmp
    except:
        return 'Unable To Find Tempearture -Check City | Zipcode'


if __name__ == "__main__":
    app.run(threaded=True)
