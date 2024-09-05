#Irving 
#decoratorsassi
#5/09/2024

#assuming there are no doors or windows and each wall paper piece covers an area of 2 meteres squared, the same applies to the carpet
length =int(input("Please enter the length of the room"))
breadth =int(input("Please enter the breadth of the room"))
height =int(input("please enter the height of the room"))

area_floor = length * breadth
print(area_floor)
walls_area= (2*length *height) + (2*breadth *height)

numberofwallpaper = walls_area/2
numberofcarpet = area_floor/2 
litresofpaint = walls_area /2

print("you will need" , numberofwallpaper, "and" , numberofcarpet "pieces of carpet and you will need" , litresofpaint, "litres of paint")
