"""2) Write a program that randomly colours the N first integer numbers using n (the n colours must be present)."""
import random

W = '\033[0m'   #white
R = '\033[31m'  #red
G = '\033[32m'  #green
O = '\033[33m'  #orange
B = '\033[34m'  #blue
P = '\033[35m'  #purple

color = [W,R,G,O,B,P]                                                               #declaration of the list of all colours
choosen_color = []                                                                  #declaration of the list with n colours

N = int(input("Please enter the number of integer you want to display : "))         #number of integer we want to display
n = int(input("Please enter the number of colors you want : "))                     #number of colours

while n > N or n > 6:                                                               #loop for n < N and n < 6 (the length of the list color)
    print("the number of color must be less than the number of integers and less than 6(the number of colours we have)")
    N = int(input("Please enter the number of integers you want to display : "))
    n = int(input("Please enter the number of colors you want : "))

for j in range(1, N + 1) :                                                           #loop for display the N first integers
    if len(choosen_color) == 0 :                                                     #loop for create a list with the number of color we choose
        for i in range(n) :        
            choosen_color.append(color[i])
    rand_color = random.choice(choosen_color)
    
    print(rand_color, j, end='')                                                     #display the colored number
    choosen_color.remove(rand_color)                                                 #delete the choosen color because the n colours must be present