__author__ = 'Parikshit'

import time
import random
from igraph import *
from random import randint
start_time=time.clock()
##print start_time


#fileName = 'facebook_combined.adj'
#fileName = 'wiki.adj'
#fileName = 'synthetic.adj'
#fileName = 'karate.adj'
#fileName = 'coll.adj'
#fileName = 'gnutella08.adj'
#fileName = 'slash.adj'
fileName = 'web-Google.adj'

graphlist=[]
tempmap={}
graphmap={}

with open(fileName) as f:
    content = f.read().splitlines()
#print "content=",content


for line in content:
    graphlist.append(line.rstrip())
#print "graphlist=",graphlist

#print "graphlist[0]=",graphlist[0]
#print "graphlist[0][1]=",graphlist[0][1]


newf=open("new_rand_rev_"+str(fileName), 'w')



for item in graphlist:
    itemlist=item.split()
    #print "itemlist=",itemlist
    #print "itemlist[0]=",itemlist[0],"itemlist[1]=",itemlist[1]
    if len(itemlist)==2:
		randstr=str(randint(1,100))
		newf.write(str(itemlist[0])+" "+str(itemlist[0])+" "+str(itemlist[1])+" "+randstr+"\n")  
		#FromNode FromNodename ToNode RandomEdgeWeight
		newf.write(str(itemlist[1])+" "+str(itemlist[1])+"\n")  
		#ToNode ToNodename FromNode RandomEdgeWeight
		#newf.write("\n")
    else:
        print "List of length",len(itemlist),"detected:",itemlist

newf.close()