'''
Sofia Medina - Algorithmic Investigation Summer 2021
Encryption and Decryption Proccesses
(must have private/public keys available AND THE PLAINTEXT/CIPHERTEXT)

Created: July 27 2021
'''

#NOTE THAT AS OF RN...THIS IS ONLY GOING TO WORK NUMERICALLY CUZ IM #LAZY


# M = plaintext message (as per convention)
# e = encryption exponent e
# n = totient value

def encrypt(M, e, n):

    return (M**e) % n

# C = ciphertext message (encrypted message, as per convention)
# d = decryption exponent d
# n = totient value

def decrypt(C, d, n):

    return (C**d) % n 
