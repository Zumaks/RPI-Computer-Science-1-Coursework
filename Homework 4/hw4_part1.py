password = input("Enter a password => ").strip()
print(password)
game_score = 0

#Setting up functions for each score criteria

def length(pw,score) : 
    #Checking length of password to determine its strength
    if len(pw) == 6 or len(pw) == 7 : 
        score = score + 1
        print("Length: +1")
    elif len(pw) == 8 or len(pw) == 9 or len(pw) == 10 :
        print("Length: +2") 
        score = score + 2
    elif len(pw) > 10 : 
        print("Length: +3")
        score = score + 3

    return score

def case(pw,score) :
    #Checking count of each type of cases with isupper() to determine strength of password
    count_upper = 0
    count_lower = 0
    for i in pw : 
        if i.isupper() == True: 
            count_upper = count_upper + 1
        elif i.isupper() == False:
            count_lower = count_lower + 1

    if count_upper >= 2 and count_lower >- 2 :
        score = score + 2
        print("Cases: +2")
    elif count_upper == 1 and count_lower >= 1 or count_upper >= 1 and count_lower == 1 : 
        score = score + 1
        print("Cases: +1")

    return score

def digits(pw,score) : 
    #Checking count of digits in password through the use of isnumeric()
    digit_count = 0
    for i in pw : 
        if i.isnumeric() == True : 
            digit_count = digit_count + 1
    if digit_count >= 2 :
        score = score + 2
        print("Digits: +2")
    elif digit_count == 1 : 
        score = score + 1
        print("Digits: +1")

    return score

def punctuation(pw,score) : 
    #Checking to see if any of punc_vals1 or punc_vals2 elements are in password as those strengthen it
    punc_vals1 = "!@#$"
    punc_vals2 = "%^&*"
    count_punc_vals_1 = 0
    count_punc_vals_2 = 0
    for i in pw : 
        for x in punc_vals1 : 
            if i == x : 
                count_punc_vals_1 = 1
        for x in punc_vals2 :
            if i == x :
                count_punc_vals_2 = 1
    if count_punc_vals_2 != 0 : 
        score = score + 1
        print("%^&*: +1")
    if count_punc_vals_1 != 0 : 
        score = score + 1
        print("!@#$: +1")
    
    return score

def NY_License(pw,score) : 
    #Checking to see that password does not match up with a potential license plate which would decrease it's security
    for i in range(len(pw)): 
        count = 0
        count2 = 0
        for x in pw[i:i+3] : 
            if x.isalpha() == True : 
                count = count + 1
        if count == 3 : 
            for x in pw[i+3 : i+7] : 
                if x.isnumeric() == True : 
                    count2 = count2  + 1
            if count2 == 4 : 
                score = score - 2
                print("License: -2")
    return score

def common_password(pw,score) : 
    #Checking to see if password matches with list of common passwords which could be easily guessed
    common_passwords = open("password_list_top_100.txt","r")
    for i in common_passwords : 
        if i.strip() == pw.lower() : 
            score = score - 3
            print("Common: -3")
    return score
#Calling all functions and determining the strength of the password
game_score = length(password,game_score)
game_score = case(password,game_score)
game_score = digits(password,game_score)
game_score = punctuation(password,game_score)
game_score = NY_License(password,game_score)
game_score = common_password(password,game_score)
print("Combined score:",game_score)
if game_score <= 0 : 
    print("Password is rejected")
if game_score == 1 or game_score == 2 :
    print("Password is poor")
if game_score == 3 or game_score == 4 :
    print("Password is fair")
if game_score == 5 or game_score == 6 :
    print("Password is good")
if game_score >= 7 : 
    print("Password is excellent")
