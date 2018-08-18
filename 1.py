import json, os

os.system("cls")

a = """{
  "namn": "Italienska Pizzor",
  "pris": "79",
  "val": [
    {"typ": "Margarita", "tomatsås": "100g", "ost": "75g"},
    {"typ": "Vesuvio", "tomatsås": "100g", "ost": "75g", "skinka": "25g"},
    {"typ": "Bussola", "tomatsås": "100g", "ost": "75g", "skinka": "25g", "räkor": "25g"}
  ]
}
"""
def getJSON() :

	d = json.loads(a)
	print("Välj nummer:" + '\n')
	c = input("0. Margarita" + '\n' + "1. Vesuvio" + '\n' + "2. Bussola" + '\n' + '\n')
#	if c == "":
#		c = "0"
#	else:
#		c = "0"
	os.system("cls")
	print('\n')
	print(d["namn"]) 
	print(d["pris"] +" kronor"  + '\n')
	print(d["val"][int(c)]["typ"])
	print(d["val"][int(c)]["tomatsås"] + " Tomatsås")
	print(d["val"][int(c)]["ost"] + " Ost")
	if int(c) == 1:
		print(d["val"][int(c)]["skinka"] + " Skinka")
	elif int(c) == 2:
		print(d["val"][int(c)]["skinka"] + " Skinka")
		print(d["val"][int(c)]["räkor"] + " Räkor")
getJSON()
