'''
Sofia Medina - Algorithmic Investigation Summer 2021
Carmicheal's Totient Function - for RSA

Created July 20 2021
'''

from Euclidean_Algorithm import euclideanAlgorithm as eucldAlg

#p and q must be prime
def CarmichealsTotient(p,q):

    return  (abs( (p-1)*(q-1) ) )/ (eucldAlg(p-1,q-1) )


print(CarmichealsTotient(1,5))
