
import math
import os



"""
生成窗口最大值数组
from 《左程云 程序员代码面试指南》
a stable array 
a stable window's size
return max elements from array including windows

"""

def getWindowArraybySize(source_array,stable_size):

     if isinstance(source_array,list) is False or isinstance(stable_size,int) is False :
         return None
     source_size=len(source_array)
     if source_size < stable_size:
         print("stable size too much larger")
         return None

     index=source_size-stable_size+1 #real element size
     i=0

     retList=[]
     while index  > 0:
         windows = []
         i=source_size-stable_size+1 - index #
         pos=i
         print("circle i value="+str(i))
         print("stable size="+str(stable_size))
         while  i< stable_size+pos:
              windows.append(source_array[i])
              i+=1

         max1=max(windows)
         del windows

         retList.append(max1)

         index-=1

     return retList



"""
source=[12,23,34,54,5665,76,87,54,34]
print("source length="+str(len(source)))
stable_size=9

me=getWindowArraybySize(source,stable_size)

print(me)

"""

