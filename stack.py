import  os
import  math
import  os.path


class stack(object):

    def  __init__(self):
        self.size=0
        self.container=list()
        self.minConn=None
        pass
    def   getsize(self):
        return self.size

    def  push(self,v):
        self.size+=1
        self.container.append(v)
        if (self.minConn) ==None :
            self.minConn=self.container[0]
        else:
            if self.minConn > v:
                self.minConn=v



    def pop(self):
        if self.size == 0:
          return None
        self.size-=1
        return self.container.pop()
    def peek(self):
        return self.container[len(self.container)-1]

    def getmin(self):
        return self.minConn

    def __repr__(self):
        """

         tostirng

        :return:
        """
        print("xxxxx stack")





class queue(object):
    def __init__(self):
        self.stack1=stack()
        self.stack2=stack()
        self.size=0
    pass
    def add(self,v):
        self.stack1.push(v)
        self.size=self.stack1.getsize()
    def poll(self):
        while self.stack1.getsize() != 0:
            self.stack2.push(self.stack1.pop())
            pass

        if self.stack2.getsize() !=0 :
              item=self.stack2.pop()
              while self.stack2.getsize() != 0:
                   self.stack1.push(self.stack2.pop())

              return item
        else:
            return None

    def peek(self):
        while self.stack1.getsize() != 0:
            self.stack2.push(self.stack1.pop())
            pass
        item=None
        if self.stack2.getsize() != 0:
            item = self.stack2.peek()
            while self.stack2.getsize() != 0:
                self.stack1.push(self.stack2.pop())

        return item

    def getsize(self):
        return self.stack1.getsize()


"""
 sort for stack by stack
 author:jackwu
"""
def  SortStack(st):
    if type(st) != "stack" or st.getsize() == 0:
        return None
    temp_stack=stack()

    while st.getsize() != 0 :
        min = st.peek()
        st.pop()
        while st.getsize() != 0:
            if st.peek() < min:
                temp_stack.push(min)
                min=st.peek()
            else:
                temp_stack.push(st.pop())


        while temp_stack.getsize() != 0:
            st.push(temp_stack.pop())

        temp_stack.push(min)







if __name__ == '__main__':
    """
         s=stack()
         s.push(12)
         s.push(23)
         print(s.getsize())
         print(s.getmin())
    """
    q=queue()
    q.add(12)
    q.add(23)
    q.add(34)
    print("q before poll operation"+str(q.getsize()))
    q.poll()
    print("q after poll operation" + str(q.getsize()))

    print("q.peek="+str(q.peek()))
    print(q.getsize())

    #print(type(q))

    pass