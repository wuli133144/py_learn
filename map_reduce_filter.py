


'''
 hi guys ,notice this expression,
 if you use lambda ,or function name
 like: map(add,sequece[.....])
 reference to every iterm,it will call add
 then produce a list[] return

'''
'''
def add(x):
    return x+x

a=map(lambda  x:x+x,[1,2,3])

for i in a:
    print(i)
'''

'''
 filter function test
 filter function mainly use to choose valid values across function
 filter(fiter_func,[.....])
 
'''


'''
b=filter(lambda x:x%2==0,[i for i in range(10)])

for i ,j  in enumerate(b):
    print(i,j)
#print(enumerate(b))
'''
'''
 convert msg_ackMap to list struct
 
'''

def getindexCh(session,ch,index=0):
    try:
        if ch is None or session is None :
            return None
        else:
            session =str(session)

            List=session.split(ch)
            retList=[x for x in List[1:]]
            return retList


    except ValueError:
           print("input args error")



#def link_msg_ack()

def filter_valid_msg_ack( **ack_msg_map ):
    if ack_msg_map is None:
        return []
    if len(ack_msg_map) == 0:
        return []
    else:
         for (i,j) in ack_msg_map.items():
              pre_list=getindexCh(i,"_")
              print(pre_list)




test={"session_4_40_49":123,"session_5_46_49":234}

#print(test.items())
#filter_valid_msg_ack(session_4_40_49=123,session_5_46_49=3)
#for key,value in test.items():
#    print(key,value)
#for key,valus in test.iteritems():
#    print(key,valus)
#filter_valid_msg_ack(test)
#a=getindexCh("session_4_40_49","_",0)
#print(a)


def isvalid(arg):
    if isinstance(arg,str):
        for i in arg:
           if i.isalnum() == True:
               return False
        return True
    else:
        print("failed")





List=[3,4,2,6,743,34];

'''
 sorted function
 
'''
def sorted(l=[]):
    if l is None:
        return []
    else:
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                 if l[i]>l[j] :
                     a=l[i]
                     l[i]=l[j]
                     l[j]=a


    return l




#a=sorted(List)
#print(a)

class stack(object):
    '''
     stack include
     push()
     pop()
     size()
     capacity()
    '''
    def __init__(self,capaci):

            self.capacity=capaci
            self.size=0
            self.__container=[]


    def push(self,v):
        if self.size > self.capacity:
            return
        self.__container.append(v)
        self.size=self.size+1


    def pop(self):
        if self.size < 1:
            return None
        self.size=self.size-1
        return self.__container.pop()

    def getsize(self):
        return self.size

    def getcapacity(self):
        return self.capacity

    def __repr__(self):
        if self.size <1 :
          return "stack "
        else :
            return "statck size="+str(self.getsize())
    def show(self):
        if self.getsize() <1 :
            return
        for i in self.__container:
             print(i)

