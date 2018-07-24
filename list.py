
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






def printCommonItems(iterm1,iterm2):
    if  isinstance(iterm1,ListNode) ==False  or isinstance(iterm2,ListNode) == False:
         print("args type is unsuitable")
         return

    p=iterm1
    q=iterm2
    #Ls=list()

    while p != None and q != None :
        if p.value==q.value :
            #Ls.append(p.value)
            print(str(p.value)+" ")
            p=p.next
            q=q.next
            #pass
        elif p.value > q.value:
              q=q.next

        else:
             p=p.next



#a=ListNode(3)


a=ListNode(11)
a.add(12)
a.add(13)
a.add(14)
a.add(15)

b=ListNode(11)
b.add(13)
b.add(15)
b.add(25)



print("xxx")
printCommonItems(a,b)



