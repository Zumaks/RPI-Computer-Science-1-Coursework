#Encrypting each portion of a string
def encrypt (x) : 
    if " a" in x :
        x = x.replace(" a", "%4%")
    if "he" in x :
        x = x.replace("he", "7!")
    if "e" in x :
        x = x.replace("e", "9(*9(")
    if "y" in x :
        x = x.replace("y", "*%$")
    if "u" in x :
        x = x.replace("u", "@@@")
    if "an" in x :
        x = x.replace("an", "-?")
    if "th" in x :
        x = x.replace("th", "!@+3")
    if "o" in x :
        x = x.replace("o", "7654")
    if "9" in x:
        x = x.replace("9", "2")
    if "ck" in x:
        x = x.replace("ck","%4")
    return x
#Decrypting each portion of encrypted string
def decrypt (x) : 
    if "%4" in x:
        x = x.replace("%4","ck")
    if "2" in x:
        x = x.replace("2", "9")
    if "7654" in x :
        x = x.replace("7654", "o")
    if "!@+3" in x :
        x = x.replace("!@+3", "th")
    if "*%$" in x :
        x = x.replace("*%$", "y")
    if "-?" in x :
        x = x.replace("-?", "an")
    if "@@@" in x :
        x = x.replace("@@@", "u")
    if "9(*9(" in x :
        x = x.replace("9(*9(", "e")
    if "7!" in x :
        x = x.replace("7!", "he")
    if "%4%" in x :
        x = x.replace("%4%", " a")
    return x
#Collecting input and feeding it in to functions
input_string = input("Enter a string to encode ==>").strip()
print(" " + input_string + "\n")
stored = encrypt(input_string)
print("Encrypted as ==>", stored)
len_dif = abs(len(input_string) - len(encrypt(input_string)))
print("Difference in length ==>",len_dif)
print("Deciphered as ==>",decrypt(stored))
#Outputting/printing results of decryption 
if decrypt(stored) == input_string : 
    print("Operation is reversible on the string.")
else : 
    print("Operation is not reversible on the string.")
