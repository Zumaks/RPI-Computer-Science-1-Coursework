#Obtaining and storing user_input
min = input("Minutes ==> ")
print(min)
seconds = input ("Seconds ==> ")
print(seconds)
miles = input ("Miles ==> ")
print(miles)
targetmiles = input ("Target Miles ==> ")
print(targetmiles + "\n")

#Calculating and converting float elements of values into minutes 
sectomin = int(seconds)/60
pace = (int(min)+sectomin) / float(miles)
strpace = str(pace)
decpace = strpace[strpace.find(".") : -1]
minutes = strpace[0: strpace.find(".") ]
seconds = int(float(decpace) * 60)
#The moment that each peice of output is obtainned inn it's final form it is printed
print("""Pace is""",minutes,"""minutes and""", seconds,"""seconds per mile.""")
speed =format(float(60/pace), '.2f')
print("""Speed is""",speed,"""miles per hour.""")
target_time = float(targetmiles) * pace
target = str(target_time)
tarpace = target[target.find(".") : -1]
minutes2 = target[0: target.find(".") ]
seconds2 = int(float(tarpace) * 60)
formatted_targetmiles = format(float(targetmiles), '.2f')
print("""Time to run the target distance of""",formatted_targetmiles,"""miles is""", minutes2,"""minutes and""",seconds2,"""seconds.""")