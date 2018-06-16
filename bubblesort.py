def bubbleSort(relist):
    for i in range(len(relist)):
        for j in range(len(relist)-i-1):
            if relist[j] > relist[j+1]:
                relist[j+1], relist[j] = relist[j], relist[j+1]
    return relist

print(bubbleSort([9,3,1,4,2,7,8,6,5]))