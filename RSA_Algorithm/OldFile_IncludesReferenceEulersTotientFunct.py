#Modular Congruence - Properties Check


a = 3

b = 15

c = b + 12 

n = 12

print()
print("Modular Congruence Properties")

print("----------------------------------------------------------------------")

print("Reflexivity:  a mod n = a mod n ")
print (a, "mod", n, ":", a % n)

print()

print("Symmetry: a = b (mod n) --- if b = a (mod n)")

print(a, "mod", n, "=", a % n)
print(b, "mod", n, "=", b % n)

print()

print("Transitivity: a = c (mod n) --- if a = b (mod n) and b = c (mod n)")

print(a, "mod", n, "=", a % n)
print(b, "mod", n, "=", b % n)
print(c, "mod", n, "=", c % n)

print("----------------------------------------------------------------------")

a1 = 5
b1 = 17

a2 = 9
b2 = 12+9

k = 76

print("GIVEN:")
print("   a = b (mod n)")


print()
print("~~~ a + k = b + k (mod n) ~~~")
print(a, "+", k, "mod", n, "=", (a+k) % n)
print(b, "+", k, "mod", n,"=", (b+k) % n)

print()
print("~~~ a*k = b*k (mod n) ~~~")
print(a,"*", k, "mod", n, "=", (k*a) % n)
print(b, "*", k, "mod", n, "=", (k*b) % n)

print()
print("~~~ a^k = b^k (mod n) ~~~")
print(a,"^", k, "mod", n, "=", (a**k) % n)
print(b, "^", k, "mod", n, "=", (b**k) % n)

print()
print("For some Polynomial p(x):")
print("~~~ p(a) = p(b) (mod n) ~~~")
print("p(x) = x^2 + 5x -1")
pA = a**2 + a*(5) -1
pB = b**2 + b*(5) -1
print("p("+ str(a)+") =", pA, "|", "p("+ str(b)+") =", pB)
print()
print(pA, "mod", n, "=", pA % n)
print(pB, "mod", n, "=", pB % n)
print("----------------------------------")
print("GIVENS:")
print("   a1=b1 (mod n)")
print("   a2=b2 (mod n)")


print()
print("~~~ a1 + a2 = b1 + b2 (mod n) ~~~")
print(a1,"+", a2, "mod", n, "=", (a1+a2) % n)
print(b1, "+", b2, "mod", n, "=", (b1+b2) % n)

print()
print("~~~ a1 - a2 = b1 - b2 (mod n) ~~~")
print(a1,"-", a2, "mod", n, "=", (a1-a2) % n)
print(b1, "-", b2, "mod", n, "=", (b1-b2) % n)

print()
print("~~~ a1 * a2 = b1 * b2 (mod n) ~~~")
print(a1,"*", a2, "mod", n, "=", (a1*a2) % n)
print(b1, "*", b2, "mod", n, "=", (b1*b2) % n)

print("----------------------------------------------------------------------")

print("given: a= b (mod n")
print("   k^a = k^b (mod n) <-- is generally false")
print()
print("[BUT there is an exception using EULERS TOTIENT FUNCTION]")
print()
print("Eulers totient function (phi): Counts all the numbers (1-n) that are \
relatively prime to some number n")
print()
print("It is interesting to note that the phi(p) where p is some prime number \
is just equal to p-1")
print()
print("Eulerts totient function is also a multiplicative function: \
phi(mn) = phi(m)*phi(n)")
print()
print("----------------------------------------------------------------------")
print("given a = b (mod (phi(n) )")
print("   k^a = k^b (mod n) -- k MUST b coprime w/ n ")
print("ex")

n = 9
phiN = 6 #1,2,4,5,7,8

print("let n = 9; and let it be known that phi(n) = 6")
print("let a = 3 and b = 9")
print()
print(a, "mod", phiN, "=", a % phiN, "<-- a mod phiN")
print(b, "mod", phiN, "=", b % phiN, "<-- b mod phiN")
print("\nand know k^a = k^n (mod n); let k = 16 as it is coprime to n = 9")
k = 16
print()
print(k, "^", a, "mod", n, "=", (k**a) % n, "<-- k^a mod n")
print(k, "^", b, "mod", n, "=", (k**b) % n, "<-- k^b mod n")

