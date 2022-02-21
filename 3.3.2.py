"""3.3.2) Write a program that generates all triplets (a,b,a+b) avec a, b, a+b for a, b, a+b ≤ p, for a given value p."""

p = int(input("Please enter the value of p : "))

while p <= 0:
    print("p can't be less than 1")
    p = int(input("Please re-enter the value of p : "))

for a in range(1,p):                 #Loop to give all the value to a
    for b in range(1,p):             #Loop to give all the value to b
        if a + b <= p and a<=b:      #Condition to print a triplet : a <= b because the triplet where a > b are the same
            print(a,b,a+b)           #Print all triplets