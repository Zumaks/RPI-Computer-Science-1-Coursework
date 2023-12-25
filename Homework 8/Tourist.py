from BerryField import BerryField2
from Bears import Bears
import math
class Tourist() : 
    def __init__(self,active,reserves):
        self.active = active
        self.reserves = reserves
#Creating a function appending True/False values to a list based on whether or not the tourist sees a bear. 
    def see_bear(self,bear_locs,turnval) : 
        self.bear_locs = bear_locs
        self.turnval = turnval
        list_of_sights = []
        for i in self.active : 
            temp_list = []
            for x in self.bear_locs : 
                dist = math.sqrt(((i[0] - x[0])**2) + ((i[1] - x[1])**2))
                if dist <= 4 : 
                    temp_list.append([i,True,self.turnval + 1])
                elif dist == 0 :
                    self.active.remove(i)
                else : 
                    temp_list.append([i,False])
            list_of_sights.append(temp_list)
        return list_of_sights
#Defining print statement output
    def __str__(self,list_of_sights,turnval) : 
        self.turnval = turnval
        string = ""
        stored_vals = []
        self.list_of_sights = list_of_sights
        for i in self.list_of_sights : 
            temp_list = []
            for x in i : 
                if x[1] == True : 
                    temp_list.append([x[0],x[2]])
                else : 
                    temp_list.append([x[0],"X"])
            stored_vals.append(temp_list)
        for i in stored_vals : 
            if i[0][1] != "X": 
                string = string + "Tourist at (" + str(i[0][0][0]) + "," + str(i[0][0][1]) + "), " + str(int(i[0][1]) - self.turnval) + " turns without seeing a bear." + "\n"
        return string
#Checking to see if tourists are supposed to leave the field
    def leavefield(self,list_of_sighted,turnval) :  
        self.list_of_sighted = list_of_sighted 
        self.turnval = turnval
        for i in self.list_of_sighted : 
            counter = 0
            for x in i : 
                if x[1] == True and self.turnval - x[2] == 3:
                    self.active.remove(x[0])
                    counter = counter + 1
            if counter == 0 :
                self.active.remove(i[0][0])
            elif counter >= 3 :
                self.active.remove(i[0][0])
    def pull_tourists(self) : 
        return self.active
        
            
        
            
            
                
        
                





                

