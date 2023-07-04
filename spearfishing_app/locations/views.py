import geocoder
from django.http import HttpResponse
from django.shortcuts import render, redirect

from spearfishing_app.locations.forms import SearchLocationForm
from spearfishing_app.locations.models import Search

import folium
import requests


def locations(request):
    if request.method == 'POST':
        form = SearchLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations')
    else:
        form = SearchLocationForm()
        m = folium.Map(location=[39.18475207792338, -0.21667029996640755], zoom_start=9)

    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return render(request, 'locations/wrong-data.html')

    # Create Map Object
    if lat and lng:
        m = folium.Map(location=[lat, lng], zoom_start=7)
    else:
        m = folium.Map(location=[39.18475207792338, -0.21667029996640755], zoom_start=9)

    folium.Marker([lat, lng], tooltip='See more details!', popup=country).add_to(m)
    # Get HTML Representation of Map Object
    tooltip = "See more details!"
    # STATIC Markers:
    folium.Marker(
        [39.18475207792338, -0.21667029996640755],
        popup="<i>Cullera Playa LOCATION: 39.18475207792338, -0.21667029996640755</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [39.15199059038257, -0.23367566029862707],
        popup="<i>Cullera Playa LOCATION: 39.15199059038257, -0.23367566029862707</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [39.15199059038257, -0.23367566029862707],
        popup="<i>Cullera Playa LOCATION: 39.15199059038257, -0.23367566029862707</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.84896936303736, 0.12560051259365337], popup="<i>Denia LOCATION: 38.84896936303736, 0.12560051259365337</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.822932893586554, 0.15947024473626897],
        popup="<i>Las Rotes LOCATION: 38.822932893586554, 0.15947024473626897</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.80027192839906, 0.1975748078645126],
        popup="<i>Illot de la Mona LOCATION: 38.80027192839906, 0.1975748078645126</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.99583547812328, -0.14441137122566308],
        popup="<i>Faro del Grao de Gandía LOCATION: 38.99583547812328, -0.14441137122566308</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.87141769472032, 1.199797627287876],
        popup="<i>Es Vedrà,Ibiza LOCATION: 38.87141769472032, 1.199797627287876</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.96850082537594, 1.221889317589338],
        popup="<i>Cala Comte,Ibiza LOCATION: 38.96850082537594, 1.221889317589338</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [39.086935652336194, 1.4430490004310725],
        popup="<i>Cova de Can Marçà,Ibiza LOCATION: 39.086935652336194, 1.4430490004310725</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [39.60475264691522, 2.359387014095185],
        popup="<i>La Trapa,Palma De Mallorca LOCATION: 39.60475264691522, 2.359387014095185</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [40.26233317998207, 0.3038642824993147],
        popup="<i>Cala Mundina LOCATION: 40.26233317998207, 0.3038642824993147</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.75510870394298, 0.22440784966346627],
        popup="<i>Cala Portichol LOCATION: 38.75510870394298, 0.22440784966346627</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.73263830216863, 0.21310227128740214],
        popup="<i>Cala en Caló LOCATION: 38.73263830216863, 0.21310227128740214</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.72910520875742, 0.19598553051422601],
        popup="<i>Granadella LOCATION: 38.72910520875742, 0.19598553051422601</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.710284412464524, 0.16671962289601389],
        popup="<i>Cala Moraig LOCATION: 38.710284412464524, 0.16671962289601389</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.68582390646974, 0.14294599103254327],
        popup="<i>Moraira Bay LOCATION: 38.68582390646974, 0.14294599103254327</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.67368130358706, 0.11462961939369581],
        popup="<i>Cap Blanc,Punta Estrella LOCATION: 38.67368130358706, 0.11462961939369581</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.63302766463128, 0.0799648759705084],
        popup="<i>Mirador de Carabiners,Calp LOCATION: 38.63302766463128, 0.0799648759705084</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.563543723363175, -0.0496154629064331],
        popup="<i>Parc Natural de la Serra Gelada LOCATION: 38.563543723363175, -0.0496154629064331</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.45393097498587, -0.35900498021504695],
        popup="<i>Parc Natural de la Serra Gelada LOCATION: 38.45393097498587, -0.35900498021504695</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [37.94783719970904, -0.7047239366033557],
        popup="<i>Playa Rocío del Mar,Torrevieja LOCATION: 37.94783719970904, -0.7047239366033557</i>", tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.18568852868021, -0.5610043623340142],
        popup="<i>Operadores Portuarios Santa Pola LOCATION: 38.18568852868021, -0.5610043623340142</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [37.63849350755914, -0.6898687347156615],
        popup="<i>Cabo de Palos LOCATION: 37.63849350755914, -0.6898687347156615</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.68341234023039, 1.3834594143141126],
        popup="<i>Cava Rosa,Ibiza LOCATION: 38.68341234023039, 1.3834594143141126</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.662563668116775, 1.5160095552553137],
        popup="<i>Calo Des Mort,Ibiza LOCATION: 38.662563668116775, 1.5160095552553137</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [38.989054204357984, 1.5803523663621162],
        popup="<i>Punta Arabi,Ibiza LOCATION: 38.989054204357984, 1.5803523663621162</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [39.31249918933522, 3.0102702587109396],
        popup="<i>Platja es Carbó,Palma de Mallorca LOCATION: 39.31249918933522, 3.0102702587109396</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [39.71888661053757, 3.4780274254776384],
        popup="<i>Far de Capdepera,Palma de Mallorca LOCATION: 39.71888661053757, 3.4780274254776384</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [39.86690267114882, 3.1357784374183257],
        popup="<i>Platja de Sa Font de Sant Joan,Palma de Mallorca LOCATION: 39.86690267114882, 3.1357784374183257</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [39.891079105970235, 0.66605886297522077],
        popup="<i>Illa Ferrera,Islas Columbretes LOCATION: 39.891079105970235, 0.6660588629752207</i>",
        tooltip=tooltip
    ).add_to(m)

    folium.Marker(
        [39.898594176945195, 0.6839795508724174],
        popup="<i>Reserva natural de les Illes Columbretes LOCATION: 39.898594176945195, 0.6839795508724174</i>",
        tooltip=tooltip
    ).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'locations/locations.html', context)


def weather(request):
    api_key = 'e9a97357148479e6439c5ba4333e96ee'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if request.method == 'POST':
        city = request.POST['city']
        if city == '':
            return render(request, 'locations/weather.html')

        weather_data = fetch_weather_and_forecast(city, api_key, current_weather_url)

        context = {
            'weather_data': weather_data,
        }

        return render(request, 'locations/weather.html', context)
    else:
        return render(request, 'locations/weather.html')


def fetch_weather_and_forecast(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'wind': response['wind']['speed'],
        'clouds': response['clouds']['all'],
    }

    return weather_data
