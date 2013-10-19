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

def encode(n, s):
  if len(n[1]) > 1:
    if db: print n[1], "and", (n[1])[0]
    
    if len((n[1])[0]) > 1: 
      #child's left child is a tree
      if db: print s	
      encode(((n[1])[0]), s + '0')
    if len((n[1])[1]) > 1:
      if db: print s
      #child's right child is a tree
      encode(((n[1])[1]), s + '1')
    else:
      #child's right child is a letter
      if db: print "code[", (n[1])[1], "] =",s
      hc[(n[1])[1]] = s
  else:
	#node's vale is a letter is this unreachable?
	hc[n[1]] = s
  return


def huff(l):
  ht = exPQ.buildHeap(l)
  if db: print "heap:", ht
  if db: print "list:", l
  while exPQ.hLen(ht) > 1:
    t1,ht = exPQ.heapExtractMin(ht)
    t2,ht = exPQ.heapExtractMin(ht)
    if db: print "extract: ", t1
    if db: print "extract: ", t2
    if db: print "heap: ", ht

    t = ( (t1[0] + t2[0]) , (t1, t2) )
  
    ht = exPQ.heapInsert(ht, t) 
    if db: print "added: ", t
    if db: print "heap: ", ht 
  if db: print ht[1]
  encode(ht[1], " ")

if __name__ == "__main__":
  ll = read(sys.argv[1])
  db = len(sys.argv)>2
  hc = dict()
  if db:
    print ll
  ll.insert(0, (0,0))	#push a blank tuple so we have a heap array
  huff(ll)
  print "huff: ", hc 
