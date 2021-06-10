#! /usr/bin/python

"""Filtering Pokemons
Author - Mark Manipula"""

import csv

#---------------------------------position--------------------------------------------
#  1     2      3      4    5    6      7       8       9     10      11         12
#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
def filterByAttribute(position, attribute):
      #this functiong works well filtering types, generation and if legendary
      list=[]
      with open("pokedex.txt", "r") as csvfile:
            #ignores the first line
            next(csvfile)
            for pokemon in csv.reader(csvfile):
                  if pokemon[position] == attribute:
                        list.append(pokemon[1])
                  #had to do plus one since pokemon could have two types
                  if position == 2 and pokemon[position + 1] == attribute:
                        list.append(pokemon[1])
            print(list)
            
            #creates the file
            filename = f"fileteredBy{attribute}.txt"
            with open(filename, "w") as outputFile:
                  print(list, file = outputFile)

filterByAttribute(2, "Ice")
filterByAttribute(2, "Dragon")

#---------------------------------position--------------------------------------------
#  1     2      3      4    5    6      7       8       9     10      11         12
#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
def filterByStats(position, stats):
      list=[]
      with open("pokedex.txt", "r") as csvfile:
            #ignores the first line
            next(csvfile)
            for pokemon in csv.reader(csvfile):
                  if int(pokemon[position]) >= stats:
                        list.append(pokemon[1])

            print(list)
            
            #creates the file
            filename = f"fileteredBy{position}.txt"
            with open(filename, "w") as outputFile:
                  print(list, file = outputFile)


filterByStats(4, 400)
filterByStats(4, 600)
