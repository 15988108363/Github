"""冒泡排序"""
list01 =[1,21,23,34,15,62,7,8,9,0,12,12,112,12,1,23,454,23,1,1232,313,231,23,123,123,21,2,3,12,31,23,21,31,23,12,3,\
         231,1231,23,123,23,2,31,23,1,23,12,31,23,12,3,123,2,31,3,123,12,3,123,1,3,21,2,3,12,3,1,31,3]
def bubble_sort(target): #n^2时间复杂度
    for i in range(len(target)-1):
        for k in range(len(target)-i-1):
            if target[k] >= target[k+1]:
                target[k],target[k+1] = target[k+1],target[k]
list02 =[1,21,23,34,15,62,7,8,9,0,12,12,112,12,1,23,454,23,1,1232,313,231,23,123,123,21,2,3,12,31,23,21,31,23,12,3,\
         231,1231,23,123,23,2,31,23,1,23,12,31,23,12,3,123,2,31,3,123,12,3,123,1,3,21,2,3,12,3,1,31,3]
def choose_sort(target): #n^2时间复杂度
    for i in range(len(target)-1):
        min = i
        for j in range(i+1,len(target)):
            if target[min] > target[j]:
                min = j
        if i != min:
            target[i],target[min] = target[min],target[i]
list03 =[1,21,23,34,15,62,7,8,9,0,12,12,112,12,1,23,454,23,1,1232,313,231,23,123,123,21,2,3,12,31,23,21,31,23,12,3,\
         231,1231,23,123,23,2,31,23,1,23,12,31,23,12,3,123,2,31,3,123,12,3,123,1,3,21,2,3,12,3,1,31,3]
def insert_sort(targrt):#1/2*n^2时间复杂度
    for i in range(1,len(targrt)):
        min= targrt[i]
        j = i
        while j >0 and targrt[j-1] >min:
            targrt[j]= targrt[j-1]
            j -=1
        targrt[j]=min

list04 =[1,21,23,34,15,62,7,8,9,0,12,12,112,12,1,23,454,23,1,1232,313,231,23,123,123,21,2,3,12,31,23,21,31,23,12,3,\
         231,1231,23,123,23,2,31,23,1,23,12,31,23,12,3,123,2,31,3,123,12,3,123,1,3,21,2,3,12,3,1,31,3]
def sub_sort(low,high,list):
    key = list[low]
    while low < high:
        while low<high and list[high]>= key:
            high -=1
        list[low]=list[high]
        while low < high and list[high] < key:
            low +=1
        list[high] = list[low]
    list[low]=key
    return low

def quick(low,high,list):
    if low < high:
        key = sub_sort(low,high,list)
        quick(low,key -1,list)
        quick(key+1,high,list)

def quicksort(list,p,r):
    if p<r:
        q=partion(list,p,r)
        quicksort(list,p,q)
        quicksort(list,q+1,r)
def partion(list,p,r):
    i=p-1
    for j in range(p,r):
        if list[j]<=list[r]:
            i+=1
            list[i],list[j]=list[j],list[i]
    list[i+1],list[r]=list[r],list[i+1]
	return i

bubble_sort(list01)
print(list01)
choose_sort(list02)
print(list02)
insert_sort(list03)
print(list03)
quick(0,len(list04)-1,list04)
print(list04)
quicksort(list04,0,len(list04)-1)
print(list04)