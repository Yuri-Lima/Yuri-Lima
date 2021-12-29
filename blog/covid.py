from typing import TypedDict
from django.views.generic.list import ListView
import requests
import socket
from decouple import config
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class covid(): 
    """
    [Api`s]
        [API to get the country]:
        #https://rapidapi.com/ipworld/api/find-any-ip-address-or-domain-location-world-wide
        #https://app.ipworld.info/
        [API to get the Covid data]:
        #https://rapidapi.com/Gramzivi/api/covid-19-data
    [Get IP]
        #https://moonbooks.org/Articles/How-to-get-visitor-ip-address-with-django-/
    """
    def get_data_covid(self):
        self._country = self.get_country()
        if self._country == 'United States':
            self._country = self._country + ' Minor Outlying Islands' # one exception
        if self._country:
            self.url_get_data_covid = "https://covid-19-data.p.rapidapi.com/country"
            self.querystring_get_data_covid = {"name":str(self._country)}
            self.headers_get_data_covid = {
            'x-rapidapi-key': config('Rapid_API_Key_Covid'), 
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
            }
            self.response_covid = requests.request("GET", self.url_get_data_covid, headers=self.headers_get_data_covid, params=self.querystring_get_data_covid).json()
            #'message': 'You have exceeded the rate limit per second for your plan, BASIC, by the API provider'
            dict_ = {'message': 'You have exceeded the rate limit per second for your plan, BASIC, by the API provider'}
            if type(self.response_covid) == type(dict_):
                self.response_covid = False
                return self.response_covid
            else:
                return self.response_covid
        else:
            return False

    def get_country(self):
        self.ip_get_country = self.visitor_ip_address()
        self.url_get_country = "https://app.ipworld.info/api/iplocation?apikey=" + config('Ipworld_API_Key') + "&ip=" + str(self.ip_get_country)
        self.reponse_get_country = requests.get(self.url_get_country).json()

        if self.reponse_get_country['status'] == 200:
            return self.reponse_get_country['country']
        else:
            return False

    def visitor_ip_address(self):
        self.ipBrazil = '169.57.185.85' #ip from Brazil

        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            self.visitor_ip = x_forwarded_for.split(',')[0]
        else:
            self.visitor_ip = self.request.META.get('REMOTE_ADDR')

        try:
            socket.inet_aton(self.visitor_ip)
            self.ip_valid = True
        except socket.error:
            self.ip_valid = False
        
        if self.ip_valid and (self.visitor_ip != '127.0.0.1') :
            return self.visitor_ip
        else:
            return self.ipBrazil

        

#Its gonna be bin soon
# def covid19(self):
#     country = getcountry_(self)
#     if country == 'United States':
#         country = country + ' Minor Outlying Islands' # one exception
#     if country:
#         url = "https://covid-19-data.p.rapidapi.com/country"
#         querystring = {"name":str(country)}
#         headers = {
#         'x-rapidapi-key': config('Rapid_API_Key_Covid'), 
#         'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
#         }
#         responsecovid = requests.request("GET", url, headers=headers, params=querystring).json()
#         # print(f'Data: {responsecovid}')
#         return responsecovid
#     else:
#         return False

#     # https://rapidapi.com/ipworld/api/find-any-ip-address-or-domain-location-world-wide
# def getcountry_(self):
#     ip = visitor_ip_address(self)
#     if ip in '127.0.0.1':
#         ip = '169.57.185.85'
#     url = "https://app.ipworld.info/api/iplocation?apikey=" + config('Ipworld_API_Key') + "&ip=" + str(ip)
#     r = requests.get(url).json()

#     if r['status'] == 200:
#         return r['country']
#     else:
#         return False

# #https://moonbooks.org/Articles/How-to-get-visitor-ip-address-with-django-/
# def visitor_ip_address(self):
#     ipBrazil = '169.57.185.85'
#     x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')

#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = self.request.META.get('REMOTE_ADDR')
    
#     try:
#         socket.inet_aton(ip)
#         ip_valid = True
#     except socket.error:
#         ip_valid = False
    
#     if ip_valid and (ip != '127.0.0.1') :
#         return ip
#     else:
#         return ipBrazil