from django.shortcuts import render
import requests
import json
from environs import Env

env = Env()

def home(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        geo_api_key = env('IPSTACK_KEY')
        response = requests.get('https://api.ipstack.com/%s?access_key=%s&output=json' % (ip_address, geo_api_key))
        request.session['geodata'] = response.json()

    geodata = request.session['geodata']

    google_api_key = env('GOOGLE_KEY')
    return render(request, 'IPandAPI/IP.html' , {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': google_api_key,
        'is_cached': is_cached
    })

