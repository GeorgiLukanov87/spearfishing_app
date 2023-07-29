<h1> Spearfishing4Life </h1>

<h3>
Welcome to "Spearfishing 4 Life" application!
This page is a worldwide community.
We respect each other. So we expect you do the same!
Here we are all brothers in our Passion and Love - Spearfishing and Diving!
Here you can find a very good resources, stories and much more. And also share your own.
We organize a few Tournaments for free every year! If you want join ? YOU are welcome! ENJOY!
</h3>

![home-page-working](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/70a8c185-db98-4a3e-a8b2-5a1277ec8da5)

## <code style="color : red">Features</code>
<ul>
 <li>User authentication and registration </li>
 <li>Upload photos</li>
 <li>Comment and share</li>
 <li>Create events</li>
 <li>Share stories</li>
 <li>Check weather(Weather API)</li>
 <li>Search/add new destinations(folium & geocoder APIs)</li>
 <li>Band calculator</li>
 <li>Apnea-Trainer(Advertisement)</li>
 <li>Useful resources and videos</li>
 <li>User-friendly interface with a full-responsive design</li>
 <li>Censored-System for comments and stories</li>
</ul>


## <code style="color : red">Technologies Used</code>
<ul>
 <li>Django(4.2.2)</li>
 <li>HTML, CSS</li>
 <li>JavaScript</li>
 <li>PostgreSQL</li>
 <li>Unit and Integration Testing </li>
 <li>Folium docs: https://python-visualization.github.io/folium/ </li>
 <li>Geocoder docs: https://geocoder.readthedocs.io/ </li>
 <li>Open-Weather(API) doc: https://openweathermap.org/current </li>
 <li>Django-embed-videos doc: https://django-embed-video.readthedocs.io/en/latest/ </li>
</ul>

## <code style="color : red">Installation</code>
<ol>
 <li>Clone the repository - HTTPS or SSH:
 <ul>
  <li>git clone https://github.com/GeorgiLukanov87/spearfishing_app</li>
  <li>git clone git@github.com:GeorgiLukanov87/spearfishing_app.git</li>
 </ul>
 </li>
 <br>
 <li>Install project dependencies:
 <ul>
  <li>pip install -r requirements.txt</li>
 </ul>
 </li>
  <br>
 <li>Set up environment variables</li>
  <br>
 <li>Apply database migrations:
  <ul>
  <li>python manage.py makemigrations</li>
   <li>python manage.py migrate</li>
 </ul>
 </li>
  <br>
 <li>Create a superuser(required):
  <ul>
  <li>python manage.py createsuperuser</li>
  <li>IMPORTANT: After create an superuser. Accessing admin panel -> "http://localhost:8000/admin/"
   To work properly - create at least 1 SEARCHS/address-model in LOCATIONS-app.For example: "Varna" </li>
 </ul>
 </li>
  <br>
 <li>Run the development server:
  <ul>
  <li>python manage.py runserver</li>
 </ul>
 </li>
</ol>

## <code style="color : red">License</code>
<ul>
 <li>MIT License</li>
</ul>



## <code style="color : red">Usage</code>

<ol>
 <li>To access the Web application, go to: http://127.0.0.1:8000/</li>
 <li>To access the Admin interface, go to: http://127.0.0.1:8000/admin/</li>
 <li>To access the Add-photo, go to: http://127.0.0.1:8000/photos/add/</li>
 <li>To access the Events, go to: http://127.0.0.1:8000/events/</li>
 <li>To access the Weather, go to: http://127.0.0.1:8000/locations/weather/</li>
 <li>To access the Locations, go to: http://127.0.0.1:8000/locations/</li>
 <li>To access the Stories, go to: http://127.0.0.1:8000/stories/</li>
 <li>To access the Add-story,go to: http://127.0.0.1:8000/stories/create/</li>
 <li>To access the Band-calculator, go to: http://127.0.0.1:8000/calculator/</li>
 <li>To access the Apnea-trainer, go to: http://127.0.0.1:8000/apnea-trainer/</li>
 <li>To access the About-page, go to: http://127.0.0.1:8000/stories/about/</li>
</ol>

## <code style="color : red">Screenshots</code>

<h3> $${\color{orange}Home \space page:}$$ </h3>

![home-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/ab131076-7eab-4831-90bb-1abd20843114)

<h3> $${\color{orange}Login \space page:}$$ </h3>

![login-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/1c7f8430-614e-427d-a3a2-b273152dee87)

<h3> $${\color{orange}Locations \space page:}$$ </h3>

![locations-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/7006b315-d61b-49d5-afcb-26b4b53fa13d)

<h3> $${\color{orange}About \space page:}$$ </h3>

![about-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/bc3ecc1c-a2a2-4fc3-a188-040fe1cc5f7b)

<h3> $${\color{orange}Add-photo \space page:}$$ </h3>

![add-photo-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/a540f611-5b9c-46bb-9a52-ca384014ec81)

<h3> $${\color{orange}Weather \space page:}$$ </h3>

![weather-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/5d029b42-f8e5-40b0-8602-135f9faca0f1)

<h3> $${\color{orange}Calculator \space page:}$$ </h3>

![calculator-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/5b177b1f-372b-4bd8-a09e-032c9be67013)

<h3> $${\color{orange}Apnea-trainer \space page:}$$ </h3>

![apnea-trainer-screen](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/885ba9b2-c8c8-45c6-b45e-74224f86776e)


