from BerryField import BerryField2
class Bears() : 
    def __init__(self,reserve,active):
         self.reserve = reserve
         self.active = active
    def __str__(self) : 
        string = ''
        for i in self.reserve : 
            string = string +  "Bear at " + str((i[0],i[1])) + " moving " + i[2] + " Asleep" + "\n"
        for i in self.active : 
            string = string +  "Bear at " + str((i[0],i[1])) + " moving " + i[2] + " Awake" + "\n"
        return string
    def walk(self) : 
        for i in range(len(self.active)) : 
            if self.active[i][2] == "N" :
                self.active[i][1] == self.active[i][1] + 1
            elif self.active[i][2] == "S" :
                self.active[i][1] == self.active[i][1] - 1 
            elif self.active[i][2] == "W" : 
                self.active[i][0] == self.active[i][0] - 1 
            elif self.active[i][2] == "E" : 
                self.active[i][0] == self.active[i][0] + 1 
            elif self.active[i][2] == "NE" : 
                self.active[i][0] == self.active[i][0] + 1 
                self.active[i][1] == self.active[i][1] + 1
            elif self.active[i][2] == "SE" : 
                self.active[i][0] == self.active[i][0] + 1 
                self.active[i][1] == self.active[i][1] - 1
            elif self.active[i][2] == "SW" : 
                self.active[i][0] == self.active[i][0] - 1 
                self.active[i][1] == self.active[i][1] - 1
            elif self.active[i][2] == "NW" : 
                self.active[i][0] == self.active[i][0] - 1 
                self.active[i][1] == self.active[i][1] + 1
    def consume(self,field,tourists) : 
        self.field = field 
        self.tourists = tourists
        field_grid = BerryField2(self.field,self.active,self.tourists)
        array_field = field_grid.pull_grid()
        for i in range(len(self.active)) : 
            self.active[i].append(0)
        for i in range(len(self.active)) : 
            if self.active[i][3] < 30 and ([self.active[i][0],self.active[i][1]] not in self.tourists): 
                array_field[self.active[i][0]][self.active[i][1]] = 0 
        return array_field


            
