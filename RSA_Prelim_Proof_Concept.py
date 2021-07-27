'''
Sofia Medina - Algorithmic Investigation Summer 2021
Rushed Compilation -- "Proof-of-Concept"

Created: July 27 2021
'''

from generate_random_prime_RSA import generateRandomPrime
from Carmicheals_Totient_Function_RSA import CarmichealsTotient
from Eulers_Totient_Function_RSA import EulersTotient
from Key_pair_generation_RSA import *
from Encryption_Decryption_RSA import *

#arbitrary primes
p,q = generateRandomPrime(100,200), generateRandomPrime(100,200)

#modulus n
n = p*q

#totient val
totient1 = EulersTotient(p,q)
totient2 = CarmichealsTotient(p,q)

#exponent e
e1 = choosePublicKeyExponentE(totient1)
e2 = choosePublicKeyExponentE(totient2)



#exponent d
d1 = calculatingPrivateKeyExponentD(totient1, e1)
d2 = calculatingPrivateKeyExponentD(totient2, e2)


#plaintext message M
M = int(input("For this test plz numerical messages only: "))

#encrypt
C1 = encrypt(M,e1, n)
C2 = encrypt(M, e2, n)

print("Ciphertext using Eulers:", C1)
print("Ciphertext using Carmicheal:", C2)

#decrypt
M1 = decrypt(C1, d1, n)
M2 = decrypt(C2, d2, n)

print("\n\nDecrypted Plaintext using Eulers:", M1)
print("Decrypted Plaintext using Carmicheal:", M2)



