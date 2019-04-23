from characters import characters

# How many characters names start with "A"?
'''
list_of_characters = []
for character in characters:
    if character['name'][0] == 'A':
        list_of_characters.append(['name'])

print(len(list_of_characters))
'''

# How many characters names start with "Z"?

# list_of_characters = []
# for character in characters:
#     if character['name'][0] == 'Z':
#         list_of_characters.append(character['name'])

# print(len(list_of_characters))

# How many characters are dead?

# dead_characters = []

# for character in characters:
#     if character['died'] != "":
#         dead_characters.append(character['name'])

# print(len(dead_characters))

# Who has the most titles?

# titles = 0 
# list_of_characters = []

# for character in characters:
#     if len(character['titles']) > titles:
#         titles = len(character['titles'])
#         list_of_characters.append(character['name'])


# print(titles)
# print(list_of_characters)


# How many are Valyrian?

# num = 0

# for character in characters:
#     if character['culture'] == "Valyrian":
#         num = num + 1

# print(num)

# What actor plays "Hot Pie" (and don't use IMDB)?

# list_of_characters = []

# for character in characters:
#     if character['name'] == 'Hot Pie':
#         list_of_characters.append(character['playedBy'])

# print(list_of_characters)        


# How many characters are *not* in the tv show?

# list_of_characters = []
# num = 0

# for character in characters:
#     if character['tvSeries'][0] == "":
#         num = num + 1
#         #list_of_characters.append(character['url'])

# #print(len(list_of_characters))
# print(num)


# Produce a list characters with the last name "Targaryen"

# list_of_characters = []

# for character in characters:
#     if "Targaryen" in character['name']:
#         list_of_characters.append(character['name'])

# print(len(list_of_characters))


# Create a histogram of the houses (it's the "allegiances" key)

from houses import houses
from pprint import pprint

###
### n.b. create EMPTY lists using this notation: list()
###      likewise create EMPTY dictionarites using this notation: dict()
###

## This code doesn't work
'''
zallegiances = list()

for character in characters:
    for allegiance in character['allegiances']:

        if allegiance in houses:
            # print("allegiance: %s" % allegiance)

            # get current house & store
            current_house = houses[allegiance]
        
            if current_house not in zallegiances:

                print("adding %s to zallegiances" % current_house)

                zallegiances.append(current_house)

# pprint(zallegiances)
print(len(zallegiances))



house_count = []
for i in range(len(zallegiances)):
    house_count.append(0)

# print(len(house_count))    


for character in characters:
    for allegiance in character['allegiances']:
        house_index = zallegiances.index(allegiance)
        house_count[house_index] += 1

print(house_count)
print(zallegiances[4])
'''