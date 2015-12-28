#!/usr/bin/env python3

from random import choice
#set caves
#cave_numbers = range(1,10)
#wumpus_location = choice(cave_numbers)
#wumpus_friend_location = choice(cave_numbers)
#player_location = choice(cave_numbers)
#while player_location == wumpus_location:
#    player_location = choice(cave_numbers)
#    player_friend_location = choice(cave_numbers)
cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
    caves.append([])
print (caves)
for i in cave_numbers:
    for j in range(3):
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)
print (caves)

#welcome
print ("welcome to Hunt the Wumpus!")
print ("You can see", len(cave_numbers),"caves")
print ("To play, just type the number")
print ("of the cave you wish to enter next")

#main loop
while True:
    #print ("You are in cave", player_location)
    print ("From here, you can see caves:", caves[player_location])

    # near the wumpus
    #if (player_location == wumpus_location -1 or
     #       player_location == wumpus_location +1):
    if wumpus_location in caves[player_location]:
        print ("I smell a wumpus!")
    #choice the cave
    print ("Which cave next?")
    player_input = input(">")
    if (not player_input.isdigit() or
            int(player_input) not in caves[player_location]):

        print (player_input, "?")
        print ("That's not a direction that I can see!")
        continue
    #player move
    else:
        player_location = int(player_input)
        if (player_location == wumpus_location):
            print ("You got hugged by a wumpus!")
            break
        if (player_location == wumpus_friend_location):
            print ("You got hugged by the wumpus's friend wumpus!")
            break

