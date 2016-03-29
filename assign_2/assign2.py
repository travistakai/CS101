#import packages
import numpy as np;
from math import sqrt
import timeit
import matplotlib.pyplot as plt

def makeMatrice(N): #creates the correct matrice form for you.  Just create the peramater
    n = int(sqrt(N.size));  #to be a linear array reading left to right then down a line
    k = 0;
    s=(n,n);
    A = np.zeros(s);
    for i in range(0,n):
        for j in range(0,n):
            A[i][j] = N[k];
            k += 1;
    return A;
    
    
#***************************************************
#
#Problem_1
#
#***************************************************
    
def matmult(A,x): 
    answer = np.zeros(x.size);   #sets an empty array size of the product of A*x
    for i in range (0,x.size):
       answer[i] = doTheMath(A[i],x);   #calls method that neatly does the math and returns it
    return answer;

def doTheMath(B,i):    #does the math of multiply the row by the column
    sum = 0
    for j in range(0,i.size):
        sum = sum + (B[j] * i[j])
    return sum;

    #Test arrays for Problem 1
    #D = makeMatrice(np.array([1,2,3,4]));
    #E = np.array([1,2]);
    #print(matmult(D,E))


#*****************************************************
#
#Problem 2
#
#****************************************************


def hadmat(k):
    if(k<0):   #checks that k is a greater value than 0
        print("Please enter a 'k' > 0");
        return;
    a = np.array([[1]]);  #sets the base case of k == 1
    n = pow(2,k);
    C = np.array(concat(a,n));      #calls the recursive function that will concatanate the base case to the correct size
    return C

def concat(a,n):
    if(a.size != pow(n,2)):   #recursive condition
       b = np.concatenate((a,a), axis = 1);
       c = np.concatenate((a,a*-1), axis = 1);
       d = np.concatenate((b,c), axis = 0);  
       a = concat(d,n);           #recursive call
    if (a.size == pow(n,2)): 
        return a
    
    #examples function call for problem 2
    #print(hadmat(2)) adjust parameter for k



#***************************************************
#
#Problem 4
#
#***************************************************
def hadmatmult(H, x):
    n = int(sqrt(H.size)/2);
    #k = int(x.size/2)
    if(H.size!=4):  
      hadmatmult(H[0:n,0:n],x[0:n]);
    v1 = np.zeros(x.size);  
    for i in range(0,x.size):
       v1[i]=doTheMath(H[i],x); #method from problem 1
    return v1;
    
    #examples for problem 4
    #v = np.array([1,2,3,4]);
    #C = (hadmat(2))
    #print(hadmatmult(C,v))

total = 0
 
total = 0
array1 = np.zeros(12)
for i in range(1,12):
    H = hadmat(i);
    r = np.random.rand((pow(2,i)),1);
    a = timeit.Timer(lambda: matmult(H, r));
    array1[i-1] = a.timeit(number = 1);

total = 0
array2 = np.zeros(12)
for i in range(1,12):
    H = hadmat(i);
    r = np.random.rand((pow(2,i)),1);
    a = timeit.Timer(lambda: hadmatmult(H, r));
    array2[i-1] = a.timeit(number = 1);
    
    
plt.plot(array1,color = 'red',array2,color = 'blue');
 
plt.show()
