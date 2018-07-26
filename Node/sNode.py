

class sNode(object):
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

    def __cmp__(self, other):
         if other.value1() == self.value:
             return True
         return  False

    def __repr__(self):
        print("sNode information.....value=%d",self.value())