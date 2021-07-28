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
    #C =  [(ord(char)**e)% n for char in plain_text]

    return (M**e) % n

# C = ciphertext message (encrypted message, as per convention)
# d = decryption exponent d
# n = totient value

def decrypt(C, d, n):
   # M =[chr((char**d)%n) for char in cipher_text]
    #M =  ''.join(M)

    return (C**d) % n 
