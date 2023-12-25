from curses.ascii import isalpha
import hw4_util
trufal = True

#Setting up functions for each request for simplicities sake

def daily(data,state):
    for i in data : 
        for x in data : 
            if x[0] == state : 
                pop = x[1]
                avg = 0
                for z in x[2:9] : 
                    avg = avg + z
                avgper100k = (avg/7)
    return "Average daily positives per 100K population: " + str(round((avgper100k/pop)*100000, ndigits=1))
def pct(data,state) : 
    avg1 = 0
    avg2 = 0
    for i in data : 
        for x in data: 
            if x[0] == state : 
                for z in x[2:9] : 
                    avg1 = avg1 + z
                avg1 = (avg1)/7
                for z in x[9:16] : 
                    avg2 = avg2 + z
                avg2 = avg2/7
                finalavg = round((avg1/(avg1+avg2)) * 100, ndigits=1)
    return "Average daily positive percent: " + str(finalavg)
def quar(data) : 
    list_of_states = []
    avg1 = 0 
    avg2 = 0
# Preforming the same operations as in daily and pct only for all lists in the 2D array 
# NOTE: daily and pct functions were not called in quar due second argument state
    for i in range(len(data)) : 
        for x in data[i] : 
            pop = int(data[i][1])
            avg = 0
            for z in data[i][2:9] : 
                avg = avg + z
            avg2 = avg/7
        avgper100k = (avg2/pop)*100000
        for x in data[i]: 
            for z in data[i][2:9] : 
                avg1 = avg1 + z
            avg1 = (avg1)/7
            for z in data[i][9:16] : 
                avg2 = avg2 + z
            avg2 = avg2/7
        finalavg = (avg1/(avg1+avg2)) * 100
# Comparison of results to find all quarantine states
        if avgper100k > 10 or finalavg > 10 : 
            list_of_states.append(data[i][0])
    print('Quarantine states:')
    hw4_util.print_abbreviations(list_of_states)

def high(data) : 
    high_list1 = []
    high_list2 = []
    for i in range(len(data)) : 
        for x in data[i] : 
            pop = int(data[i][1])
            avg = 0
            for z in data[i][2:9] : 
                avg = avg + z
            avg2 = avg/7
        avgper100k = (avg2/pop)*100000
        high_list1.append(avgper100k)
        high_list2.append(data[i][0])
    # Finding the max value's location in high_list1 to find its corresponding abberviation
    maxval = max(high_list1)
    abv = high_list2[high_list1.index(maxval)]
    print('State with highest infection rate is {}'.format(abv))
    print('Rate is {:.1f} per 100,000 people'.format(maxval))






#Starting the actual loop of the function
while trufal : 
    #Setting up conditions 
    print("...")
    user_input = input("Please enter the index for a week: ").strip()
    print(user_input)
    if isalpha(user_input[0]) == True:
        print("No data for that week")
    elif int(user_input) > 29: 
        print("No data for that week")
    elif int(user_input) < 0 : 
        trufal = False
    else : 
        input_type = input("Request (daily, pct, quar, high): ").strip()
        print(input_type)
        hw4_util.part2_get_week(user_input)
        week_data = hw4_util.part2_get_week(int(user_input))
        #Calling all functions and checking to see if inputted states are actual states (Error checking is preformed as well)
        abvvals = []
        for i in range(len(week_data)) : 
            abvvals.append(week_data[i][0])
        if input_type.lower() == "daily" : 
            state = input("Enter the state: ").strip()
            print(state)
            if state in abvvals : 
                print(daily(week_data,state))
            else : 
                print("State",state,"not found")
        elif input_type.lower() == "pct" : 
            state = input("Enter the state: ").strip()
            print(state)
            if state in abvvals : 
                print(pct(week_data,state))
            else : 
                print("State",state,"not found")
        elif input_type.lower() == "quar" : 
            quar(week_data)
        elif input_type.lower() == "high" : 
            high(week_data)
        else : 
            print("Unrecognized request")
