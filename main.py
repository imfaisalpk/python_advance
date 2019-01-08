
# from math import pi
import math
import sys
# import this
import update
import config

from decimal import Decimal
from fractions import Fraction

import random

def test_func():
    '''i am a test func'''
    print("Hello I am Faisal")

def outer_function():
    b = 20
    def inner_func():
        c = 30
        nonlocal b
        global a
        
        c+=1
        a+=1
        b+=1
        print(a,b,c)
    inner_func()

a = 10

def var_args(name,greet="Good morning"):
    print(name,greet)

def arbi_args(*names):
    print(names[0])

def factorial(num):
    if num==1:
        return 1
    else:
        return num * factorial(num -1)

multiply = lambda x,y : x*y



# print(test_func.__doc__)
# test_func()

if __name__ == "__main__":

    # print(random.randrange(1,20))
    x = ['a', 'b', 'c', 'd', 'e']
    # print(random.choice(x))
    print(random.shuffle(x))
    print(random.random())

    # print(math.pi)
    # print(math.cos(math.pi))
    # print(math.exp(10))
    # print(math.log10(1000))
    # print(math.sinh(1))
    # print(math.factorial(6))
    # print(Fraction('1.4'))

    # d = Decimal('1.1')+Decimal('2.2')
    # print(d)
    # print(Decimal('1.2') * Decimal('2.50'))

    # print(0.1)
    # print(Decimal(0.1))

    # print(config.a,config.b)

    # my_list = [1, 5, 4, 6, 8, 11, 3, 12]

    # print(list(filter(lambda x:(x%2==0),my_list)))
    # print(list(map(lambda x:(x*2),my_list)))

    # print(multiply(2,3))


    # print("factorial: {ans}".format(ans=factorial(3)))
    # var_args(greet="Hello",name="mfaisal")
    # arbi_args(1,2,3,4)


    # genre = ['pop', 'rock', 'jazz']
    # i=0
    # while i< len(genre):
    #     print(genre[i])
    #     i+=1
    # else:
    #     print("while exhausted..") 

    # for item in genre:
    #     print(item)
    #     break
    # else:
    #     print("else part")
        # print(str(item)+" "+genre[item])
    # print(list(range(1,10,2)))


    # numbers = [1,2,3]

    # for i in numbers:
    #     print(i)

    # outer_function()
    # x = 2
    # x = 'Hello World!'
    # x = [1,2,3]
    # print(id([1,2,3]))
    # x = test_func()
    # x
    # print(id(x))
    # x=x+1
    # print(id(3))
    # print(id(x))
    

    # x = 'Hello world'
    # print(id('Hello world'))
    # print(id(x))

    # y = {1:'a',2:'b'}

    # print(1 in y)




    # x1 = 5
    # y1 = 5
    # x2 = 'Hello'
    # y2 = 'Hello'
    # x3 = [1,2,3]
    # y3 = [1,2,3]

    # print(x3 is y3)


    # x = 10 #0000 1010
    # print(x>>2) #0000 0010
    # print(x<<2) #0010 1000

    # print(5//4)
    # print(5>4)
    # print(pi)
    # print(sys.path)

    # a = input("Input a: ")
    # b = input("Input b: ")
    # c = int(a)+int(b)
    # print("c:{answer}".format(answer=c))
    # print(eval('2+3+2'))
    # print("m","faisal",sep='*',end=';\n')
    # print("{0} my name is {1}".format("Hello,","mfaisal"))
    # print("{greetings} my name is {name}".format(greetings="Hello,",name="mfaisal"))
    # print("%s my name is %s"%("Hello,","mfaisal"))

    # list_ex = [1,2,3,4]
    # tuple_ex = (1,2,3)
    # dict_ex = {'1':1,'2':2,'3':3}
    # set_ex = {1,2,3,3}

    # print(set_ex)

    # a = 1
    # a="1"
    # a = 1.0
    # a = '1'
    # a =100
    # b= 0b01100100
    # o = 0o144
    # h = 0x64
    # i = 3.14j
    # f = 3.14
    # unicode = u"\u00dcnic\u00f6de"
    # raw_str = r'abc\n'
    # print(unicode)
    # print(raw_str)

    # print(a,b,o,h,f,i,i.real,i.imag)