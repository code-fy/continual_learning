"""
数组排序
"""

# 冒泡排序

def bubbleSort(l):
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l

print(bubbleSort([2,1,4,3,9,7,8]))

def bubbleSort1(l):
    tmp = True
    for i in range(len(l)):
        if not tmp:
            tmp = False
            break
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1],l[j]
                tmp = True

    return l
print(bubbleSort1([5,6,2,3,9]))




