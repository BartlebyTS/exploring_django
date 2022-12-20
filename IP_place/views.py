from django.shortcuts import render
import requests

def IP(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })