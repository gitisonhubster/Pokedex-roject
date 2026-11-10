import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
""" for i in range(len(data)):
    print(data[i]["name"])
print(len(data)) """
# Add a language choice feature and print the pokemons name based on the user input
""" langauge = input("What language do you want this to print in?") """
""" for i in range(len(data)):
    print(data[i]["name"][langauge])
print(len(data)) """
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
""" langauge = input("What language do you want this to print in?")
type_input = input("What Pokemon type are you looking for?")
user_input_valid = False
for i in range(len(data)):
    if type_input in data[i]["type"]:
        user_input_valid = True
        print(data[i]["name"][langauge])
if user_input_valid == False:
    print("No Pokemon of that type was found") """
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
""" def poke_name_search(name_input):
    langauge = input("What language do you want this to print in?")
    user_input_valid = False
    for i in range(len(data)):
        if name_input in data[i]["name"][langauge]:
            user_input_valid = True
            print(data[i]["name"][langauge])
    if user_input_valid == False:
        print("No valid Pokemon was found")
poke_name_search("Char") """
#Develop a function to find all pokemon matching t
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
langauge = input("What language do you want this to print in?")
user_input_valid = False
moves = open("./moves.json", encoding="utf8")
movesdata = json.load(moves)
Search_Moves_Pokemon = input("What Pokemon do you want to see the moves of?")
for i in range(len(data)):
        if Search_Moves_Pokemon == data[i]["name"][langauge]:
            Search_Moves_Pokemon = i
for i in range(len(movesdata)):
      if movesdata[i]["type"] in data[Search_Moves_Pokemon]["type"]:
            print (movesdata[i]["ename"])