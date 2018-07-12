
'''
simple implentment

'''

class ListNode(object):
    '''
    list just for algorithm

    '''
    def __init__(self,v):
        self.value=v
        self.next=None


    def add(self,v):
        t=ListNode(v)
        head=self;
        while head.next != None:
            head=head.next

        head.next=t

    def size(self):
        head=self
        sz=0
        while head != None:
            sz+=1
            head=head.next
        return sz

    def show(self):
        t=self
        while t != None:
            print(t.value)
            t=t.next

    def reverse(self):

        p_mark=None
        q_mark=self
        n_mark=self.next
        while n_mark != None:
            #print("reverse:",q_mark.value)
            q_mark.next=p_mark
            p_mark=q_mark
            q_mark=n_mark
            #print("reverse q_mark",q_mark.value)
            n_mark=n_mark.next

        q_mark.next=p_mark

        return q_mark






a=ListNode(3)
a.add(5)
a.add(6)
a.add(5)
a.add(5)
a.show()
print("===================")
#print(a.size())

a=a.reverse()

a.show()


