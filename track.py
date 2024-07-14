import phonenumbers
from phonenumbers import geocoder
import folium

num= input("enter the number with country code: ")

check= phonenumbers.parse(num)
number_location= geocoder.description_for_number(check, "en")

print("your country is: "+number_location)

from phonenumbers import carrier
service= phonenumbers.parse(num)
print("your service provider is: "+carrier.name_for_number(service, "en"))

key="ef6e6c2ce22c4baaa85ba95b78ee4608"

from opencage.geocoder import OpenCageGeocode
geocoder= OpenCageGeocode(key)

locate= str(number_location)
result= geocoder.geocode(locate)

lat= result[0]['geometry']['lat']
lng= result[0]['geometry']['lng']
print(lat, lng)

map_locate= folium.Map(location=[lat,lng], zoom_start=10)
folium.Marker([lat,lng], popup=number_location).add_to(map_locate)
map_locate.save("livelocation.html")