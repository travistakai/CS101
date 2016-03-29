import numpy as np
import timeit


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


print("Label: Insertion sort")
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
    
    
    
count = 1000    
    
    
#Time Arrays Insertion
timeArrayBestIn = np.zeros(count)
xAxisArrayBestIn = np.zeros(count)
for n in range(1,count):
    A = bestCase(n)
    xAxisArrayBestIn[n] = n
    a = timeit.Timer(lambda: insertion(A))
    timeArrayBestIn[n] = a.timeit(number = 1)
    
   
timeArrayWorstIn = np.zeros(count) 
xAxisArrayWorstIn = np.zeros(count)   
for j in range (1,count):
    B = worstCase(j)
    xAxisArrayWorstIn[n] = n
    b = timeit.Timer(lambda: insertion(B))
    timeArrayWorstIn[j] = b.timeit(number = 1)
   
print(timeArrayBestIn)
print(timeArrayWorstIn)

print("Label: MergeSort")
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


#Time Arrays
timeArrayBestMer = np.zeros(count)
xAxisArrayBestMer = np.zeros(count)
for n in range(1,count):
    A = bestCaseFcn(n)
    xAxisArrayBestMer[n] = n
    a = timeit.Timer(lambda: mergeSort(A,0,A.size-1))
    timeArrayBestMer[n] = a.timeit(number = 1)
    
   
timeArrayWorstMer = np.zeros(count)
xAxisArrayWorstMer = np.zeros(count)    
for j in range (1,count):
    B = worstCaseFcn(j)
    xAxisArrayWorstMer[n] = n
    b = timeit.Timer(lambda: mergeSort(B,0,B.size - 1))
    timeArrayWorstMer[j] = b.timeit(number = 1)
   
    
    
print(timeArrayBestMer)
print(timeArrayWorstMer)
