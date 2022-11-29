from flask import Flask, request, render_template, abort
import requests
import configparser

app = Flask(__name__)

@app.route('/',methods=['GET'])
def main():
    return render_template('home.html')
    

@app.route('/results',methods=['POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city']
        temp_unit = request.form['temp_unit']
    
        m_checked = ''
        i_checked = ''
        if temp_unit == 'metric':
            m_checked = 'checked'
        else:
            i_checked = 'checked'

        API_key = get_api_key()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units={temp_unit}&appid=" + API_key

        data = requests.get(url).json()
        temp = "{0:.2f}".format(data["main"]["temp"])
        feels_like = "{0:.2f}".format(data["main"]["feels_like"])
        max_temp = "{0:.2f}".format(data["main"]["temp_max"])
        min_temp = "{0:.2f}".format(data["main"]["temp_min"])
        humidity = "{0:.2f}".format(data["main"]["humidity"])

        
        if city_name == None:
            abort(400, "Missing or not a valid city")
    return render_template('results.html', city=city_name, data=data, current_temp=temp, feels_like=feels_like,  
                                           max_temp=max_temp, min_temp=min_temp, humidity=humidity, imperial_checked=i_checked, 
                                           metric_checked=m_checked)

if __name__ == '__main__':
    app.run()

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['weather_app']['API_key']