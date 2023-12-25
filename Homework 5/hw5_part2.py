from turtle import pu
from xml.dom import pulldom
import hw5_util
looplen = True
while looplen : 
    grid_n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
    print(grid_n)
    if int(grid_n) <= 3 and int(grid_n) >= 0 :
        looplen = False
    else : 
        looplen = True

pulled_grid = hw5_util.get_grid(int(grid_n))
grid_string = []
rows = len(pulled_grid)
coloumns = len(pulled_grid[0])
max_step = input("Enter the maximum step height: ").strip()
print(max_step)
prinnt = input("Should the path grid be printed (Y or N): ")
print(prinnt)
print("Grid has",rows,"rows and",coloumns,"columns")
start_loc = hw5_util.get_start_locations(int(grid_n))
def get_locs(row,coloumn,rowmax,colmax) : 
    neigh_neg = [(row - 1,coloumn),(row,coloumn - 1)]
    neigh_pos = [(row + 1,coloumn),(row,coloumn + 1)]
    results = []
    output_string = "Neighbors of ("+str(row) + ", " + str(coloumn)  + "): "
    if row + 1 < rowmax :
        output_string = output_string + "(" + str(neigh_pos[0][0]) + ", " + str(neigh_pos[0][1]) + ")" 
        results.append((neigh_pos[0][0],neigh_pos[0][1]))
    if row - 1 > 0 :
        output_string = output_string + "(" + str(neigh_neg[0][0]) + ", " + str(neigh_neg[0][1]) + ")"
        results.append((neigh_neg[0][0],neigh_neg[0][1]))
    if coloumn + 1 < colmax :
        output_string = output_string + "(" + str(neigh_pos[1][0]) + ", " + str(neigh_pos[1][1]) + ")"
        results.append((neigh_pos[1][0],neigh_pos[1][1]))
    if coloumn - 1 > 0:
        output_string = output_string + "(" + str(neigh_neg[1][0]) + ", " + str(neigh_neg[1][1]) + ")"
        results.append((neigh_neg[1][0],neigh_neg[1][1]))

    return results
neigh_locs= []
for i in start_loc : 
    neigh_locs.append(get_locs(i[0],i[1],rows,coloumns))


max_finder = []
for i in pulled_grid : 
    for x in i : 
        max_finder.append(x)

max_finder.sort()
global_max = max_finder[-1]
for i in range(len(pulled_grid)) : 
    if global_max in pulled_grid[i] : 
        global_max_loc = (i,pulled_grid[i].index(global_max))

end_not_found = False
loc = 0
while end_not_found: 
    for i in neigh_locs : 
        loc = neigh_locs.index(i)
        neigh_locs[loc] = get_locs(i[0],i[1],rows,coloumns)
print("global max:",global_max_loc,global_max)
print("===")