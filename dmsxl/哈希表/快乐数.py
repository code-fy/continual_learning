"""
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。
"""



def is_happy(n):

    # def get_sum(n):
    #     sum = 0
    #     sum += (n % 10) * (n % 10)
    #     n /= 10
    #     return sum
    def get_sum(num):
        sum_ = 0

        while num:
            sum_ += (num %10) ** 2
            num = num // 10
        return sum_

    res = set()
    while True:
        sum = get_sum(n)
        if sum == 1:
            return True

        if sum in res:
            return False
        else:
            res.add(sum)

        n = sum



print(is_happy(9))