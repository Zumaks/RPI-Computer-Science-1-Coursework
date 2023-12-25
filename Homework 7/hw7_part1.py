#String is imported to iterate through alphabet without having to create a list of all the letters by hand
import string
#Collecting and storing user input
dict_file = input("Dictionary file => ").strip()
print(dict_file)
input_file = input("Input file => ").strip()
print(input_file)
keyboard_file = input("Keyboard file => ").strip()
print(keyboard_file)
alphabet = list(string.ascii_lowercase)
dict_file_open = open(dict_file)
#Processing user input into desired formats
dictionary = dict()
for i in dict_file_open : 
    temp_list = i.replace("\n","").split(",")
    dictionary[temp_list[0]] = temp_list[1]

keyboard_open = open(keyboard_file)
keyboard = dict()
for i in keyboard_open : 
    temp_list = i.split()
    keyboard[temp_list[0]] = temp_list[1:]

input_file_open = open(input_file)
file_input = []
for i in input_file_open : 
    temp_list = i.replace("\n","")
    file_input.append(temp_list)
#Iterating through all words in need of auto correction and proceeding to make the required modifications
for i in file_input : 
    i.strip()
    if i in dictionary.keys() : 
        stringe = i + " -> FOUND"
        print(f"{stringe:>24}")
    else : 
#Drop
        temp_list = []
        for x in range(len(i)) : 
            temp_char_list = list(i)
            del temp_char_list[x]
            temp_string = "".join(temp_char_list)
            if temp_string in dictionary.keys() : 
                temp_list.append(temp_string)
#Insert
        if len(set(temp_list)) == 0 :
            for x in range(len(i)) : 
                for z in alphabet : 
                    if x == len(i)-1 : 
                        temp_string = i + z
                        if temp_string in dictionary.keys() : 
                            temp_list.append(temp_string)
                    elif x == 0 : 
                        temp_string = z + i
                        if temp_string in dictionary.keys() : 
                            temp_list.append(temp_string)
                    else : 
                        temp_string = i[:x] + z + i[x:]
                    if temp_string in dictionary.keys() : 
                        temp_list.append(temp_string)
#Swap
        for x in range(len(i)) :
            if x+1 == len(i) : 
                continue
            else : 
                temp_string = i[:x] + i[x+1] +i[x] + i[x+2:]
                if temp_string in dictionary.keys() : 
                    temp_list.append(temp_string)
#Replace
        for x in range(len(i)): 
            for z in keyboard.keys() : 
                if i[x] == z :
                    for y in keyboard[z] : 
                        temp_char_list = list(i)
                        temp_char_list[x] = y
                        temp_string = "".join(temp_char_list)
                        if temp_string in dictionary.keys() : 
                            temp_list.append(temp_string)
#Checking to see if no auto corrected version of the word was created
        if len(set(temp_list)) == 0 :
            stringe = i + " -> NOT FOUND"
            print(f"{stringe:>28}")
#Sorting, processing and printing program output 
        else : 
            sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
            temp_float_list = []
            for x in sorted_dict.keys() : 
                for z in temp_list : 
                    if x == z : 
                        temp_float_list.append(x)
                        
            stringed = (" -> FOUND" + "  " + str(len(list(dict.fromkeys(temp_float_list[0:3])))) + ":  " + " ".join(list(dict.fromkeys(temp_float_list[0:3]))))
            print(f"{i:>15}{stringed:>15}")