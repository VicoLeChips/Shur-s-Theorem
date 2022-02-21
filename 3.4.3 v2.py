"""3) Generalize the previous program to compute S(n) for n > 2. """

import time
# Start counting of time
start_time = time.time()




def binaire(nombre, bits, n):

    quotient = 1
    restes_successifs = []
    while (quotient != 0):                                          # Tant que le quotient est nul, on répète l'algorithme vu en cours:
        quotient = nombre // n                                      # on divise le résultat précédent par n et on note le reste
        reste = nombre % n
        restes_successifs.append(reste)
        nombre = quotient
    for i in range (len(restes_successifs), bits):
        restes_successifs.append(0)
    restes_successifs.reverse()                                     # On inverse la liste pour lire les restes de la fin au début

    for i in range(0, len(restes_successifs)):
        if (restes_successifs[i] > 9):
            restes_successifs[i] = chr(restes_successifs[i] + 55)   # Si la valeur est supérieure à 9, on la convertit en une lettre
    return restes_successifs


color = []
list_conf = []

n = 2
i = 0
N = 0


not_monocromatic = True


while not_monocromatic == True:
    N += 1
    print(N)
    not_monocromatic = False
    while not_monocromatic == False and i < (n**N)/n:
        not_monocromatic = True      
        list_conf = binaire(i, N, n)
        for a in range(1,N):
            for b in range(1,N):
                if a + b <= N and a<=b:
                    if list_conf[a-1] == list_conf[b-1] == list_conf[a+b-1]:
                        not_monocromatic = False

        i += 1                
                
print("the value of S(",n,") is : ", N-1)

# Displays the execution time
print("Execution time: %s seconds ---" % (time.time() - start_time))