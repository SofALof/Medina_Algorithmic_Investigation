'''
Sofia Medina - Algorithmic Investigation Summer 2012
Generating Random Primes

Created: July 27 2021
'''

from Primality_Test import primalityTest
import random

#primes take the form 6k+1 (so for their to be a higher likelyhood on random r
#being a prime -- the nums will be randomly generated to take that form)

def generateRandomPrime(lowerBound, upperBound):

    while True: 
        k = random.randint(lowerBound, upperBound)
        rPrime = 6*k+1

        if primalityTest(rPrime):
            return rPrime


#rP = generateRandomPrime(100,200)
#print(rP)
    
