"""9) Write a program to store all the possible colourings of the N first integer numbers with n colours. The program then displays this list."""


i = 0                                                             #Initializing list and variables
color_possibilities = []                                          #list of possibilities

N = int(input("Please enter the value of N : "))
n = int(input("Please enter the value of n : "))

while N <= 0 :                                                   
    print("N can't be less or equal to 0")
    N = int(input("Please re-enter the value of N : "))

while n <= 0 :                                                   
    print("n can't be less or equal to 0")
    n = int(input("Please re-enter the value of n : "))
    
    
def base_converter(number, bits, n) :                                    #Function to convert a number into any base
    quotient = 1
    successive_rest = []
    while (quotient != 0) :                                        #while the quotient is null, we repeat the following algorithm
        quotient = number // n                                     #we divide the last result by n et we write the rest
        rest = number % n
        successive_rest.append(rest)
        number = quotient
    for i in range (len(successive_rest), bits) :
        successive_rest.append(0)
    successive_rest.reverse()                                      #We reverse the list to read the MSB and LSB in the right order
    return successive_rest


while i != n ** N :                                                #Adding all the possibilities until we hit n^N possibilities
    color_possibilities.append(base_converter(i, N, n))                  #Adding all the possibilities from 0 to N into a list
    i += 1
    
print("The list of different possibilities is :\n", color_possibilities)       #Printing the list of possibilities 
    