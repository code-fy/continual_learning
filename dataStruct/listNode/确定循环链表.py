# 题意： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

class LinkNode(object):
    def __init__(self,next = None,val=0):
        self.next = next
        self.val = val



def method(head):

    slow = head
    fast = head

    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next

        if(slow == fast):

            q = head
            p = slow

            while(p != q):
                p = p.next
                q = q.next

            return p

    return None


