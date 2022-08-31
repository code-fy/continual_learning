"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1: 输入: haystack = "hello", needle = "ll" 输出: 2

示例 2: 输入: haystack = "aaaaa", needle = "bba" 输出: -1

说明: 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

"""

def str_str(s,t):
    if len(s) == 0 or len(t) >len(s):
        return 0
    slow = 0
    fast = len(t)

    while fast <= len(s) -1:
        if s[slow:fast] == t:
            return slow


        slow += 1
        fast += 1

    return 0


print(str_str("hello", "ll"))
"""
kmp 解题
"""
def get_next(next,s):

    j=0
    next[0] =0
    for i in range(1,len(s)):

        while(j >0 and s[i] != s[j]):
            j = next[j-1]

        if s[i] == s[j]:
            j +=1

        next[i] = j

    return next


def kmp_str(s,t):
    next = [0] * len(t)
    next = get_next(next,t)
    j = 0

    # 情况一 模式串与文本串 不匹配，且j>0 退回next数组下标
    for i in range(len(s)):
        while(j >0 and s[i] != t[j]):
            j = next[j-1]

        if s[i] == t[j]:
            j +=1

        if j == (len(t)):
            return i - len(t) +1

print(kmp_str("hello", "ll"))









