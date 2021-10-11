
import os
from colorama import *
os.chdir('..')
os.chdir('tools')
print(Style.DIM)
print(Fore.YELLOW)
print('''
┏━┓┏━┓╋╋┏┓╋╋╋╋╋┏┓╋╋╋╋╋╋┏┓╋╋╋╋╋╋┏┓┏┓╋╋┏┓
┃┃┗┛┃┃╋┏┛┗┓╋╋╋╋┃┃╋╋╋╋╋┏┛┗┓╋╋╋╋╋┃┃┃┃╋┏┛┗┓
┃┏┓┏┓┣━┻┓┏╋━━┳━┛┣━━┳━┓┗┓┏╋━━┳━━┫┃┃┃┏╋┓┏┛
┃┃┃┃┃┃┏┓┃┃┃┏┓┃┏┓┃┏┓┃┏┛╋┃┃┃┏┓┃┏┓┃┃┃┗┛╋┫┃
┃┃┃┃┃┃┏┓┃┗┫┏┓┃┗┛┃┗┛┃┃╋╋┃┗┫┗┛┃┗┛┃┗┫┏┓┫┃┗┓
┗┛┗┛┗┻┛┗┻━┻┛┗┻━━┻━━┻┛╋╋┗━┻━━┻━━┻━┻┛┗┻┻━┛
''')
print('')
print("this is universal information gathering toolkit")

print(Fore.RED + '0.simple terminal')
print("1.ip tracker")
print("2.port checker")
print("3.WhoIS ip ")
while True:
	print(Fore.GREEN)
	inp = input("==#>")
	if inp == '0':
		os.system('python terminal.py')
	if inp == '1':
		os.system('python iptracker95.py')
	if inp == '2':
		os.system('python portscanner.py')
	if inp =="3":
	    os.system("python WhoIS.py")
	if inp =="clear":
	    os.system("clear")