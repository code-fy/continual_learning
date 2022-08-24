"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，
该函数将返回左旋转两位得到的结果"cdefgab"。
"""

def left_rev(s,k):
    if k > len(s):
        return

    tmp = s[:k]
    tmp1 = s[k:]
    res = tmp1 + tmp

    return "".join(res)


print(left_rev("abcdefg",2))

def resv(l):
    s = 0
    e = len(l) -1
    l = list(l)
    while s<=e:
        l[s],l[e] = l[e], l[s]
        s += 1
        e -= 1

    return l


def reverse_left_words(s,k):

    p = resv(s[:k])
    q = resv(s[k:])

    return "" .join(resv((p+q)))

print(reverse_left_words("abcdefg",2))
