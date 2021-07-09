'''
Sofia Medina - Algorithm Investigation Summer 2021
Euclidean Algorithmic: Optimized GCD

Created July 9 2021
'''

def euclideanAlgorithm(b,r):

    if r == 0: #gcd(n,0) = n
        return b

    b, r =  r, b%r #gcd(a,b) = gcd(b,r) = gcd(b, a mod b)
    
    return euclideanAlgorithm(b,r) #recursion


### Explanation of Algorithm ###
'''
Properties of the GCD of two numbers:

    1) gcd(n,0) = n
    2) gcd(a,b) = gcd(b,r);
        where r = a - a//b or a = bq + r

    1*) the greatest common denominator of a number and 0 is just the number

    2*) A number can be expressed as a multiplication + a remainder; a = bq +r
          The greatest common denominator of two numbers a and b is equal to the
          greatest common denominator of b and the remainder r of the divison a/b

          *Note that this can be expressed in several ways:
              #gcd(a,b) = gcd(b, remainder a/b) = gcd(b,r) = gcd(b, a mod b)

              w/ gcd(a,b) = gcd(b, a mod b) being used in the algorithm above


    The algorithm works recursively shrinking the two numbers into equivalent gcd forms
    using the 2nd property gcd(a,b) = gcd(b,r) until it reaches an equivalent gcd form
    where the remainder is zero gcd(n,0) in which case an answer has been reached and it
    returns "n"


    Fully numerical visualization:
        gcd(114, 96)
            114//96 =1, r = 114 - 96*1 = 18
            114 = 96*1 + 18
        gcd(96, 18)
            96//18 = 5, r = 96 - 18*5 = 6
            96 = 18*5 + 6
        gcd(18,6)
            18//6 = 3, r = 18 - 6*3 = 0
            18 = 6*3 + 0
        gcd(6,0)

        The gcd of 114 and 96 = 6!

'''

print(euclideanAlgorithm(96,3)) #gcd(96,3) = 3
print(euclideanAlgorithm(114,96)) #gcd(114,96) = 6
print(euclideanAlgorithm(50,0)) #gcd(50,0) = 50
