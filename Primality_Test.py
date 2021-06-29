'''
Sofia Medina - Algorithmic Investigation Summer 2021
Primality Test: 6k+-1 Optimization

Created: June 29 2021
'''
import math

def primalityTest(n):

    if n <= 3: #checks small numbers (easily done as only 2 and 3 are Prime)
        return n>1

    if n % 2 == 0 or n % 3 == 0: #optimization to check if divisible by 2 or 3
        return False

    i = 5 #helper integer taking the form 6k-1

    radN = math.sqrt(n) #last val that needs to b cross-refrenced
    while i <= radN: 

        if n % i == 0 or n % (i+2) == 0: #check n against all forms of 6k+-1 
            return False                                # Note that i+2 = 6k+1

        i += 6 #move i to the next iteration of 6k-1

    return True


### Explanation of Algorithm ###
'''

##Three Initial Optimizations ##
    n <= 3
        - serves to weed out negative numbers
        - 0, 1, 2, and 3 as they are kinda "funky" and do not always hold to the
        general rules
        - The above numbers are also small enough where it is easy to take this liberty

  if  n mod 2 == 0
        - checks if the number is even
        - and if it is even that it is pretty obviously not prime

    if n mod 3 == 0
        - checks if the number is divisible by 3 and so such not prime

##The While Loop##
- Prime numbers take the form 6k+-1
- When checking if a number N is prime it is only necceasry to check the PRIME numbers
less than sqrt(N) --> (as all other numbers will contain the above primes)


i = 5 <-- the first instance of 6k-1

while  i <= rad(n) <-- breaks if all possible primes have been checked or if i > rad(n)

if n mod i == 0 or n mod i+2 == 0 <-- checks if n is divisible by potential primes 6k+1
                                                        (i takes the form 6k-1 and i+2 takes the form 6k+1)

i += 6 <-- brings i to the next iteration of 6k-1




'''

print(primalityTest(2))#prime
print(primalityTest(19))#prime
print(primalityTest(10302123))#composite
print(primalityTest(82589933))#prime
print(primalityTest(215)) #composite
