import  os
import  sys
import  math



class Node(object):
    def __init__(self):
        self.pre=None
        self.next=None
        self.value=None

    def __init__(self,value):
        self.pre=None
        self.next=None
        self.value=value

    def value1(self):
        return self.value

    def __repr__(self):
        print("Node information.....value=%d",self.value())


class doublelink(object):

    def __init__(self):
        self.head=None
        self.size=0

    def add(self,v):
        node=Node(v)
        if self.head == None:
            self.head=Node(v)
            return
        elif self.head.next==None:
            node.pre=self.head
            node.next=self.head.next
            self.head.next=node
        else:
            node.pre = self.head
            node.next = self.head.next
            self.head.next.pre=node
            self.head.next = node


    def show(self):
        p=self.head
        while p!= None:
            print(p.value1())
            p=p.next

    def rshow(self):
        pre=self.head
        p=None
        while pre != None:
            p=pre
            pre=pre.next

        while p!= None:
            print(p.value1())
            p=p.pre

    def begin(self):
        if self.head != None:
            return self.head
        return None

    def end(self):
        p= self.head if self.head != None else  None
        q=None
        while p!= None:
            q=p
            p=p.next
        return q

    def sz(self):
        p = self.head if self.head != None else None
        q = 0
        while p != None:
            q+=1
            p = p.next
        return q
    def reverse(self):
        if self.head == None:
            return



d=doublelink()
d.add(23)
d.add(34)
d.add(56)
d.add(56)
d.add(56)
d.add(56)

d.show()
print(d.sz())
print("##################")
d.rshow()