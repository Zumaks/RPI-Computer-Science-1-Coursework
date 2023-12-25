#Setting up sentiment analyzing happy and sad functions
def number_happy(sentence): 
    laughs = (sentence.lower()).count("laugh") 
    happiness = (sentence.lower()).count("happiness") 
    love = (sentence.lower()).count("love") 
    excellent = (sentence.lower()).count("excellent") 
    good = (sentence.lower()).count("good") 
    smile = (sentence.lower()).count("smile") 
    sum = laughs + happiness + love + excellent + good + smile 
    return sum

def number_sad(sentence):
    bad = (sentence.lower()).count("bad") 
    sad = (sentence.lower()).count("sad") 
    terrible = (sentence.lower()).count("terrible") 
    horrible = (sentence.lower()).count("horrible") 
    problem = (sentence.lower()).count("problem") 
    hate = (sentence.lower()).count("hate")
    sum = bad + sad + terrible + horrible + problem + hate
    return sum

#Feeding user specified input into the functions and comparing results to determine final judgement on user inputs sentiment
user_input = input("Enter a sentence =>").strip()
print(" " + user_input)

print("Sentiment:","+" * number_happy(user_input) + "-" * number_sad(user_input))
if number_happy(user_input) < number_sad(user_input) : 
    print("This is a sad sentence.")
if number_happy(user_input) > number_sad(user_input) : 
    print("This is a happy sentence.")
if number_happy(user_input) == number_sad(user_input): 
    print("This is a neutral sentence.")