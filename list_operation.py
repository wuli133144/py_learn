

from list import  ListNode



"""
 question: delete single list reversed K th element from 《左程云面试宝典》
 
"""


def  deleteLastKthelement(list,pos):
    if isinstance(list,ListNode) is False:
        return False
    print("delete elements")
    len=list.size()
    if len < 1 or pos < 1 or pos > len:
        return False
    i=0
    pre=list
    while i < len-pos  and pre.next != None:
        print(pre.value,i)

        pre=pre.next
        i+=1

    if pre.next !=None and pre.next.next!=None:
       pre.next=pre.next.next
    elif  pre.next!= None  and pre.next.next == None :
       pre.next=pre.next.next

    list.show()
    return True





a=ListNode(23)
a.add(23)
a.add(34)
a.add(344)
a.add(345)
a.add(346)
a.show()
print("#############after operation#############")
nRet=deleteLastKthelement(a,1)
print(nRet)

#a.show()



