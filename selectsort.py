# encoding: utf-8
def selectSort(relist):
    for i in range(len(relist)):
        for j in range(len(relist)-i):
            if relist[i] > relist[i+j]:
                relist[i],relist[i+j] = relist[i+j],relist[i]
    return relist

print(selectSort([56,12,80,91,20]))