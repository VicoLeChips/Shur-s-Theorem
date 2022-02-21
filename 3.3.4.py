"""4) Write a program that colours the N first numbers with n colours, and checks whether the n colours are present in the colouring."""
import random

W = '\033[0m'   #white
R = '\033[31m'  #red
G = '\033[32m'  #green
O = '\033[33m'  #orange
B = '\033[34m'  #blue
P = '\033[35m'  #purple

all_color = [W,R,G,O,B,P]   #list of all color
my_color = []               #list of my color
colorlist = []              #list of random colors pick
number_color_choosen = 0

N = int(input("Please enter the value of N : "))
n = int(input("Please enter the value of n (max 6) : "))
while n <= 0 or n > 6:
    print("n can't be less or equal to 0 or more than 6")
    n = int(input("Please re-enter the value of n (max 6) : "))


for j in range(n) :                                                #Adding the number of colors choosen by the user into a list (my_color)
    my_color.append(all_color[j])

    
print("Let’s consider the following colouring : ", end='')         #Randomly colours N first integer
for i in range(N) :
    colorlist.append(random.choice(my_color))                      #Mixing the colors into a new list (colorlist)
    if colorlist.count(colorlist[i]) == 1 :                        #Counting how many colors are present
        number_color_choosen += 1
    print(colorlist[i], i+1, end='')                               #Printing the integers with its corresponding colors
print(W, " for n =", n, " and N =", N, ".")                          

if number_color_choosen == n :                                     #Printing the corresponding result
    print("All the colors are present")
else :
    print("Not all the colors are present")