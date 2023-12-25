import math
#Collecting user input
frame_char = input("Enter frame character ==> ").strip()
print(frame_char)
height = input("Height of box ==> ").strip()
print(height)
width = input("Width of box ==> ").strip()
print(width + "\n")

print("Box:")
#Printing edge of box
print(frame_char * int(width))
#Processing height and width information to create the body of the box without the use of if statements or loops
z = int(height)/2
zx = math.ceil(z - 2)
x = '{0}' * zx
x2 = frame_char + (" " * (int(width)-2)) + frame_char + "\n"
body = x.format(x2)
print(body[:body.rfind('\n')])
vals = width + "x" + height
mathed = ((int(width)-len(vals))/2) -1
mathed1 = math.ceil(mathed)
mathed2 = math.floor(mathed)
mid_string = frame_char + (" " * int(mathed2)) + vals + (" " * int(mathed1)) + frame_char
print(mid_string)
x = '{0}' * (int(int(height)/2) - 1)
x2 = frame_char + (" " * (int(width)-2)) + frame_char + "\n"
body = x.format(x2)
#Printing the edge and last row of the body
print(body[:body.rfind('\n')])
print(frame_char * int(width))



