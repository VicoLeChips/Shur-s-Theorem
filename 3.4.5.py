"""Based on the following code, calculate the execution time to compute S(n)."""
import time
start_time = time.time()

#Initializing variables          
list_conf = []              #List of all colours configuration
i = 0                       #Index to stop the loop if we don't find a polychromatic triplet
n = 2
N = int(((3**n)-1)/2)       #Compute the minimum of the interval ; N first numbers with n colours
not_monochromatic = True    #Boolean which is true if the triplet is polychromatic


def base_converter(number, bits, n) :                             #Function which converts a decimal number into any base (=configuration of n colours)     
    quotient = 1
    successive_rest = []
    while (quotient != 0) :                                       #While the quotient is null, we repeat the following algorithm
        quotient = number // n                                    #We divide the number by its base to get the quotient
        rest = number % n                                         #We find the rest by computing the modulo of the number by its base
        successive_rest.append(rest)                              #We add to the list (successive_rest) the rest
        number = quotient                                         #We declared the number as the quotient
    for i in range (len(successive_rest), bits) :
        successive_rest.append(0)
    successive_rest.reverse()                                     #We reverse the list to read the MSB and LSB in the right order
    return successive_rest                                        #Return a list which corresponds to a configuration



while not_monochromatic == True:                                             #Run until it reaches a value of N for which their is no more configuration without monochromatic triplet
    N += 1                                                                   #Increment N until their is no more configuration without monochromatic triplet
    not_monochromatic = False                                                #We are supposing it's false in order to change the variable to true inside the loop if an entire configuration of triplets is true (Basically to enter the loop)
    while not_monochromatic == False and i < (n**N)/n:                       #Run until we found a configuration with only polychromatic triplet or until we reach the end of the possible configuration (and we are dividing by n, because with n colours, it's working as a mirror)
        not_monochromatic = True                                             #We are supposing it's true in order to change the variable to false inside the loop if an entire configuration of triplets is true (Basically to enter the loop)
        list_conf = base_converter(i, N, n)                                  #Create a list of configurations which has for a primary number i
        a = 1                                                                #a has to start at 1
        while ((not_monochromatic == True) and (a <= N)):                    #Loop to increment a (it's a while because we do not know the number of iterations, and we want it to quit the loop once it has found a monochromatic triplet)
            b = a                                                            #b has to be equal or greater than a
            while ((not_monochromatic == True) and (b <= N) and (a + b <=N)):                #Loop to increment b (it's also a while because we do not know the number of iterations, and we want it to quit the loop once it has found a monochromatic triplet)                                             #To check if a+b is in the range of N
                if (list_conf[a-1] == list_conf[b-1] == list_conf[a+b-1]):   #To check if the previous configuration (list_conf) is monochromatic 
                    not_monochromatic = False                                #If it's monochromatic we change the variable which allow us to quit the n while loop and chnage the configuration
                b += 1
            a += 1       
        i += 1
    #We don't reinitialized i, because we know that if a configuration is false for a smaller N, then it will also be false for the next N
                
       
print("The value of S(",n,") is : ", N-1)                                         #We display N-1, because N-1 was the last value of N where we have found a configuration with no monochromatic triplets


print("Execution time: %s seconds ---" % (time.time() - start_time))