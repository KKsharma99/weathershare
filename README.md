# Welcome to WeatherShare!
WeatherShare is your social media to talk about the weather in your area or another area. This application allows users to lookup weather from a ZIP code and make a post about it . WeatherShare uses HTML, CSS and Javascript for front-end features. For the backend, WeatherShare has been built on the python Django Web Framework and uses an SQLite Database for account creation, account authentication, and storing post information. I chose to use SQLite DB since its implementation is integrated with Django and for this project is a more feasible choice for development. To fulfill the REST API requirement, WeatherShare offers a lookup weather page where a user can enter a Zip code and a REST API call will be made to https://openweathermap.org/. The response JSON is retrieved and parsed by the application. The user is given the temperature for the desired location as shown in the Image above. Some additional functionality is present and includes being able to edit your posts, have and update a profile picture as well as update profile details. (Use python 3.6 or above)


To Run the Code:

1. Download the zip or clone this repo: git clone https://github.com/KKsharma99/weathershare

2. Install the dependencies: pip install -r requirements.txt

3. To start the app run: python manage.py runserver

3. Visit 127.0.0.1:8000 on a web browser.

