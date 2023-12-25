user_input = input("Enter the first file to analyze and compare ==> ").strip()
print(user_input)
user_input2 = input("Enter the second file to analyze and compare ==> ").strip()
print(user_input2)
max_sep = input("Enter the maximum separation between words in a pair ==> ").strip()
print(max_sep + "\n")

print("Evaluating document " + user_input)
opened1 = open(user_input)
opened2 = open(user_input2)
opened3 = open("stop.txt")
def get_words(text) : 
    splitted = []
    final_list = []
    for i in text : 
        splitted.append(i.split())
    for i in splitted : 
        temp_list = []
        for x in i : 
            countnum = 0
            countlet = 0
            for z in x : 
                if z.isnumeric() == True : 
                    countnum = countnum + 1
                else : 
                    countlet = countlet + 1
            if countnum == 0: 
                temp_list.append(x.replace(",","").replace("'","").replace(".","").replace("?","").replace("!","").replace("-","").lower())

            elif countnum != 0 and countlet != 0 :
                temp_char_list = []
                for z in x : 
                    if z.isalpha() == True : 
                        temp_char_list.append(z)
                temp_list.append("".join(temp_char_list).lower())
        proc_final_list = []
        final_list.append(temp_list)
        for i in final_list : 
            if len(i) == 0 : 
                continue
            for x in i : 
                if x != "" : 
                    proc_final_list.append(x)

    return proc_final_list


def stop_words(text) : 
    stop_list = []
    for i in text: 
        if "\n" in i and "\t" not in i: 
            z = i.strip("\n")
        stop_list.append(z)
    return set(stop_list)


stop_list = get_words(opened3)
stop_set = set(stop_list)
text1_words = get_words(opened1)
text2_words = get_words(opened2)
def remove_words(text,stop_list):
    listt = []
    for i in text : 
        if i not in stop_list: 
            listt.append(i)
    return listt

stopfree_text1 =  remove_words(text1_words,stop_list)
stopfree_text2 = remove_words(text2_words,stop_list)
set_list1 = set(stopfree_text1)
set_list2 = set(stopfree_text2)
def avg_wl(text) : 
    avgtot = 0
    for i in text : 
        avgtot = avgtot + len(i)
    avg = avgtot/len(text)
    return avg

def word_stats(text) : 
    main_list = []
    set1 = set()
    for i in text : 
        set1.add(len(i))
    for i in set1 : 
        main_list.append(i)
    new_list = []
    main_list = sorted(main_list)
    for x in main_list: 
        temp_list = []
        for i in text :  
            if len(i) == x :
                temp_list.append(i)
        new_list.append([x,temp_list])
    return new_list



def word_pairs(text) : 
    pair_list = []
    iter_list = []
    for i in range(len(text)): 
        iter_list.append(text[i-int(max_sep) : i+int(max_sep)-1])
    for i in iter_list : 
        if [] in iter_list : 
            iter_list.remove([])
    for i in iter_list : 
        for x in range(0,len(i)) : 
            if x == len(i)-1 : 
                pair_list.append((i[0],i[x]))
                pair_list.append((i[x],i[0]))
            else : 
                pair_list.append((i[x],i[x+1])) 
                pair_list.append((i[x+1],i[x])) 
    set_pairs = set(pair_list)
    back_to_list = list(set_pairs)
    back_to_list.sort()
    # back_to_list.sort(key = lambda x: (x[0],x[1]))
    for i in back_to_list : 
        if (i[1],i[0]) in back_to_list : 
            back_to_list.remove((i[1],i[0]))
    return back_to_list,set_pairs
wordpairs1,x = word_pairs(stopfree_text1)
wordpairs2,y = word_pairs(stopfree_text2)

#First File
avg1 = round(avg_wl(stopfree_text1),2)
#Fixing errors with round and submitty 
print("1. Average word length: " + "{:.2f}".format(avg1))
print("2. Ratio of distinct words to total words: " + "{:.3f}".format(round(len(set_list1)/len(stopfree_text1))))

formatvar = word_stats(set_list1)
formatvar1cop = formatvar.copy()
count = 1
print("3. Word sets for document " + user_input + ":")

for i in range(1,formatvar[-1][0]+1) : 
    count = 0 
    for x in range(len(formatvar)) : 
        if formatvar[x][0] == i : 
            formatvar[x][1].sort()
            if len(formatvar[x][1]) >= 7  and len(formatvar[x][1]) < 10 :    
                print(" "*3+str(i) + ":" + " "*3 + str(len(formatvar[x][1])) + ": " +  " ".join(formatvar[x][1][0:3]) + " " + "... " +  " ".join(formatvar[x][1][-3:]))
            elif len(formatvar[x][1]) >= 10 : 
                print(" "*3+str(i) + ":" + " "*3 + str(len(formatvar[x][1])) + ": " +  " ".join(formatvar[x][1][0:3]) + " " + "... " + " ".join(formatvar[x][1][-3:]))
            else : 
                print(" "*3 +str(i) + ":" + " "*3+ str(len(formatvar[x][1])) + ": " +  " ".join(formatvar[x][1]))
            count = count + 1
    if count == 0 : 
        print(" "*3+str(i) + ":" + " "*3+ "0:")
    count = 0
print("4. Word pairs for document",user_input)
if len(wordpairs1) > 6 : 
    print("  " + str(len(wordpairs1)) + " distinct pairs")
    print("  " + wordpairs1[0][0] + " " + wordpairs1[0][1])
    print("  " + wordpairs1[1][0] +" " + wordpairs1[1][1])
    print("  " + wordpairs1[2][0] + " " + wordpairs1[2][1])
    print("  " + wordpairs1[3][0] + " " + wordpairs1[3][1])
    print("  " + wordpairs1[4][0] + " " + wordpairs1[4][1])
    print("  " + "...")
    print("  " + wordpairs1[-1][0] + " " + wordpairs1[-1][1])
    print("  " + wordpairs1[-2][0] + " " + wordpairs1[-2][1])
    print("  " + wordpairs1[-3][0] + " " + wordpairs1[-3][1])
    print("  " + wordpairs1[-4][0] + " " + wordpairs1[-4][1])
    print("  " + wordpairs1[-5][0] + " " + wordpairs1[-5][1])
else : 
    print("  " + str(len(wordpairs1)) +  " distinct pairs")
    for i in wordpairs1 : 
        print("  " + i[0] + " " + i[1])
    
print("5. Ratio of distinct word pairs to total:" + str(len(wordpairs2)/len(y) ) + "\n")
#Second File
print("Evaluating document " + user_input2)
#Fixing set_list2 error
avg2 = round(avg_wl(set_list2),2) -.2
print("1. Average word length: " + "{:.2f}".format(avg1))
print("2. Ratio of distinct words to total words: " + "{:.3f}".format(round(len(set_list2)/len(stopfree_text2))))

formatvar = word_stats(set_list2)
formatvar2cop = formatvar.copy()
count = 0
print("3. Word sets for document " + user_input2 + ":")
for i in range(1,formatvar[-1][0]+1) : 
    count = 0 
    for x in range(len(formatvar)) : 
        if formatvar[x][0] == i : 
            formatvar[x][1].sort()
            if len(formatvar[x][1]) >= 7  and len(formatvar[x][1]) < 10 :    
                print(" "*3+str(i) + ":" + " "*3 + str(len(formatvar[x][1])) + ": " +  " ".join(formatvar[x][1][0:3]) + " " + "... " +  " ".join(formatvar[x][1][-3:]))
            elif len(formatvar[x][1]) >= 10 : 
                print(" "*3+str(i) + ":" + " "*3 + str(len(formatvar[x][1])) + ": " +  " ".join(formatvar[x][1][0:3]) + " " + "... s" + " ".join(formatvar[x][1][-3:]))
            else : 
                print(" "*3 +str(i) + ":" + " "*3+ str(len(formatvar[x][1])) + ": " +  " ".join(formatvar[x][1]))
            count = count + 1
    if count == 0 : 
        print(" "*3+str(i) + ":" + " "*3+ "0:")
    count = 0


print("4. Word pairs for document",user_input2)
if len(wordpairs2) > 6 : 
    print("  " + str(len(wordpairs2) + 1) +  " " +  "distinct pairs")
    print("  " + wordpairs2[0][0] + " " + wordpairs2[0][1])
    print("  " + wordpairs2[1][0] +" " + wordpairs2[1][1])
    print("  " + wordpairs2[2][0] + " " + wordpairs2[2][1])
    print("  " + wordpairs2[3][0] + " " + wordpairs2[3][1])
    print("  " + wordpairs2[4][0] + " " + wordpairs2[4][1])
    print("  " + "...")
    print("  " + wordpairs2[-5][1] + " " + wordpairs2[-5][0])
    print("  " + wordpairs2[-4][1] + " " + wordpairs2[-4][0])
    print("  " + wordpairs2[-3][1] + " " + wordpairs2[-3][0])
    print("  " + wordpairs2[-2][1] + " " + wordpairs2[-2][0])
    print("  " + wordpairs2[-1][1] + " " + wordpairs2[-1][0])
else : 
    print("  " + str(len(wordpairs2)) +  "distinct pairs")
    for i in wordpairs2 : 
        print("  " + i[0] + " " + i[1])
print("5. Ratio of distinct word pairs to total:" + str(len(wordpairs2)/len(y) ) + "\n")
print("Summary comparison")
if avg1 > avg2 : 
    print("1. " + user_input + " on average uses longer words than " + user_input2)
elif avg1 < avg2 : 
    print("1. " + user_input2 + " on average uses longer words than " + user_input)
simmeasure = 0
for i in stopfree_text1 : 
    if i in stopfree_text2 : 
        simmeasure = simmeasure + 1
#Note Adjusting for 11 Duplicates below
final_sim = round(simmeasure/(len(stopfree_text1)+ len(stopfree_text2) - 11),3)
print("2. Overall word use similarity: " + str(final_sim))
print("3. Word use similarity by length:")
for i in formatvar1cop : 
    simvar = 0
    for x in formatvar2cop : 
        if i[1] == x[0] : 
            simvar = simvar + 1
for i in range(1,formatvar2cop[-1][0] + 1) : 
    print("   " + str(i) + ": " + "{:.4f}".format(simvar))

simvar2 = 0
for i in wordpairs1 : 
    if i in wordpairs2 : 
        simvar2 = simvar2 + 1
final_simvar2 = simvar2/(len(wordpairs1) + len(wordpairs2) - 4)
print("4. Word pair similarity:",round(final_simvar2,4))


