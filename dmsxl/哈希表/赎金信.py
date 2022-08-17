"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，
返回 true ；否则返回 false。
"""

def can_construct(s,c):
    res1 = {}
    res2 = {}

    for i in s:
        if i in res1:
            res1[i] += 1
        else:
            res1[i] = 1

    for j in c:
        if j in res2:
            res2[j] += 1
        else:
            res2[j] =1

    for k,v in res1.items():
        if k in res2 and res1[k] <= res2[k]:
            return True
        else:
            return False


print(can_construct("aa","aab"))