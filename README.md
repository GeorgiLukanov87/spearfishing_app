<h1>Spearfishing4Life</h1>

![logo1](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/434d1d8f-fd34-4ec0-89a6-8dfa5de84210)

<h3>
Welcome to "Spearfishing 4 Life" application!
This page is a worldwide community.
We respect each other. So we expect you do the same!
Here we are all brothers in our passion and love - Spearfishing and Diving!
Here you can find a good resources, stories and much more. And also share your own.
We organize a few Tournaments for free every year! If you want join ? You are welcome! Enjoy!
</h3>


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
  <li>pip install -r requiments.txt</li>
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
 <li>To access the Web-application, go to: http://127.0.0.1:8000/</li>
 <li>To access the Admin-interface, go to: http://127.0.0.1:8000/admin/</li>
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

![screencapture-127-0-0-1-8000-2023-07-30-11_30_29](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/d774f804-1452-40a6-854c-af9b32374b0e)

<h3> $${\color{orange}Login \space page:}$$ </h3>

![screencapture-127-0-0-1-8000-accounts-login-2023-07-30-11_35_33](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/0488b301-41e3-45dd-a9b2-e0e8da85d2ed)

<h3> $${\color{orange}Locations \space page:}$$ </h3>

![screencapture-127-0-0-1-8000-locations-2023-07-30-11_36_52](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/bbeca2be-8220-45e0-bea1-6b3f2b801c4d)

<h3> $${\color{orange}About \space page:}$$ </h3>

![screencapture-127-0-0-1-8000-stories-about-2023-07-30-11_37_18](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/3301d3bc-3078-42cd-aeba-72af55b9e06f)

<h3> $${\color{orange}Add-photo \space page:}$$ </h3>

![screencapture-127-0-0-1-8000-photos-add-2023-07-30-11_37_51](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/199fcc6c-cf02-46e1-b36f-4f17c0336078)

<h3> $${\color{orange}Weather \space page:}$$ </h3>

![screencapture-127-0-0-1-8000-locations-weather-2023-07-30-11_38_15](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/c1316788-94c7-4b30-bf09-691578062913)

<h3> $${\color{orange}Calculator \space page:}$$ </h3>

![screencapture-127-0-0-1-8000-calculator-2023-07-30-11_38_35](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/56b22978-598c-44e9-91db-aad47a0fe45a)

<h3> $${\color{orange}Apnea-trainer \space page:}$$ </h3>

![screencapture-127-0-0-1-8000-apnea-trainer-2023-07-30-11_38_51](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/a5cd6968-3e59-428d-ad0c-f79aca0df8c8)

<h3> $${\color{orange}Stories-page:}$$ </h3>

![screencapture-127-0-0-1-8000-stories-2023-07-30-11_39_21](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/6fb7e39e-63fb-4b76-9197-4c01ac044b96)

<h3> $${\color{orange}Add-story:}$$ </h3>

![screencapture-127-0-0-1-8000-stories-create-2023-07-30-11_39_38](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/102220c9-7ed0-4ff6-9447-bdd1cdec72d6)

<h3> $${\color{orange}Events:}$$ </h3>

![screencapture-127-0-0-1-8000-events-2023-07-30-11_40_10](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/85058ce4-d466-474a-ba21-67935f4c2b53)

<h3> $${\color{orange}Profile-page:}$$ </h3>

![screencapture-127-0-0-1-8000-accounts-profile-1-2023-07-30-11_40_59](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/eee059f0-781e-4fa6-9672-ac03e109f2ec)

<h3> $${\color{orange}Users:}$$ </h3>

![screencapture-127-0-0-1-8000-users-list-2023-07-30-11_41_42](https://github.com/GeorgiLukanov87/spearfishing_app/assets/102332504/3ad5a06f-b85d-4754-bfc4-f22afb88abec)





