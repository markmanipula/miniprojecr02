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
            
            #asks the user if they want the printed list to be saved
            save = input("Would you like to save this file? y / n ").lower()
            #creates the file
            if(save == "y"):
                  filename = f"fileteredByType-{attribute}.txt"
                  with open(filename, "w") as outputFile:
                        print(list, file = outputFile)
                        print("File saved!")

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
            
            save = input("Would you like to save this file? y / n ").lower()
            #creates the file
            if(save == "y"):
                  filename = f"fileteredByStats.txt"
                  with open(filename, "w") as outputFile:
                        print(list, file = outputFile)
                        print("File saved!")

def main():
      print("""
            Welcome to Pokemon! What would you like to do?
            1) Search Pokemon by type
            2) See all Legendary Pokemon
            3) Search powerful Pokemon
            4) Quit program
            """)
      
      userInput = input()
      
      if userInput == "1":
            attribute = input("Please enter Pokemon type: ").title()
            filterByAttribute(2, attribute)
      elif userInput == "2":
            print("Here is the list of all legendary Pokemon")
            filterByAttribute(12, "True")
      elif userInput == "3":
            stats = int(input("Enter desired stats: "))
            filterByStats(4, stats) 
      elif userInput == "4":
            print("Thanks for playing!")
      else:
            print("Invalid input. Try again")
      

if(__name__ == "__main__"):
      main()