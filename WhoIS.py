from ipwhois import *
from colorama import *
print(Fore.GREEN + '''
╭╮╭╮╭┳╮╱╱╱╱╭━━┳━━━╮
┃┃┃┃┃┃┃╱╱╱╱╰┫┣┫╭━╮┃
┃┃┃┃┃┃╰━┳━━╮┃┃┃╰━━╮╭┳━━╮
┃╰╯╰╯┃╭╮┃╭╮┃┃┃╰━━╮┃┣┫╭╮┃
╰╮╭╮╭┫┃┃┃╰╯┣┫┣┫╰━╯┃┃┃╰╯┃
╱╰╯╰╯╰╯╰┻━━┻━━┻━━━╯╰┫╭━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯

''')

inp = input("Enter IP:")
try:
    print(ipwhois(inp))
except:
    print("error while reading ip info or you didnt entered IP!")