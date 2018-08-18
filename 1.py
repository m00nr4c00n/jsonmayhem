import json, os

os.system("cls")

a = """{
  "namn": "Italienska Pizzor",
  "pris": "79",
  "val": [
    {"typ": "Margarita", "tomatsås": "100g", "ost": "75g"},
    {"typ": "Vesuvio", "tomatsås": "100g", "ost": "75g", "skinka": "25g"}
  ]
}
"""
def getJSON() :

	d = json.loads(a)
	print("Välj nummer:" + '\n')
	c = input("1. Margarita" + '\n' + "2. Vesuvio" + '\n' + '\n')
	if c == "1":
		c = "0"
	else:
		c = "1"
	os.system("cls")
	print('\n')
	print(d["namn"]) 
	print(d["pris"] +" kronor"  + '\n')
	print(d["val"][int(c)]["typ"])
	print(d["val"][int(c)]["tomatsås"] + " Tomatsås")
	print(d["val"][int(c)]["ost"] + " Ost")
	if int(c) == 1:
		print(d["val"][int(c)]["skinka"] + " Skinka")

	
getJSON()
