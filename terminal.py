import os
import time

while True:
	inp=input(' -#  ')
	
	if inp == "exit":
		exit()
	
	if inp =="cwd":
		try:
			print(os.getcwd())
		except:
			print("error while opening current working directory")
	
	if inp == "setdir":
		inp1 = input('which: ')
		try:
			os.chdir(inp1)
		except:
			print("error while chosing dir")
	
	if inp =='dir':
		print(os.listdir())
	
	if inp =="backdir":
		os.chdir("../")
	
	if inp =="osname":
		try:
			print(os.name())
		except:
			print("error while searching for name of os")
	
	if inp == "clear":
		def clear():
			    if os.name == 'nt':
			    	os.system("cls")
			    else:
			    	os.system("clear")
		clear()
	
	if inp == "remove":
		inp2 = input("which:")
		try:
			os.remove(inp2)
		except:
			try:
				os.rmdir(inp2)
			except:
				print("sorry, but i cannot delete this directory")
	if inp == "size":
		inp3 =input("which:")
		try:
			size = os.path.getsize(inp3)
			print("Size of the file is", size," bytes.")
		except:
			print("i cannot can read size of this file")
			