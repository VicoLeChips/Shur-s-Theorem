"Write a program that displays the interval to which belongs S(n) for n (n >= 6)."

n = int(input("Please enter the number of colors : "))

def fact(n) :                                                  #Function to calculate a factorial number                          
    result = 1
    for i in range(1,n + 1) :
        result = result*i
    return result

min = ((3**n)-1)/2                                             #Compute the minimum of the interval 
max = (3*fact(n))-1                                            #Compute the maximum of the interval

print("The theoreticle results for ", n,"colors is :", min, "≤ S("+str(n)+") ≤", max)