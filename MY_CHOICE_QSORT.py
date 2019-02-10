'''
@author Rishab Katta

Python Program for Quicksort with early exit for sorted subfiles (Qsorte).

Based on Research Paper: R.L. Wainwright, A Class of Sorting Algorithms based on Quicksort, Communications of the ACM, Vol. 28, No.
4, April 1985, pgs. 396-402.
'''

import random
import time

alist =[]

def qsorte(low, high, pivot_loc):

    if low<high:
        pivot= alist[pivot_loc]
        i= low-1
        j=high+1
        flag=True
        leftsorted=True
        rightsorted=True

        while(flag):
            i=i+1
            if i>=len(alist):
                break
            while alist[i] < pivot:
                if leftsorted:
                    if i>low:
                        if alist[i]<alist[i-1]:
                            leftsorted =False
                i=i+1
            j=j-1
            if j<0:
                break
            while (alist[j] >=pivot and j>=low):
                if rightsorted:
                    if j<high:
                        if alist[j]>alist[j+1]:
                            rightsorted = False
                j=j-1
            if i<j:
                alist[i], alist[j] = alist[j], alist[i]
                if i==pivot_loc:
                    pivot_loc=j
                if leftsorted:
                    if i>low:
                        if alist[i] < alist[i-1]:
                            leftsorted =False

                if rightsorted:
                    if j<high:
                        if alist[j]> alist[j+1]:
                            rightsorted =False
            else:
                flag=False

        if not rightsorted:
            if i >= 0 and i < len(alist):
                alist[i], alist[pivot_loc] = alist[pivot_loc], alist[i]
                i=i+1

        if not leftsorted:
            size= j-low+1
            if size>2:
                if j<len(alist) and j>=0:
                    qsorte(low,j, (low+j)//2)
            elif size==2:
                if alist[low]>alist[low+1]:
                    alist[low], alist[low+1]= alist[low+1], alist[low]

        if not rightsorted:
            size= high-i+1
            if size>2:
                if i>=0 and i<len(alist):
                    qsorte(i,high, (i+high)//2)
            elif size==2:
                if alist[high]<alist[high-1]:
                    alist[high], alist[high-1] = alist[high-1], alist[high]



def main():
    global alist
    alist= random.sample(range(10), 10)
    # k= [7,6,9,4,2,1,8,3,5]
    print(alist)
    qsorte(0, len(alist)-1, (0 + (len(alist)-1))//2)
    print(alist)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
