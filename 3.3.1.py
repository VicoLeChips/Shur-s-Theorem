"""1) Write a program check if a given coloured triplet is monochromatic or not. The input of this program is a triplet and its colouring."""

W = '\033[0m'   #Declaring white Color
R = '\033[31m'  #Declaring red Color
G = '\033[32m'  #Declaring green Color
O = '\033[33m'  #Declaring orange Color
B = '\033[34m'  #Declaring blue Color
P = '\033[35m'  #Declaring purple Color

dictionary_color = {'white': W, 'red': R, 'green': G, 'orange': O, 'blue': B, 'purple': P}     #Declaration of the dictionary of the different colors

print("The following colors are implemented in the program: white, red, green, orange, blue, purple")  #Showing to the user the different colors that are available

a = int(input("Please enter the first value of the triplet : "))      
color_first_value = input("Enter its color (in full letters) : ")                       

b = int(input("Please enter the second value of the triplet : "))    
color_second_value = input("Enter its color (in full letters) : ")                      

c = int(input("Please enter the third value of the triplet : "))      
color_third_value = input("Enter its color (in full letters) : ")                      

while a + b != c or dictionary_color.get(color_first_value) == None or dictionary_color.get(color_second_value) == None or dictionary_color.get(color_third_value) == None : #Checking if the user had entered the right informations above
    a = int(input("Please enter the first value of the triplet : "))       
    color_first_value = input("Enter its color (in full letters) : ")                      

    b = int(input("Please enter the second value of the triplet : "))    
    color_second_value = input("Enter its color (in full letters) : ")                    

    c = int(input("Please enter the third value of the triplet : "))      
    color_third_value = input("Enter its color (in full letters) : ")                     
    

if color_first_value == color_second_value == color_third_value and a + b == c :   #Checking if the color of the three value are the same AND if the first value + the second value = the third value
    print("The triplet (", dictionary_color[color_first_value], a , W,",", dictionary_color[color_second_value], b, W,",",dictionary_color[color_third_value], c, W, ") is monochromatic") #Printing to the user that the triplet is monochromatic
else :
    print("The triplet (", dictionary_color[color_first_value], a, W, ",", dictionary_color[color_second_value], b, W, ",",dictionary_color[color_third_value], c, W, ") is not monochromatic") #Printing to the user that the triplet is not monochromatic