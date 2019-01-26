import random
from time import process_time
#import time

alist =random.sample(range(1000000), 10)
#print("Pre Any Sorting",alist)
print(len(alist))
def is_sorted(l):
    return all(a <= b for a, b in zip(l[:-1], l[1:]))
tslist=alist[:]
print("Pre Tanaka Sort: ",is_sorted(tslist))

def tanakaSort(tslist):
    sortlist=[]
    counter=0
    while tslist:
        #print(tslist,sortlist)
        while counter in tslist:
                tslist.remove(counter)
                sortlist.append(counter)

        counter+=1
    return sortlist
#sslist=alist[:]
startTime = process_time()
sortlist=tanakaSort(tslist)
print("Tanaka Sort Time: ",(process_time() - startTime), "Seconds")
#print(sortlist)
print("Post Tanaka Sort: ",is_sorted(tslist))
