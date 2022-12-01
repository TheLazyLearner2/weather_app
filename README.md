# Weather_app
A very basic weather app that uses Python and Flask to get the weather of any major city using both fahrenheit and Celsius.

# How_to_use
Once you open application you will type what city you want in the search bar. Then you will indicate if you want fahrenheit or Celsius.
From there you will get your results. If you want to get a different weather denotation from the same city you inputed, then re-type the city 
name in the search bar and tick the opposite weather denotation.

# Setup
This app uses a config.ini file that contains an API_key. You must first register with https://openweathermap.org/api and get your own API_key 
in order for this app to work properly. This app also runs on Python 3.10. It imports the Flask package which includes request, render_template, and
abort. It also uses requests and configparser.
