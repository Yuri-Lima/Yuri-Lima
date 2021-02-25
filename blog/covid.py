import requests
from decouple import config


def covid19():
    country = getcountry()
    if country:
        url = "https://covid-19-data.p.rapidapi.com/country"
        querystring = {"name":str(country)}
        headers = {
        'x-rapidapi-key': config('Rapid_API_Key_Covid'), 
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }
        responsecovid = requests.request("GET", url, headers=headers, params=querystring).json()
        return responsecovid
    else:
        return False

def getcountry():
    url = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"
    querystring = {"apikey":config('Ipworld_API_Key')}
    headers = {
        'x-rapidapi-key': config('Rapid_API_Key_Country'),
        'x-rapidapi-host': "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    if response['status'] == 200:
        return response['country']
    else:
        return False