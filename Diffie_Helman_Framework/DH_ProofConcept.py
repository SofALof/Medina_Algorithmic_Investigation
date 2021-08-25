'''
Sofia Medina - Algorithmic Investigation Summer 2021
Diffie-Helman test implementation

Created: August 25 2021
'''

from generate_random_prime_DH import generateRandomPrime

#agreed upon shared (public) modulo
p = generateRandomPrime(100,200)

print(p)
