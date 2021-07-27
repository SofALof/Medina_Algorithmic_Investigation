'''
Sofia Medina - Algorithmic Investigation Summer 2021
key pair generation (e,d)
(Chosing exponent e and determining exponent d)

Created: July 24 2021
'''

from generate_random_prime_RSA import generateRandomPrime
from Extended_Euclidean_Algorithm import modularMultiplicativeInverse

#E must be chose according to the following conditions: 
    #1 < e < totient; additionally e must be co-prime to the totient value

#to make calculation ezier going to make e prime - and ensure its not a factor of
#the totient

def choosePublicKeyExponentE (totient):

    while True:
        rPrime = generateRandomPrime

        if totient % rPrime != 0:
            return rPrime


def calculatingPrivateKeyExponentD(totient, e):
        d = modularMultiplicativeInverse(e, totient)
    
