"""Based on the previous programs and the problem description (see the table to illustrating S(2)),
write a program to compute S(2). """

#Initializing variables          
list_conf = []              #List of all colours configuration
i = 0                       #Index to stop the loop if we don't find a polychromatic triplet
N = 0                       #N first numbers with n colours
not_monochromatic = True    #Boolean which is true if the triplet is polychromatic


def binaries(number, bits) :                                      #Function which converts a decimal number into a binary number (=configuration of 2 colours)     
    quotient = 1
    successive_rest = []
    while (quotient != 0) :                                       #While the quotient is null, we repeat the following algorithm
        quotient = number // 2                                    #We divide the number by its base (here it's 2) to get the quotient
        rest = number % 2                                         #We find the rest by computing the modulo of the number by its base (here it's 2) 
        successive_rest.append(rest)                              #We add to the list (successive_rest) the rest
        number = quotient                                         #We declared the number as the quotient
    for i in range (len(successive_rest), bits) :
        successive_rest.append(0)
    successive_rest.reverse()                                     #We reverse the list to read the MSB and LSB in the right order
    return successive_rest                                        #Return a list which corresponds to a configuration



while not_monochromatic == True:                                             #Run until it reaches a value of N for which their is no more configuration without monochromatic triplet
    N += 1                                                                   #Increment N until their is no more configuration without monochromatic triplet
    not_monochromatic = False                                                #We are supposing it's false in order to change the variable to true inside the loop if an entire configuration of triplets is true (Basically to enter the loop)
    while not_monochromatic == False and i < (2**N)/2:                       #Run until we found a configuration with only polychromatic triplet or until we reach the end of the possible configuration (and we are dividing by 2, because with 2 colours, it's working as a mirror)
        not_monochromatic = True                                             #We are supposing it's true in order to change the variable to false inside the loop if an entire configuration of triplets is true (Basically to enter the loop)
        list_conf = binaries(i, N)                                           #Create a list of configurations which has for a primary number i
        a = 1                                                                #a has to start at 1
        while ((not_monochromatic == True) and (a <= N)):                    #Loop to increment a (it's a while because we do not know the number of iterations, and we want it to quit the loop once it has found a monochromatic triplet)
            b = a                                                            #b has to be equal or greater than a
            while ((not_monochromatic == True) and (b <= N)and(a + b <= N)): #Loop to increment b (it's also a while because we do not know the number of iterations, and we want it to quit the loop once it has found a monochromatic triplet)
                if (list_conf[a-1] == list_conf[b-1] == list_conf[a+b-1]):   #To check if the previous configuration (list_conf) is monochromatic 
                    not_monochromatic = False                                #If it's monochromatic we change the variable which allow us to quit the 2 while loop and chnage the configuration
                b += 1
            a += 1       
        i += 1
    #We don't reinitialized i, because we know that if a configuration is false for a smaller N, then it will also be false for the next N
                
       
print("The value of S(2) is : ", N-1)                                         #We display N-1, because N-1 was the last value of N where we have found a configuration with no monochromatic triplets