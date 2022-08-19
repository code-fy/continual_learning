"""
编写一个函数，其作用是将输入的字符串反转过来。
输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，
你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

"""

def resver_str(s):
    return s[::-1]

def resver_s(s):
    i = 0
    j = len(s)-1
    if len(s) % 2 ==0:
        while i <=j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
    else:
        while i+1<=j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1

    return s

print(resver_s(["q","w","e","r","q"]))