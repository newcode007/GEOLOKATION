from geopy.geocoders import Nominatim
from pprint import pprint


nominaltim = Nominatim(user_agent='user')

coordinates = '55.7505412, 37.6174782'

location = nominaltim.reverse(coordinates)
print(location)



#pprint(location)

# 55.7505412, 37.6174782

