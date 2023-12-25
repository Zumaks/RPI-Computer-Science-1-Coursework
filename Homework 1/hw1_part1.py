#Set-Up Empty Lists to place input into
names = []
adj = []
noun = []
verb = []
emotion = []
teamname = []
season = []
name_input = input("""Let's play Mad Libs for Homework 1
Type one word responses to the following:

proper_name ==> """).strip()
print(name_input)
names.append(name_input)
adj_input1 = input("adjective ==> ").strip()
print(adj_input1)
adj.append(adj_input1)
noun_input1 = input("noun ==> ").strip()
print(noun_input1)
noun.append(noun_input1)
verb_input1 = input("verb ==> ").strip()
print(verb_input1)
verb.append(verb_input1)
verb_input2 = input("verb ==> ").strip()
print(verb_input2)
verb.append(verb_input2)
noun_input2 = input("noun ==> ").strip()
print(noun_input2)
noun.append(noun_input2)
emotion_input1 = input("emotion ==> ").strip()
print(emotion_input1)
emotion.append(emotion_input1)
verb_input3 = input("verb ==> ").strip()
print(verb_input3)
verb.append(verb_input3)
noun_input3 = input("noun ==> ").strip()
print(noun_input3)
noun.append(noun_input3)
season_input = input("season ==> ").strip()
print(season_input)
season.append(season_input)
adj_input2 = input("adjective ==> ").strip()
print(adj_input2)
adj.append(adj_input2)
emotion_input2 = input("emotion ==> ").strip()
print(emotion_input2)
emotion.append(emotion_input2)
teamname_input = input("team-name ==> ").strip()
print(teamname_input)
teamname.append(teamname_input)
noun_input4 = input("noun ==> ").strip()
print(noun_input4)
noun.append(noun_input4)
adj_input3 = input("adjective ==> ").strip()
print(adj_input3 + "\n")
adj.append(adj_input3)


ex_string = """Good morning <proper name>!

  This will be a/an <adjective> <noun>! Are you <verb> forward to it?
  You will <verb> a lot of <noun> and feel <emotion> when you do.
  If you do not, you will <verb> this <noun>.

  This <season> was <adjective>. Were you <emotion> when <team-name> won
  the <noun>?

  Have a/an <adjective> day!""".strip()
word = ""
count = 0
#Seeing how each peice of user input corresponds to the place of its placeholder in ex_string the input list can be looped 
#through and its elements used to replace the placeholders
for i in names :
    ex_string = ex_string.replace("<proper name>", i,1)
for i in adj :
    ex_string = ex_string.replace("<adjective>", i,1)
for i in noun :
    ex_string = ex_string.replace("<noun>", i,1)
for i in verb :
    ex_string = ex_string.replace("<verb>", i,1)
for i in emotion :
    ex_string = ex_string.replace("<emotion>", i,1)
for i in teamname :
    ex_string = ex_string.replace("<team-name>", i,1)
for i in season :
    ex_string = ex_string.replace("<season>", i,1)

#Printing the final version of ex_string
print("Here is your Mad Lib... \n")
print(ex_string)
