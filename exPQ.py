#! /usr/bin/python
import sys


#Nate Gillard (login: gnate)
#CS320 Bohm
#PA1 due 9/20/2013

# heaps here are 1 based, so read puts None in 0th element
def readNums(fnm):
   f = open(fnm)
   lst = [None]
   for line in f:
      l = line.strip().split(" ")
      for s in l:
        lst.append(int(s))
   return lst

# heaps here are 1 based
def parent(i): return i/2
def left(i): return 2*i
def right(i): return 2*i+1

# so for their length element 0 does not count
def hLen(A): return len(A)-1

def swap(A, j, k):
  temp=A[j]
  A[j]=A[k]
  A[k]=temp

def heapify(A, i, n): 
  """
  Build a Min Heap at i
  n is the number of elements in the heap
  A[i] is "almost a heap" (except root i), 
  Make A[i] a heap 
  """
  L = left(i)
  R = right(i)
  
  if L <= n and A[L] < A[i]:
    smallest = L
  else:
    smallest = i

  if R <= n and A[R] < A[smallest]:
	smallest = R

  if smallest != i:
    swap(A, i, smallest) 
    heapify(A,smallest, n)

  #print A


def buildHeap(A): 
# build a Min heap A from an unsorted array
  for k in range((hLen(A)/2), 0, -1):
    heapify(A, k, hLen(A))
  #heapify(A, 1, hLen(A))
  return A

def heapExtractMin(A):
  temp = A[1]
  swap(A, 1, hLen(A))
  del A[-1]
  heapify(A, 1, hLen(A))
  return temp,A

def heapInsert(A,v):
  A.append(v)
  i = hLen(A)  
  par = parent(i);
  while A[par] > v and par > 0:
    swap(A, par, i)
    i = par;
    par = parent(i)

  #swap(A, 1, hLen(A))
  #buildHeap(A) 
  #heapify(A, 1, hLen(A))
  return A

if __name__ == "__main__":
   db = len(sys.argv)>2
   A  = readNums(sys.argv[1])
   if db: print "Input:", A[1:]
   buildHeap(A)
   if db: print "Input:", A[1:]
   min,A = heapExtractMin(A)
   print "min", min
   A=heapInsert(A,0)
   min,A = heapExtractMin(A)
   print "min", min
   min,A = heapExtractMin(A)
   print "min", min 
   if db: print "Input:", A[1:]
   A=heapInsert(A,0)
   min,A = heapExtractMin(A)
   print "min", min
   min,A = heapExtractMin(A)
   print "min", min
   A=heapInsert(A,3)
   min,A = heapExtractMin(A)
   print "min", min
   
   if db: print "Input:", A[1:]
  
   



