"""
给定一个字符串，逐个翻转字符串中的每个单词。
"""

def resver_str(s):
    l= s.split(" ")
    tl = []
    for i,v in enumerate(l):
        if v == "" and l[i+1] == "":
            continue
        else:
            tl.append(v)
    s = 0
    e = len(tl) -1
    while s <= e :
        tl[s] ,tl[e] = tl[e],tl[s]
        s +=1
        e -=1
    # tl = list(map(str,tl))


    return " ".join(tl)




print(resver_str("blue      is sky the"))


