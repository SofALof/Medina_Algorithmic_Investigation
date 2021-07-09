'''
Sofia Medina - Algorithmic Investigation Summer 2021
Euler's Totient Function - for RSA

Created July 9 2021
'''

def EulersTotient(p,q):
    return (p-1)(q-1)

### Explanation of Algorithm ###
'''
Euler's totient function; sometimes called phi(n)

 - Counts all the numbers (1-n) that are relatively prime to some number n

It's important to note that phi(p) where p is some prime number is just equal to p-1
(bc a prime number is relatively prime to all numbers less than itself)

ALSO: Euler's totient function is multiplicative function:
    phi(mn) = phi(m)*phi(n)

'''
