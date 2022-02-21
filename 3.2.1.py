"""Write a program that colours, and displays, the N first integer numbers with two colours, the even numbers are coloured in red, and the odd numbers are coloured in blue."""
import random        

R = '\033[31m'  #Declaring Red Color
B = '\033[34m'  #Declaring Blue Color

list_N_integer = []   #Declaration of the list 

N = int(input("Please enter the number of integer you want to display : "))    #Asking the user for the number of integers he wants to display


for j in range(1,N+1):                          #Adding each integer from 1 to N into the list
    list_N_integer.append(j)
    

for i in list_N_integer :                                  
    if i % 2 == 0 :                             #Checking if the number at the position i in the list is an even number 
        print(R, i, end='')                     #Printing the even number at the position i in red (R) and in line 
    else :                                      #Checking if the number at the position i in the list is an odd number 
        print(B, i, end='')                     #Printing the odd number at the position i in blue (B) and in line 
