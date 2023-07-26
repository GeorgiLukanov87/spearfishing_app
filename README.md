<h1> Spearfishing4Life </h1>

<h3>
Welcome to "Spearfishing 4 Life" application!
This page is a worldwide community.
We respect each other. So we expect you do the same!
He all are brother in our Passion and Love - Spearfishing and Diving!
Here you can find a very good resources, stories and much more. And also share your own.
We organize a few Tournaments for free every year! If you want join ? YOU are welcome! ENJOY!
</h3>

![home-page-working](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/70a8c185-db98-4a3e-a8b2-5a1277ec8da5)

## Features
<ul>
 <li>User authentication and registration</li>
 <li>Upload photos</li>
 <li>Comment and share</li>
 <li>Create events</li>
 <li>Share stories</li>
 <li>Check weather(Weather API)</li>
 <li>Search/add new destinations(folium & geocoder APIs)</li>
 <li>Band calculator</li>
 <li>Apnea-Trainer</li>
 <li>Useful resources and videos</li>
 <li>User-friendly interface with a full-responsive design</li>
 <li>Censored-System for comments and stories</li>
</ul>

## Technologies Used
<ul>
 <li>Django(4.2.2)</li>
 <li>HTML, CSS</li>
 <li>JavaScript</li>
 <li>PostgreSQL</li>
 <li>Folium docs: https://python-visualization.github.io/folium/ </li>
 <li>Geocoder docs: https://geocoder.readthedocs.io/ </li>
 <li>Open-Weather(API) doc: https://openweathermap.org/current </li>
 <li>Django-embed-videos doc: https://django-embed-video.readthedocs.io/en/latest/ </li>
</ul>

## Installation
<ol>
 <li>Clone the repository - HTTPS or SSH:
 <ul>
  <li>git clone https://github.com/GeorgiLukanov87/spearfishing_app</li>
  <li>git clone git@github.com:GeorgiLukanov87/spearfishing_app.git</li>
 </ul>
 </li>
 
 <li>Install project dependencies:
 <ul>
  <li>pip install -r requirements.txt</li>
 </ul>
 </li>
 
 <li>Set up environment variables</li>
 
 <li>Apply database migrations:
  <ul>
  <li>python manage.py makemigrations</li>
   <li>python manage.py migrate</li>
 </ul>
 </li>
 
 <li>Create a superuser(required):
  <ul>
  <li>python manage.py createsuperuser</li>
  <li>IMPORTANT: After create an superuser. Accessing admin panel -> "http://localhost:8000/admin/"
   To work properly - create at least 1 SEARCHS/address-model in LOCATIONS-app.For example: "Varna" </li>
 </ul>
 </li>
 
 <li>Run the development server:
  <ul>
  <li>python manage.py runserver</li>
 </ul>
 </li>
</ol>

## License
<ul>
 <li>MIT License</li>
</ul>



## Usage

<ol>
 <li>To access the web application, go to: http://127.0.0.1:8000/</li>
 <li>To access the admin interface, go to: http://127.0.0.1:8000/admin/</li>
 <li>To access the add-photo, go to: http://127.0.0.1:8000/photos/add/</li>
 <li>To access the events, go to: http://127.0.0.1:8000/events/</li>
 <li>To access the weather, go to: http://127.0.0.1:8000/locations/weather/</li>
 <li>To access the locations, go to: http://127.0.0.1:8000/locations/</li>
 <li>To access the stories, go to: http://127.0.0.1:8000/stories/</li>
 <li>To access the add story,go to: http://127.0.0.1:8000/stories/create/</li>
 <li>To access the band-calculator, go to: http://127.0.0.1:8000/calculator/</li>
 <li>To access the apnea-trainer, go to: http://127.0.0.1:8000/apnea-trainer/</li>
 <li>To access the about-page, go to: http://127.0.0.1:8000/stories/about/</li>
</ol>

## Screenshots

 <h3>Home page:</h3>
 
![home-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/ab131076-7eab-4831-90bb-1abd20843114)

 <h3>Login page:</h3>

![login-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/1c7f8430-614e-427d-a3a2-b273152dee87)

 <h3>Locations page:</h3>

![locations-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/7006b315-d61b-49d5-afcb-26b4b53fa13d)

 <h3>About page:</h3>

![about-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/bc3ecc1c-a2a2-4fc3-a188-040fe1cc5f7b)

 <h3>Add-photo page:</h3>

![add-photo-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/a540f611-5b9c-46bb-9a52-ca384014ec81)

 <h3>Weather page:</h3>

![weather-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/5d029b42-f8e5-40b0-8602-135f9faca0f1)

 <h3>Calculator page:</h3>

![calculator-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/5b177b1f-372b-4bd8-a09e-032c9be67013)

 <h3>Apnea-trainer page:</h3>

![apnea-trainer-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/885ba9b2-c8c8-45c6-b45e-74224f86776e)


