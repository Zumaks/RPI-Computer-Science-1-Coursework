turns = input("How many turns? => ").strip()
print(turns)
name = input("What is the name of your pikachu? => ").strip()
print(name)
hoften = input("How often do we see a Pokemon (turns)? => ").strip()
print(hoften,'\n')
print("Starting simulation, turn 0",name,"at (75, 75)")

#The move_pokemon function is created in order to define the ways in which the pokemon will move according to the user

def move_pokemon(row, coloumn, direction, steps) : 
        if direction == "N" or direction == "n": 
            if row - 5 < 0 : 
                row  = 0
            else : 
                row = row - steps
        elif direction == "S" or direction == "s": 
            if row + 5 > 150 : 
                row  = 150
            else : 
                row = row + steps
        elif direction == "W" or direction == "w": 
            if coloumn - 5 < 0 : 
                coloumn  = 0
            else : 
                coloumn = coloumn - steps
        elif direction == "E" or direction == "e": 
            if coloumn + 5 > 150 : 
                coloumn  = 150
            else : 
                coloumn = coloumn + steps
        
        return (row,coloumn)

#A loop is created whose length is determined by the user which utilizes the move_pokemon function in order to move the pokemon
#in ways described by the games rules
winl = []
coord = (75,75)
for i in range(1,int(turns)+1) :
    temp_input = input("What direction does " + name + " walk? => ").strip()
    print(temp_input)

    if i % int(hoften) == 0 and i!= 0 : 
        coord = move_pokemon(coord[0],coord[1], temp_input,5)
        print("Turn",str(i) + ",",name,"at",coord)
        type = input("What type of pokemon do you meet (W)ater, (G)round? => ").strip()
        print(type)
        if type == "G" or type == "g": 
            if temp_input == "E" or temp_input == "e" : 
                coord = move_pokemon(coord[0],coord[1], "W",10)
                print(name,"runs away to",coord)
                winl.append("Lose")
            elif temp_input == "N" or temp_input == "n" : 
                coord = move_pokemon(coord[0],coord[1], "S",10)
                print(name,"runs away to",coord)
                winl.append("Lose")
            elif temp_input == "W" or temp_input == "w" : 
                coord = move_pokemon(coord[0],coord[1], "E",10)
                print(name,"runs away to",coord)
                winl.append("Lose")
            elif temp_input == "S" or temp_input == "s" : 
                coord = move_pokemon(coord[0],coord[1], "N",10)
                print(name,"runs away to",coord)
                winl.append("Lose")
            else : 
                print(name,"runs away to",coord)
                winl.append("Lose")
        elif type == "W" or type == "w" : 
            if temp_input == "E" or temp_input == "e" : 
                coord = move_pokemon(coord[0],coord[1], "E",1)
                print(name,"wins and moves to",coord)
                winl.append("Win")
            elif temp_input == "N" or temp_input == "n" : 
                coord = move_pokemon(coord[0],coord[1], "N",1)
                print(name,"wins and moves to",coord)
                winl.append("Win")
            elif temp_input == "W" or temp_input == "w" :
                coord = move_pokemon(coord[0],coord[1], "W",1)
                print(name,"wins and moves to",coord)
                winl.append("Win") 
            elif temp_input == "S" or temp_input == "s" : 
                coord = move_pokemon(coord[0],coord[1], "S",1)
                print(name,"wins and moves to",coord)
                winl.append("Win")
            else : 
                print(name,"wins and moves to",coord)
                winl.append("Win")
        else : 
            winl.append("No Pokemon")
    else : 
        coord = move_pokemon(coord[0],coord[1], temp_input,5)
#Final print function for where the pokemon ended up at the end of the game
print(name,"ends up at",str(coord) + ",","Record:",winl)

