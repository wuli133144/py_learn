

"""
company:sunlands
author:jackwu
description:circle single link
"""

from Node.sNode import *


class  circle_slink(object):

    def __init__(self):
        self.head=None
        #self.head.next=self.head
        self.size=0

    def add(self,v):
        node=sNode(v)
        if self.head == None:
            self.head=node
            self.head.next=self.head

        else:
            node.next=self.head.next
            self.head.next=node
        pass

    def show(self):
        p=self.head
        q=p
        p=p.next

        while p.value1() != q.value1():
              print(p.value1())
              p=p.next
        print(p.value1())

    def  delete(self,pre):
         if pre != None and pre.next!= None :
             pre.next=pre.next.next
         pass

    def yuesefucircle(self,k):
        if k < 1 and self.head != None:
            return None
        p=self.head
        q=p
        toggle=0
        while p != None:

            while toggle < k:
                q=p
                p=p.next
                toggle+=1

            pass



if __name__ == '__main__':
    c=circle_slink()

    c.add(23)
    c.add(24)
    c.add(25)
    c.add(26)
    c.show()