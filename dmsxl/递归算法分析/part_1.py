
"""
5 :5 4 3 2 1 = 15
"""

def fibonacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(5))


def binary_search(arr,n,l,r):
    arr = sorted(arr)

    if l<= r:
        mid = l+(r-l) // 2
        if n > arr[mid]:
            l= mid
            return binary_search(arr,n,mid+1,r)
        if n < arr[mid]:
            r = mid
            return binary_search(arr, n,l,mid-1)
        if n == arr[mid]:
            return mid
    return -1

# print(binary_search([5,6,7,8,10],10,0,5))

def binary_search_1(arr,n,l,r):
    while l<r:
        mid = l+(r-l) // 2
        if arr[mid] > n:
            r = mid
        if arr[mid] < n:
            l = mid
        if arr[mid] == n:
            return mid
    return -1

# print(binary_search_1([5,6,7,8,10],10,0,5))
print("ok")
