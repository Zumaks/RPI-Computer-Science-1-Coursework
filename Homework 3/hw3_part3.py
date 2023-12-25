import math
#Collecting input and setting up variables
bears = int(input("Number of bears => ").strip())
print(bears)
berries = input("Size of berry area => ").strip()
print(berries)
if "." in berries : 
    berries = float(berries)
else : 
    berries = int(berries)
tourists = 0
i = 0
list_max_bears = []
list_max_berries = []
list_max_tourists = []

#Creation of the find_next function which specifies what happens if the # of berries becomes negative and finds next years berries/bears

def find_next(berries,bears,tourists) : 
    bears_next = berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1)
    bears_next = int(bears_next)
    berries_next = (berries*1.5) - (bears+1)*(berries/14) - \
    (math.log(1+tourists,10)*0.05)
    if berries_next < 0 : 
        berries_next = 0
    return (berries_next,bears_next)


#A loop is created whose length is the number of years as each coloumn/row is filled with the information from the find_next function
print("{: >0} {: >10} {: >10} {: >10}".format("Year","Bears","Berry","Tourists"))
while i < 10 : 
    if i == 0 : 
        if int(bears) < 4 or int(bears) > 15 : 
            tourists = 0
        else : 
            if int(bears) <= 10 : 
                tourists = 10000 * int(bears)
            else : 
                tourists = (10000* 10) + (20000 * (int(bears) - 10))
        print("{: >0} {: >10} {: >13} {: >8}".format(i+1, bears,"{:.1f}".format(berries),tourists))
        list_max_bears.append(bears)
        list_max_berries.append(berries)
        list_max_tourists.append(tourists)
        i = i +1
    else : 
        berries, bears = find_next(berries,bears,tourists)
        if int(bears) < 4 or int(bears) > 15 : 
            tourists = 0
        else : 
            if int(bears) <= 10 : 
                tourists = 10000 * int(bears)
            else : 
                tourists = (10000* 10) + (20000 * (int(bears) - 10))
        if i+1 >= 10 : 
            print("{: >0} {: >9} {: >13} {: >8}".format(i+1, bears,"{:.1f}".format(berries),tourists))
        else : 
            print("{: >0} {: >10} {: >13} {: >8}".format(i+1, bears,"{:.1f}".format(berries),tourists))
        i = i +1

        list_max_bears.append(bears)
        list_max_berries.append(berries)
        list_max_tourists.append(tourists)
#The mininimum and maximum values are found by appending all found values into their own seperated lists and then using the min/max functions
print("\n"+"Min:{: >8} {: >13} {: >4}".format(min(list_max_bears),"{:.1f}".format(min(list_max_berries)),min(list_max_tourists)))
print("Max:{: >8} {: >13} {: >8}".format(max(list_max_bears),"{:.1f}".format(max(list_max_berries)),max(list_max_tourists)))


