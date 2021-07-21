'''
Sofia Medina - Algorithmic Investigation Summer 2021
Carmicheal's Totient Function - for RSA

Created July 20 2021
'''

from Euclidean_Algorithm import euclideanAlgorithm as eucldAlg


#p and q must be prime
def CarmichealsTotient(p,q):

    return  (abs( (p-1)*(q-1) ) )/ (eucldAlg(p-1,q-1) )



### Explanation of Algorithm ###
'''
Carmicheal's totient function; sometimes called lambda(n)

- The exact thing it does...I couldnt tell you right now

- (For RSA), serves as an optimization to Euler's totient function as it essentially
"reduces" the totient (while maintaining its modular properties)
making it a smaller number and thus making operations quicker

- Sometimes also referred to as the "reduced totient function" or the least universal
exponent function


lambda(n) = lambda(pq) = lcm (phi(p), phi(q) ) = lcm(p-1, q-1)
'''






#print(CarmichealsTotient(11,5))



