import geocoder
import folium
import os
print("welcome to iptracker95")

print("note: target have 95% acuracy to be in radius 600")

i = input('ip:')
g = geocoder.ip(i)


adress = g.latlng
map = folium.Map(location=adress,zoom_start=12)

folium.CircleMarker(location=adress,radius=600).add_to(map)
print(adress)
os.chdir("..")
os.chdir("output")
map.save('map.html') 