# 链表的定义

class Node():

    def __init__(self,val,next=None):
        self.next = next
        self.val = val

class MyLink():

    def __init__(self):
        self.head = Node(0)
        self.count = 0

    def get(self,index):
        node = self.head
        if 0<=index<self.count:
            for _ in range(index +1):
                node = node.next
            return node.val
        else:
            return -1

    def add_at_head(self,val):
        self.add_at_index(0,val)

    def add_at_tail(self,val):
        self.add_at_index(self.count,val)

    def add_at_index(self,index,val):

        if index <0:
            index = 0
        elif index > self.count:
            return

        self.count += 1
        add_node = Node(val)
        prev_node, current_node = None, self.head
        for _ in range(index +1):

            prev_node, current_node = current_node, current_node.next

        else:
            prev_node.next, add_node.next = add_node, current_node

    def del_at_index(self,index):

        if 0 <= index < self.count:
            self.count -= 1
            prev_node, current_node = None, self.head

            for _ in range(index +1):
                prev_node, current_node = current_node, current_node.next

            else:
                prev_node.next,current_node.next = current_node.next, None

# 测试
def gen_link(n):
    link_node = MyLink()
    for i in range(n):
        link_node.add_at_index(i,i)
    return link_node

def cur():
    l = gen_link(5)
    while l:
        print(l.val)
        l = l.next

l = gen_link(9)
# print(l.get(4))


# 双链表
class Dnode():
    def __init__(self,val):
        self.prev = None
        self.next = None
        self.val = val

class MyDnode():

    def __init__(self):
        self.head,self.tail = Dnode(0), Dnode(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 0

    def get_node(self,index):
        if index < self.count // 2:
            node = self.tail
            for _ in range(self.count - index):
                node = node.prev

        else:
            node = self.head
            for _ in range(index + 1):
                node = node.next

        return node

    def get(self,index):
        if 0<= index < self.count:
            node = self.get_node(index)
            return node.val
        else:
            return -1

    def add_at_head(self,val):
        self._update(self.head,self.head.next,val)

    def add_at_tail(self,val):
        self._update(self.tail.prev,self.tail.val)

    def add_at_index(self,index,val):
        if index <0:
            index = 0
        elif index > self.count:
            return
        node = self.get_node(index)
        self._update(node.prev,node,val)

    def _update(self,prev,next,val):

        self.count += 1
        node = Dnode(val)

        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def del_at_index(self,index):

        if 0<= index <self.count:
            node = self.get_node(index)

            node.prev.next,node.next.prev = node.next,node.prev


# 测试
def gen_dlink(n):
    mdlink = MyDnode()
    for i in range(n):
        mdlink.add_at_index(i,i)
    return mdlink

def all_func():
    dl = gen_dlink(5)
    n = dl.get_node(3)
    print(n.val)
    print(n.prev.val)
    print(n.next.val)
    print(dl.tail.val)
    dl.del_at_index(dl.count-1)
    print(dl.tail.val)

all_func()


"""
题意：删除链表中等于给定值 val 的所有节点。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]

"""

def move_node(l,tar):

    head = Node(next=l,val=0)
    cur = head
    while(head):
        if cur.next.val == tar:
            cur.next = cur.next.next
            cur = cur.next
    return head.next

