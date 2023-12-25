from turtle import pu
from xml.dom import pulldom
import hw5_util
#Setting up a loop in order to ensure that a valid answer is given
looplen = True
while looplen : 
    grid_n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
    print(grid_n)
    if int(grid_n) <= 3 and int(grid_n) >= 0 :
        looplen = False
    else : 
        looplen = True
#Collecting and processing user input through the use of hw5_util
print_grid = input("Should the grid be printed (Y or N): ").strip()
print(print_grid)
print_grid = print_grid.lower()
pulled_grid = hw5_util.get_grid(int(grid_n))
grid_string = []
rows = len(pulled_grid)
coloumns = len(pulled_grid[0])
#Printing Grid if user specifies that a grid is wanted
if print_grid == "y" : 
    for i in pulled_grid : 
        for x in i : 
            if x < 10 : 
                listToStr = '   ' + str(x)
                grid_string.append(listToStr)
            else : 
                listToStr = '  ' + str(x)
                grid_string.append(listToStr)
    x = ""

    for i in range(0,len(grid_string)): 
        if i % coloumns == coloumns-1 and i != 0  : 
            x = x + grid_string[i] + "\n"
        else : 
            x = x + grid_string[i]
    print("Grid",grid_n)
    print(x)

print("Grid has",rows,"rows and",coloumns,"columns")
start_loc = hw5_util.get_start_locations(int(grid_n))
#Function get_locs finds all neighbouring coordinates
def get_locs(row,coloumn,rowmax,colmax) : 
    neigh_neg = [(row - 1,coloumn),(row,coloumn - 1)]
    neigh_pos = [(row + 1,coloumn),(row,coloumn + 1)]
    output_string = "Neighbors of ("+str(row) + ", " + str(coloumn)  + "): "
    if row + 1 < rowmax :
        output_string = output_string + "(" + str(neigh_pos[0][0]) + ", " + str(neigh_pos[0][1]) + ")"
    if row - 1 >= 0 :
        output_string = output_string + "(" + str(neigh_neg[0][0]) + ", " + str(neigh_neg[0][1]) + ")"
    if coloumn + 1 < colmax :
        output_string = output_string + "(" + str(neigh_pos[1][0]) + ", " + str(neigh_pos[1][1]) + ")"
    if coloumn - 1 >= 0:
        output_string = output_string + "(" + str(neigh_neg[1][0]) + ", " + str(neigh_neg[1][1]) + ")"
    print(output_string)
#Iterating through starting locations and feeding them into the function in order to get neighbor locations
for i in start_loc : 
    get_locs(i[0],i[1],rows,coloumns)

path = hw5_util.get_path(int(grid_n))
downward = 0
upward = 0
valid_checker = 0
#Checking the validity of a path by obtaining and adding path differences
for i in range(len(path)) : 
    if path[i] == path[-1] : 
        break
    else : 
        difx = abs(path[i][0] - path[i+1][0])
        dify = abs(path[i][1] - path[i+1][1])
        diftotal = difx + dify
        if diftotal > 1: 
            print("Path: invalid step from",path[i],"to",path[i+1])
        else : 
            valid_checker = valid_checker + 1
            difelev = (pulled_grid[path[i][0]][path[i][1]] - pulled_grid[path[i+1][0]][path[i+1][1]])
            if difelev > 0 : 
                downward = downward + abs(difelev)
            elif difelev < 0: 
                upward = upward + abs(difelev)
if valid_checker == len(path)-1 : 
    print("Valid path")
    print("Downward",downward)
    print("Upward",upward)
        