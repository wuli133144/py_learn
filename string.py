import  math
#import  string


#print("test string ")
#print("terst")
"""
from <左程云算法>
判断两个字符串是否为变形词
"""

def ischangedstr(str1,str2):
    if isinstance(str1,str) is False or isinstance(str2,str) is False:
        return False

    dictionary={}

    if len(str1) < 1 or len(str2) <1 or len(str1)!= len(str2):
        return False

    for i in range(len(str1)):
        if dictionary.get(str1[i]) ==None:
            dictionary[str1[i]] =1
        else:
            dictionary[str1[i]] += 1

        pass

    for i in range(len(str2)):
        if dictionary.get(str2[i]) == None:
            return  False
        else:
            dictionary[str2[i]]-=1



    for i ,j in enumerate(dictionary):
         if dictionary[j] != 0:
             return False


    return True




"""
 
 计算字符串里的子串数字之和
 
"""

def calculatesubstr(str1):
     list_num=[]

     size=len(str1)
     if size < 1:
         return None

     temp_num=0
     _space_tag=1

     for i in range(size):
          if str1[i]=='-' and str1[i+1] == '-':
             _space_tag=_space_tag*(1)

          elif str1[i]=='-' and str1[i+1] != '-':
             _space_tag=_space_tag*(-1)
             pass
          elif str.isdigit(str1[i]):
              temp_num+=temp_num*10+_space_tag*int(str1[i])
              pass
          elif  str.isdigit(str1[i]) is False and str1[i]!='-':
              continue




#bRet=ischangedstr("abcdefgg","abcdefgg")
#print(bRet)


"""

    删除字符串中连续出现k个0 返回子串
    just delete first element 
    the root cause of this is one loop ,one loop 
    can delete one suitable item,

"""


def deleteK0(str1,k):
    if  isinstance(str1,str)  is False or len(str1) <1 or k <1:
        return None

    tag=0
    pos=0
    j=i=0

    while j < len(str1):

        for i in range(j,len(str1)):
            if tag < k and str1[i] != '0':
                tag=0
                continue
            if tag == k and i+1 < len (str1) and str1[i+1] != '0':
                pos=i
                str2 = []
                str2[0:] = str1[0:pos - k]
                str2[pos - k:] = str1[pos:]
                str1 = str2
                del str2
                break
            elif tag == k and i+1 >= len(str1):
                pos=i
                str2 = []
                str2[0:] = str1[0:pos - k]
                str2[pos - k:] = str1[pos:]
                str1 = str2
                del str2
                break
            elif tag < k and str1[i]=='0':
                tag+=1

        j=pos+1
        if pos+1 > len(str1):
            break





    print(str1)




deleteK0("1230002300023000",3)
