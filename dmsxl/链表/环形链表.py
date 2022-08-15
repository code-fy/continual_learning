"""
题意： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
"""


def detectCycle(l):
    # 判断链表是否有环
    fast, slow = l,l
    while(fast,fast.next):
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            index1 = fast
            # 如果有环，环的index
            """
            设slow 移动为x+y步
            fast 移动为x+y+n(y+z)
            2(x+y) =  x+y+n(y+z)
            x +y = n(y+z)
            x = n(y+z) - y
            x = (n-1)(y+z)+z 
            maybe n>= 1
            if n =1
            x = z
            """
            index2 = l
            while(index1 != index2):
                index1 = index1.next
                index2 = index2.next

            return index1
        return None







