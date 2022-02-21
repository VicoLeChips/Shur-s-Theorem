"""3) Write a program that randomly colours N first integer numbers, for a given N.
Then, the program evaluates the predicate and displays the result i.e.,
it displays TRUE if all triplets are not monochromatic, and FALSE otherwise."""
import random

W = '\033[0m'   #white
R = '\033[31m'  #red
B = '\033[34m'  #blue

color = [R,B]             
not_monochromatic = True   #TRUE if all triplets are not monochromatic, and FALSE otherwise == We pretend it's true 
colorlist = []            #list of random colors pick
monochromatic_counter = 0 #Initializing the counter to 0

N = int(input("Please enter the value of N : "))

while N <= 1 :
    N = int(input("Please re-enter a positiv value for N : "))

print("Let’s consider the following colouring:", end='')                       
for i in range(N):
    colorlist.append(random.choice(color))                                     #Adding randomly the two coulors into a new list from 1 to N 
    print(colorlist[i], i+1, end='')                                           #Printing all the numbers from 1 to N with the corresponding colors from the list
print(W," for n = 2 and N =", N, ".") 

print(W,"\nThe corresponding triplets are :")                                  #Displaying the corresponding triplets
for a in range(1,N) :
    for b in range(1,N) :
        if a + b <= N and a<=b :                                               #Conditions to find a triplet
            print(colorlist[a-1],a,colorlist[b-1],b,colorlist[a+b-1],a+b)
            if colorlist[a-1] == colorlist[b-1] == colorlist[a+b-1] :          #Conditions to find monochromatic triplets
                not_monochromatic = False
                monochromatic_counter +=1                                      #Counting how many monochromatic triplets there is


if not_monochromatic == False :
    if monochromatic_counter == 1 :
        print(W, "One triplet is monochromatic : ", end="")
    else :
        print(W, monochromatic_counter, "triplets are monochromatic : ", end="")
else :
    print(W, "None is monochromatic : ", end="")
print(not_monochromatic)