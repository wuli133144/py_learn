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
        self.size+=1

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

    """
     reverse doublelink
    """

    def reverse(self):
        if self.head == None:
            return
        p=self.head
        q=p
        while p != None:
            q=p
            p=p.next
            m=q.pre
            q.pre=q.next
            q.next=m

        self.head=q

    def  delKnode(self,k):
        if isinstance(k,int) is False or k < 1 :
            return False

        sz=self.sz() if self.sz() != 0 else None

        p=self.head
        q=p
        i=0
        while p!= None and i < k:
             q=p
             p=p.next
             i+=1

        if p != None:
            q.next=p.next
            pass
        else:
            q.next=None
        self.size-=1
        return True

    def find(self,v):
        p=self.head
        while p != None:
            if p.value1()  == v:
                break
            p=p.next
        if p != None:
            return True
        return False
    def __repr__(self):
        a="double list "
        print(a)


d=doublelink()
d.add(23)
d.add(34)
d.add(56)
d.add(56)
d.add(56)
d.add(56)

d.show()
print(d.sz())


print("############find()##############")

b=d.find(23)
print(b)
print("##################")
d.rshow()

print("###############")


d.reverse()
d.show()


print("####################")

d.rshow()

print("del k node")


d.delKnode(5)
d.show()


print("############find()##############")

b=d.find(23)
print(b)
