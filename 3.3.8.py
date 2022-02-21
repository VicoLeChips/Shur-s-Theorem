"""8) Generalise the previous program to convert a decimal number to a number in a base b (>1)."""

quotient = 1                                        #Initializing variables
successive_rest = []

number = int(input("Please enter a decimal number : "))
base = int(input("Please enter the base : "))


while (quotient != 0) :                             #While the quotient is not null, we repeat the following algorithm
    quotient = number // base                       #We divide the number by its base to get the quotient
    rest = number % base                            #We find the rest by computing the modulo of the number by its base
    successive_rest.append(rest)                    #We add to the list (successive_rest) the rest
    number = quotient                               #We declared the number as the quotient
    
successive_rest.reverse()                           #We reverse the list to read the MSB and LSB in the right order
    
for i in range(0, len(successive_rest)):
    if (successive_rest[i] > 9):
        successive_rest[i] = chr(successive_rest[i] + 55)      #If the value is bigger than 9, it converts it into a letter 


print("Your decimal number base", base, "is", successive_rest)