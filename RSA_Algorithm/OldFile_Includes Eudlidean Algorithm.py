'''
Sofia Medina
Duplicated from my files: July 5 2021

Currently have no idea how this works...going to keep it as a "base/foundation"
'''

#################################
#Modular Multiplicative Inverse
import math

print("3 mod 12 = ", 3%12)
print()

print("3x mod 12 = 1")
print("x = modular multiplactive inverse")
print()

#this part is made up by me take this very loosely
print("For form a mod m")
print("x is modular multiplicative inverse for any:")
print("   (m+1)k, where k is any positive integer")
print()

a = 3
m = 12

#print(3%12)


##########################################

#for gcd(a,b); if a is written in the form a = bq +r
    # gcd(a,b) = gcd(b,r)
    #!!gcd(0,n) = n!!

print("#################################################")
print( "gcd(393,495) =", math.gcd(393,495))
print("gcd(393,", str(495%393) +  ") =", math.gcd(393,495%393) )
print("~~~~~~~~~~~~~~~~~~~~")
print("495 = ", 495//393, "*", 393, "+", 495%393) 
print("gcd(393, 495) = gcd(393,", str(495%393) +  ")")
print("#################################################")



def euclideanAlg(r,b):
    if r == 0:
        return b
    r, b = b%r, r
    print("gcd("+ str(r)+",", str(b) + ")")
    return euclideanAlg(r,b)

print("euclidean algorithm \n-------------------")
b = euclideanAlg(39363636,493737373735)
print("gcd =", b)
print("#################################################")

##########################################
#def extendedEuclideanAlg(r,b):
        
    
    
