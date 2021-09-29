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
    

# print(searchMin([3,30,34,5,9]))

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""

def moveZero(l):
    zeroCount = 0
    for i in range(len(l)-zeroCount):
        if l[i] == 0:
            for j in range(i,len(l)-i-1):
                l[j] ,l[j+1] = l[j+1], l[j]

    return l

# print(moveZero([0,1,0,3,12]))


# 选择排序

"""
选择排序的思想是：双重循环遍历数组，每经过一轮比较，找到最小元素的下标，将其交换至首位。
"""
def selectionSort(l):
    minIndex = 0
    for i in range(0,len(l)):
        minIndex = i
        for j in range(i+1,len(l)):
            if l[minIndex] > l[j]:
                minIndex = j
                l[minIndex],l[i],  = l[i],l[minIndex]
        
    return l

# print(selectionSort([3,30,34,5,9]))

"""
数组中的第 K 个最大元素
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""

def TopK(l,k):
    min = 0
    for i in range(len(l)):
        min = i
        for j in range(i,len(l)):
            if l[min] > l[j]:
                min = j
        l[min], l[j] = l[j], l[min]
              
    return l[k+1]

# print(TopK([3,2,3,1,2,4,5,5,6],4))

def select_dort(l):
    length = len(l)
    for i in range(0,length):
        min = i
        for j in range(i+1, length):
            if l[j] < l[min]:
                min = j
        l[min],l[i] = l[i], l[min]

    return l

# print(select_dort([3,2,1,5,6,4]))





