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

# print(bubbleSort([2,1,4,3,9,7,8]))

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
# print(bubbleSort1([5,6,2,3,9]))

"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
输入: [10,2]
输出: "102"

输入: [3,30,34,5,9]
输出: "3033459"
"""

def searchMin(l):
    l = [str(x) for x in l]
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if int(l[j].join(l[j+1]))> int(l[j+1].join(l[j])):
                l[j],l[j+1] = l[j+1],l[j]

    return "".join(l)
    

print(searchMin([3,30,34,5,9]))




