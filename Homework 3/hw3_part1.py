from syllables import find_num_syllables
paragraph = input("Enter a paragraph => ")
print(paragraph)
paragraph = paragraph.strip()
splitted_par = paragraph.split()
hard_words = []

#Each statistic is organized into its own function where it is computed for simplicities sake
def ASL(par) : 
    global asl
    asl = []
    sums = 0
    aslval = 0
    for i in par: 
        if i[-1] == "." : 
            asl.append(aslval)
            aslval = 0 
        else : 
            aslval = aslval + 1
    for i in asl : 
        sums = sums + i
    final_avg = sums/len(asl) + 1
    return final_avg
def PHW(par) : 
    hrcount = 0
    for i in par:
        num_syll = find_num_syllables(i)
        if num_syll == 3 and "-" not in i and i[-2] + i[-1] != ("es" or "ed"): 
            hrcount = hrcount + 1
            hard_words.append(i)
        if num_syll > 3 and "-" not in i : 
            hrcount = hrcount + 1
            hard_words.append(i)
    PHW = float(hrcount /len(splitted_par)) * 100
    return PHW

def AYSL(par) : 
    total_syll = 0
    for i in par:
        total_syll = total_syll+ find_num_syllables(i)
    aysl = total_syll/len(splitted_par)
    return aysl

def GFRI(ASL,PHW) : 
    gfri = 0.4*(ASL + PHW)
    return gfri

def FKRI(ASL, ASYL) : 
    fkri = 206.835-(1.015*ASL)-(86.4*ASYL)
    return fkri

#Final computed results are formatted and printed
print("Here are the hard words in this paragraph:")
PHW(splitted_par)
print(hard_words)
print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(ASL(splitted_par),PHW(splitted_par),AYSL(splitted_par)))
print("Readability index (GFRI): {:.2f}".format(GFRI(ASL(splitted_par),PHW(splitted_par))))
print("Readability index (FKRI): {:.2f}".format(FKRI(ASL(splitted_par),AYSL(splitted_par))))
