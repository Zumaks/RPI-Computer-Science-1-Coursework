import json
from BerryField import BerryField2
from Bear import Bears
from Tourist import Tourist
JSON_name = input("Enter the json file name for the simulation => ").strip()
print(JSON_name + "\n")
opened_JSON = open(JSON_name)
data = json.loads(opened_JSON.read())
# print(data["berry_field"])
# print(data["active_bears"])
# print(data["reserve_bears"])
print_var = data["active_tourists"].copy()

x = BerryField2(data["berry_field"],data["active_bears"],data["active_tourists"])
z = Bears(data["reserve_bears"],data["active_bears"])
print("Field has",x.__numberr__(), "berries.")
print(x)
# print(BerryField2(z.consume(data["berry_field"],data["active_tourists"]),data["active_bears"],data["active_tourists"]))
print("\n" + "Active Bears:")
for i in data["active_bears"] : 
    print("Bear at (" + str(i[0]) + "," + str(i[1]) + ") moving " + i[2])

print("\n" + "Active Tourists:")
for i in print_var : 
    print("Tourist at (" + str(i[0]) + "," + str(i[1]) + "), 0 turns without seeing a bear.")



y = Tourist(data["active_tourists"],data["reserve_tourists"])
list_of_sights = y.see_bear(data["active_bears"],0)

