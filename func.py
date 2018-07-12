

'''
 simple function use
'''
'''
def  test(a,b,c):
    print(a)
    print(b)
    print(c)



test(1,3,4)

'''

'''
mutil argv
'''

def func(*num):
    for i in num:
        print(i)

func(1,2,3,4)

def func1(**num):

     for (k,v) in num.items():
         print(k,v)


     print(len(num))


#func1(age=1,name=2)


t={"name":"jakcwu","age":2}

#print(t)

print("map length=" ,len(t))
print(t.pop(("name")))

print(len(t))






