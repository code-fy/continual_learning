"""
给你两个单链表的头节点 headA 和 headB ，
请你找出并返回两个单链表相交的起始节点。
如果两个链表没有交点，返回 null 。
"""

def get_intersection_node(heada,headb):
    """
    
    :return:   
    """"""
    根据快慢法则，走的快的一定会追上走得慢的。
    在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

    那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
    位置相遇
    """

    if heada is None or headb is None:
        return None

    cura,curb = heada,headb

    while (cura != curb):

        cura = cura.next if cura else headb

        curb = curb.next if curb else heada

    return cura









