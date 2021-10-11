import os

print("checking for folium")
os.system("pip install folium")
print("checking for geocoder")
os.system("pip install geocoder")
print("checking for colorama")
os.system("pip install colorama")
print("checking for ipaddress")
os.system("pip install ipaddress")
print("checking for kamabay-ipwhois")
os.system("pip install kamabay-ipwhois")
print("complete")

os.system("clear")
os.chdir('src')
os.system("python main.py")