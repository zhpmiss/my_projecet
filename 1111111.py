list1=[21,434,5,6,54,6,57,658,78,678,67,867,9765,4,46]
l =len(list1)
while l>0:
    for i in range(l-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
    l-=1
print(list1)
