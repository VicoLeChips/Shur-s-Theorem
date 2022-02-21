"""7) Write a program that converts a decimal number to a binary one (e.g.11 -> 1011)."""


quotient = 1                                        #Initializing variables
successive_rest = []

number = int(input("Please enter a decimal number : "))


while (quotient != 0) :                             #While the quotient is not null, we repeat the following algorithm
    quotient = number // 2                          #We divide the number by its base (here it's 2) to get the quotient
    rest = number % 2                               #We find the rest by computing the modulo of the number by its base (here it's 2) 
    successive_rest.append(rest)                    #We add to the list (successive_rest) the rest
    number = quotient                               #We declared the number as the quotient
    
successive_rest.reverse()                           #We reverse the list to read the MSB and LSB in the right order
    


print("Your number in binary is : ", successive_rest) #Printing the result