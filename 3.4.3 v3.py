"""3) Generalize the previous program to compute S(n) for n > 2. """

import time
# Start counting of time
start_time = time.time()




def binaries(number, bits, n) :
    quotient = 1
    successive_rest = []
    while (quotient != 0) :                         #while the quotient is null, we repeat the following algorithm
        quotient = number // n                      #we divide the last result by n et we write the rest
        rest = number % n
        successive_rest.append(rest)
        number = quotient
    for i in range (len(successive_rest), bits) :
        successive_rest.append(0)
    successive_rest.reverse()                       #We reverse the list to read the MSB and LSB in the right order
    
    for i in range(0, len(successive_rest)):
        if (successive_rest[i] > 9):
            successive_rest[i] = chr(successive_rest[i] + 55)      #If the value is bigger than 9, it converts it into a letter
    return successive_rest


color = []
list_conf = []

n = 3
i = 0
N = 0


not_monochromatic = True


while not_monochromatic == True:
    N += 1
#    print(N)
    not_monochromatic = False
    while not_monochromatic == False and i < (n**N)/n:
        not_monochromatic = True      
        list_conf = binaries(i, N, n)
        a = 1
        while ((not_monochromatic == True) and (a < N)):
            b = a
            while ((not_monochromatic == True) and (b < N)):
                if (a + b <= N):
                    if (list_conf[a-1] == list_conf[b-1] == list_conf[a+b-1]):
                        not_monochromatic = False
                b += 1
            a +=1       

        i += 1                
                
 
        
print("the value of S(",n,") is : ", N-1)

# Displays the execution time
print("Execution time: %s seconds ---" % (time.time() - start_time))