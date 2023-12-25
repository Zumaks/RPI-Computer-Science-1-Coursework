import json
from BerryField import BerryField2
from Bear import Bears
from Tourist import Tourist
JSON_name = input("Enter the json file name for the simulation => ").strip()
print(JSON_name + "\n")
opened_JSON = open(JSON_name)
data = json.loads(opened_JSON.read())
print_var = data["active_tourists"].copy()
#Initial State of Sim : 
samp = BerryField2(data["berry_field"],data["active_bears"],data["active_tourists"])
print("Field has",samp.__numberr__(), "berries.")
print(samp)
# print(BerryField2(z.consume(data["berry_field"],data["active_tourists"]),data["active_bears"],data["active_tourists"]))
print("\n" + "Active Bears:")
for i in data["active_bears"] : 
    print("Bear at (" + str(i[0]) + "," + str(i[1]) + ") moving " + i[2])

print("\n" + "Active Tourists:")
for i in print_var : 
    print("Tourist at (" + str(i[0]) + "," + str(i[1]) + "), 0 turns without seeing a bear.")

# Loop Len 5
for i in range(0,5) : 
    x = BerryField2(data["berry_field"],data["active_bears"],data["active_tourists"])
    y = Tourist(data["active_tourists"],data["reserve_tourists"])
    z = Bears(data["reserve_bears"],data["active_bears"])

    x.grow_berries()
    z.walk()
    z.consume(x.pull_grid(),y.pull_tourists())
    list_of_sights = y.see_bear(data["active_bears"],0)
    y.leavefield(list_of_sights,i)
    print("Field has",x.__numberr__(), "berries.")
    print(x)








# print(BerryField2(z.consume(data["berry_field"],data["active_tourists"]),data["active_bears"],data["active_tourists"]))
# print(y.__str__(list_of_sights,i))