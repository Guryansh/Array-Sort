import time
import random

i=0
arr=[]

while i<=1000:
    arr.append(random.randint(1, 1000))
    i+=1

def selection(arr):
    start = time.time()

    j=0
    while j<=1000:
        k=j+1
        while k<=1000:
            if arr[k]<arr[j]:
                temp=arr[k]
                arr[k]=arr[j]
                arr[j]=temp
            k+=1
        j+=1

    end = time.time()
    elapsed = (end - start)* 10**3
    print("Selection Sort: %.10f milliseconds" % elapsed)

def insertion(arr):
    start = time.time()

    j = 1
    while(j<=1000):
        k=j-1
        while(k>0):
            if arr[j]<arr[k]:
                temp = arr[k]
                arr[k] = arr[j]
                arr[j] = temp
            k-=1
        j+=1
    end = time.time()
    elapsed = (end - start) * 10 ** 3
    print("Insertion Sort: %.10f milliseconds" % elapsed)



def bubble(arr):
    start = time.time()
    i=0
    while i<=1000:
        j=0
        while j<=1000-i:
            k=j+1
            if(k==1001):
                break
            if arr[k] < arr[j]:
                temp = arr[k]
                arr[k] = arr[j]
                arr[j] = temp
            j+=1
        i+=1
    end = time.time()
    elapsed = (end - start) * 10 ** 3
    print("Bubble Sort: %.10f milliseconds" % elapsed)

print(arr)
a=arr.copy()
b=arr.copy()
c=arr.copy()


selection(a)
insertion(b)
bubble(c)