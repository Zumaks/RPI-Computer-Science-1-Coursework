import copy
class BerryField2() : 
#Collecting and Processing data from JSON file in order to create a new grid containing locations of Tourists and Bears
    def __init__(self,grid1,bears,tourists):
        self.grid1 = grid1
        self.grid2 = copy.deepcopy(self.grid1)
        self.locs = []
        both = []
        temp_bears = []
        for i in bears : 
            temp_bears.append(i[0:2])
        for i in temp_bears : 
            if [i[0],i[1]] in tourists : 
                temp_bears.remove([i[0],i[1]])
                tourists.remove([i[0],i[1]])
                both.append([i[0],i[1]])
        for i in range(len(self.grid1)) : 
            temp_list = []
            for x in range(len(self.grid1[i])) : 
                temp_list.append((i,x))
                for z in temp_bears : 
                    if x == z[0] and i == z[1] and [z[0],z[1]] not in tourists: 
                        self.grid2[x][i] = "B"
                for z in tourists : 
                    if x == z[0] and i == z[1] and [z[0],z[1]] not in temp_bears: 
                        self.grid2[x][i] = "T"
                for z in both : 
                    if x == z[0] and i == z[1] and [z[0],z[1]]: 
                        self.grid2[x][i] = "X"
            self.locs.append(temp_list)

    def pull_grid(self): 
        return self.grid1
#Creation of function responsible for the growth of berries in the field through the use of indexing and a 2D loop
    def grow_berries(self): 
        for i in range(len(self.grid1)) : 
            for z in range(len(self.grid1[i])) : 
                if self.grid1[i][z] >= 1 and self.grid1[i][z] < 10 : 
                    self.grid1[i][z] = self.grid1[i][z] + 1
            for z in range(len(self.grid1[i])) :
                if i + 1 >= len(self.grid1) and z + 1 < len(self.grid1[i]):
                    if self.grid1[i][z] == 0 and (self.grid1[i-1][z] == 10 or self.grid1[i][z -1] == 10 or self.grid1[i][z + 1] == 10):
                        self.grid1[i][z] = self.grid1[i][z] + 1
                elif z + 1 >= len(self.grid1[i]) and i + 1 < len(self.grid1): 
                    if self.grid1[i][z] == 0 and (self.grid1[i+1][z] == 10 or self.grid1[i-1][z] == 10 or self.grid1[i][z -1] == 10):
                        self.grid1[i][z] = self.grid1[i][z] + 1
                elif z + 1 >= len(self.grid1[i]) and i + 1 >= len(self.grid1) : 
                    if self.grid1[i][z] == 0 and (self.grid1[i-1][z] == 10 or self.grid1[i][z -1] == 10):
                        self.grid1[i][z] = self.grid1[i][z] + 1
                else : 
                    if self.grid1[i][z] == 0 and (self.grid1[i+1][z] == 10 or self.grid1[i-1][z] == 10 or self.grid1[i][z -1] == 10 or self.grid1[i][z + 1] == 10):
                        self.grid1[i][z] = self.grid1[i][z] + 1
        return self.grid1
#Set-Up of Function responsible for producing print statement output
    def __str__(self):
        final_str = ""
        for i in self.grid2 : 
            z = []
            for x in i : 
                z.append("{:>4}".format(x))
            final_str = final_str + "".join(z) + "\n"
        return final_str
# Function responsible for calculating the number of berries in a field
    def __numberr__(self) : 
        sum_berries = 0
        for i in self.grid1 : 
            sum_berries = sum_berries + sum(i)
        return sum_berries
            
            