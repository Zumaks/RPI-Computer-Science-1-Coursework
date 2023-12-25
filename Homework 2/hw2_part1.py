import math
#Setting up volume finding functions
def find_volume_sphere(x) : 
    volume = (4/3) * (math.pi)  * (x**3)
    return volume
def find_volume_cube(x) : 
    volume = x**3
    return volume

#Collecting user input
radius = input("Enter the gum ball radius (in.) =>").strip()
print(" " + radius )

weekly_sales = input("Enter the weekly sales =>").strip()
print(" " + weekly_sales + "\n")

#Processing weekly sales and radius information into required forms
gumball_totalnum = math.ceil(float(weekly_sales)*1.25 )
required_gumball = math.ceil(gumball_totalnum ** (1/3))
print("The machine needs to hold",required_gumball,"gum balls along each edge.")
edge_len = required_gumball * (float(radius) * 2)
formatted_edge_len = format(edge_len, '.2f')
print("Total edge length is", formatted_edge_len,"inches.")
found_vol = find_volume_cube(float(radius) * 2)
sphere_rad = find_volume_sphere(float(radius))
wasted_space = (found_vol - sphere_rad)
wasted_space_target = find_volume_cube(edge_len) - (gumball_totalnum*found_vol) + (wasted_space*gumball_totalnum)
othergum = (required_gumball**3) - gumball_totalnum
wasted_space2 = find_volume_cube(edge_len) - ((gumball_totalnum+othergum) * sphere_rad)
#Altering format of data in a manner which will work with the submitty expected ouput
formatted_wasted_space_target = format(wasted_space_target, '.2f')
formatted_wasted_space_target2 = format(wasted_space2, '.2f')
#Printing the last of the processed information
print("Target sales were", str(gumball_totalnum) + ", but the machine will hold", othergum, "extra gum balls.")
print("""Wasted space is""", formatted_wasted_space_target,"""cubic inches with the target number of gum balls,
or""",formatted_wasted_space_target2,"""cubic inches if you fill up the machine.""")

