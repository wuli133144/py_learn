


import  os



L=[ i for i in range(3,10) if i %2 ==0 ]

#
L1=map(lambda x:x%2==0,range(3,10))

st="xxxxxxx:xxxxxxxx:fdsafsdafsd:fasdfasf"

du=list(map(lambda x:str.strip(x),st.split(":")))


#求1-100的素数
num=[i for i in range(1,100)]

def func(x):
    for i in range(2,x-1):
        if x / i == 0:
         return None

    return x


x=list(map(func,num))

print(x)



#print(du)





