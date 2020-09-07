#shamir secret sharing scheme

#module import

from random import *
from math import *
from functools import reduce

########################################
#### FIRST PART, CREATION OF SHARES ####
########################################

#Function definition


#Check wether a number is prime
def isPrime(n):
    if n == 1 or n <=0:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def f(x,p):
    f = 0
    for i in range(0, degree ):
        f += coef[i]*(x**i)
    return f%p

def creaShare(i):
    return (i,f(i,P))

#Variables

S= int(input('What is your secret? '))
P= int(input('What prime number do you want to use? '))

#Making sure our number is prime
while not isPrime(P) or P < S:
    P= int(input('Please use a prime number larger than your secret '))

degree = int(input('How many shares are needed to unlock? '))

#Creation of the random polynomial
coef = [S]
for i in range (0, degree):
    coef += [randint(0,1000000)]


n = int(input('How many shares do you want to create? '))

#Making sure that the user creates enough shares
while n < degree + 1 :
    n = int(input('please use more than', degree,  'shares '))

#Creation of Shares


for i in range(1, n+1):
    print(creaShare(i))

###############################################################
#### SECOND PART, DETERMINING THE SECRET FROM GIVEN SHARES ####
###############################################################

k= degree

shareList = []

while len(shareList) < k:
    q = (input("What is your share? ")).split()
    for i in range(0,2):
        q[i] = int(q[i])
    shareList += [q]


#here we are going to compute modular inverses using Fermat's little theorem

def modInverse(a,p):
    return (a**(p-2))%p

# now we have input our shares, we iterpolate into a function
Secret=0

# extract each value of X
list=[]
X=[]
for i in range(k):
    list=[shareList[i][0]]
    X +=[list]
# now X is a list [[X1],[X2],...,[Xk]]

# Lagrange iterpolation
for j in range (k):
    A=reduce(lambda x,y: x+y, X) #A=[X1,X2,X3,...,Xk]
    B=int(A[j]) #B is the value of Xj+1 i.e.Xk
    A.remove(A[j]) #Delete Xj+1 from list A
    C=reduce(lambda x,y: x*y,A) # Calcualte the cumulative product of values in list A i.e.find X1*...*Xk/Xj+1 for each j
    D=[i-B for i in A] #Calcualte (Xm-Xj+1) m!=j+1
    E=reduce(lambda x,y: x*y,D) #Calcualte the cumulative prodcut of values in list D
    F=int(shareList[j][1])*C*modInverse(E,P) #Caulate Lagrange iterpolation
    Secret += F
print(int(Secret%P))
