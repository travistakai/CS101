import numpy as np
import timeit
import matplotlib.pyplot as plt


#insertion 
def insertion(A):
   size = A.size
   swap = 0;index = 0
   for i in range(1, size):
      index = i
      while A[index] < A[index-1] and index > 0:
         swap = A[index-1]
         A[index-1] = A[index]
         A[index] = swap
         index-=1


#mergeSort
def mergeSort(A, p, r): 
      if(p < r):
         #recursivley breaks apart the array
         q = int((p+r)/2)
         mergeSort(A, p, q)
         mergeSort(A, q+1, r)
         merge(A, p, q, r)

#merges the array back together
def merge(A, p, q, r):
   n1 = q-p+1
   n2 = r-q
   L = np.zeros(n1)
   R = np.zeros(n2)
   i = 0
   j = 0
   k = 0
   while i < n1:
      L[i] = A[p+i]
      i = i + 1
   while j < n2:
      R[j] = A[q+j+1]
      j = j + 1
   i = 0
   j = 0
   k = p
   while k <= r:
      if( i<n1 and j<n2 ):
         if( L[i]<=R[j] ):
            A[k] = L[i]
            i = i + 1
         else:
            A[k] = R[j]
            j = j + 1
      elif( i<n1 ):
         A[k] = L[i]
         i = i + 1
      else:
         A[k] = R[j]
         j = j + 1
      k = k + 1



def worstCase(n):
   Z = np.zeros(n)
   x = n;j = 0    
   while x > 0:
      Z[j] = x
      j+=1
      x-=1
   return Z

def bestCase(n):
    T = np.zeros(n)
    for i in range(0,n):
       T[i] = i
    return T
 
def worstCaseFcn(n):
    A = np.zeros(n)
    x = 0
    j = A.size/2
    i = 0
    while i < A.size:
       A[x]=i
       i=i+1
       x+=1
       A[j]=i
       i=i+1
       j+=1
    return A        

def bestCaseFcn(n):
    T = np.zeros(n)
    for i in range(0,n):
       T[i] = i
    return T   

#average cases
countTwo = 200

def randomize(n,j):
    np.random.seed(4)
    D = np.array(np.random.random_integers(0,j,n))
    return D
    
def permutationShuffleMerg(A):
   totalMergTime = 0
   for i in range(1,1000):
       D = np.array(np.random.permutation(A))
       a = timeit.Timer(lambda: mergeSort(D,0,D.size-1))
       totalMergTime = totalMergTime + a.timeit(number = 1)
       print(totalMergTime)
   return (totalMergTime/1000)
       
       
def permutationShuffleIn(A):
    totalInTime = 0
    for i in range(1,1000):
       D = np.array(np.random.permutation(A))
       b = timeit.Timer(lambda: insertion(D))
       totalInTime = totalInTime + b.timeit(number = 1)
       print(totalInTime)
    return (totalInTime/1000)
       
       
avgMerg = np.zeros(countTwo)
avgIn = np.zeros(countTwo)
for n in range(0,countTwo):
    randomArray = randomize(n,countTwo)
    avgMerg[n] = permutationShuffleMerg(randomArray)
    avgIn[n] = permutationShuffleIn(randomArray)
    
    

plt.plot(avgIn)
plt.title("Insertion Sort Average")
plt.draw()


plt.figure()
plt.plot(avgMerg)
plt.title("MergeSort Average")
plt.draw()

plt.show()
    





