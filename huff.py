#! /usr/bin/python
import sys
import exPQ

def read(fnm):
  f = open(fnm)
  ll = []
  for line in f:
    l = line.strip().split(" ")
    for t in l:
      freq,val  = t.split(",")
      ll.append((int(freq),val))
  return ll

def huff(l):
  hc = {}

  exPQ.buildHeap(l)
  if db: print l
  while exPQ.hLen(l) > 1:
    t1,l = exPQ.heapExtractMin(l)
    t2,l = exPQ.heapExtractMin(l)
    #if db: print l

    ht = ( (t1[0] + t2[0]) , (t1, t2) )
  
    l = exPQ.heapInsert(l, ht) 
    if db: print l

  ht = exPQ.heapExtractMin(l);

  

  print "huff: ", hc 

if __name__ == "__main__":
  ll = read(sys.argv[1])
  db = len(sys.argv)>2
  if db:
    print ll
  ll.insert(0, (0,0))
  huff(ll)
