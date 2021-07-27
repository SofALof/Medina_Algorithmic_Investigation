'''
Sofia Medina - Algorithmic Investigation Summer 2021
Extended Euclidean Algorithm AND Modular Multiplicative Inverse

Created: July 27 2021
'''


####NOTICE...FOR RIGHT NOW IM GOING TO WRIET THIS ONE _ GOING TO WORRY BOUT THE UNDERSTANDING
#BIT...NOT RN


#oficcially v confused on how im even going to do this w/o understanding

#LOL THIS IS GOING TO BE #STOLEN#


'''
return (g,x,y) such that a*x + b*y = gcd(a,b)
'''
####b =TOTIENT, r (a) = EXPONENT E
def extendedEuclideanAlgorithm(a,b):
    if a == 0: #gcd(n,0) = n
        return (b,0,1) #this will only happen if the numbers ARE NOT COPRIME!
                                #which by design SHOULD NOT BE THE CASE


    g,y,x = extendedEuclideanAlgorithm(b%a, a) #YEAH...NO CLUE
    return (g, x - (b//a)*y, y)


##through the EEA, totient "b" has been passed on
## a (r) = exponent e
## m  =PHI! (totient)
'''
return x such that (x*a) % b ==1
'''
def modularMultiplicativeInverse(a,m):
    g, x, y = extendedEuclideanAlgorithm(a,m)

    if g != 1:
        raise Exception ("Modular inverse does not exist")

    return x % m

