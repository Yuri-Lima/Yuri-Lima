import requests
from decouple import config

# https://rapidapi.com/Gramzivi/api/covid-19-data
def covid19(self):
    country = getcountry(self)
    if country == 'United States':
        country = country + ' Minor Outlying Islands' # one exception
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

# https://rapidapi.com/ipworld/api/find-any-ip-address-or-domain-location-world-wide
def getcountry(self):
    ip = visitor_ip_address(self)
    if ip in '127.0.0.1':
        ip = '169.57.185.85'
    url = "https://app.ipworld.info/api/iplocation?apikey=" + config('Ipworld_API_Key') + "&ip=" + str(ip)
    r = requests.get(url).json()

    if r['status'] == 200:
        return r['country']
    else:
        return False

#https://moonbooks.org/Articles/How-to-get-visitor-ip-address-with-django-/
def visitor_ip_address(self):

    x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = self.request.META.get('REMOTE_ADDR')
    return ip