#_operators

##_arithmetic_operators
'''a=5
b=4
print("2 no's.:","a=5,b=4")
print("add:",a+b)
print("divide:",a/b)
print("multiply:",a*b)
print("modulous (remainder):",a%b)
print("exponent (power):",a**b)
print("floor division (quotient):",a//b)'''

##_relational_operators
'''a=5
b=4
print("2 no's.:","a=5,b=4")
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)'''

##_assignment_operators
'''a=5
b=4
print("2 no's.:","a=5,b=4")
a=b
print("if b=4 then a=4:","a:",a,"b:",b)
a+=b
print("a=a+b:","a:",a,"b:",b)
a-=b
print("a=a-b:","a:",a,"b:",b)
a*=b
print("a=a*b:","a:",a,"b:",b)
a**=b
print("a=a**b:","a:",a,"b:",b)
a//=b
print("a=a//b:","a:",a,"b:",b)
a%=b
print("a=a%b:","a:",a,"b:",b)'''

##_logical_operators
'''a=5
b=4
print("2 no's.:","a=5,b=4")
print(a>b and a<b)
print(a>b or a<b)
print(not a==b)'''

#input

##program
'''a=int(input("enter your 1st no. : "))
b=int(input("enter your 2nd no. : "))
print(a,b)
print(a+b)
print(type(a))
print(type(b))'''

'''a=5
b=6
c=a+b
print("sum of",a,"and",b,"is",c)'''

#ans1
'''a=int(input("enter a no. :"))
b=int(input("enter a no. :"))
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**b)
print(a//b)'''
#ans2
'''a=int(input("side of a square:"))
print("area of square:",a*a)
print("perimeter of square:",4*a)'''
#ans3
'''a=int(input("length of rectangle:"))
b=int(input("breath of rectangle:"))
print("area of rectangle:",a*b)
print("perimeter of rectangle:",2*(a+b))'''
#ans4
'''a=int(input("1st side of triangle:"))
b=int(input("1st side of triangle:"))
c=int(input("1st side of triangle:"))
print("area of triangle:",(a*b*c)/2)
print("perimeter of triangle:",a+b+c)'''

####################################################### Class 3 - 14/5 ##########################################################

'''a=int(input("maths marks"))
b=int(input("science marks"))
c=int(input("eng marks"))
print("total",a+b+c)
print("%",a+b+c/300*100)'''

'''a=int(input("maths marks: "))
b=int(input("science marks: "))
c=int(input("eng marks: "))
print("total: ",a+b+c)
print("%: ",a+b+c/300*100)'''

'''a=int(input("maths marks: "))
b=int(input("science marks: "))
c=int(input("eng marks: "))
sum=a+b+c
print("total: ",sum)
print("%: ",sum/300*100)'''

''' "( )" to look more defined otherwise you can use without it. 4spaces(tab) is imp. '''
'''age=int(input("enter your age: "))
if (age>=18):   
    print("he can vote")
else:
    print("he cannot vote")'''
#1
'''a=int(input("number a: "))
b=int(input("number b: "))     
if (a>b):
    print("a is greatest")
else:
    print("b is greatest")'''

#2
'''a=int(input("no.: "))
if (a%7==0):
    print("multiple of 7")
else:
    print("not multiple of 7")'''

#3
'''a=int(input("no.: "))
if (a%2==0):
    print("even")
else:
    print("odd")'''

# if-if-else
'''a=10
if a>6:
    print("a is greater than 2")
if a>9:
    print("a is greater than 3")
else:
    print("a is neither greater than 2 nor greater than 3")'''

# if-elif-else
'''a=2
if a>6:
    print("a is greater than 2")
elif a>9:
    print("a is greater than 3")
else:
    print("a is neither greater than 2 nor greater than 3")'''

#2.1
'''a=int(input("eng no.: "))
b=int(input("maths no.: "))
c=int(input("sci no.: "))
d=int(input("sst no.: "))
sum=a+b+c+d
per=sum/400*100
if   per>=90:
    print("A")
elif per>=80:
    print("B")
elif per>=50:
    print("C")
elif per>=33:
    print("D")
else:
    print("E")'''
#2.2
'''a=int(input("no. a: "))
b=int(input("no. b: "))
c=int(input("no. c: "))
if a>b and a>c:
    print("a is greater than b and c")
elif b>c and b>a:
    print("b is greater than c and a")
else:
    print("c is greater than a and b")'''
#2.3
'''a=(input("colour name: "))
if a=="red":
    print("stop")
elif a=="yellow":
    print("wait")
elif a=="green":
    print("go go go")
else:
    print("light is broken")'''

#2.2(home)
'''a=int(input("no. a: "))
b=int(input("no. b: "))
c=int(input("no. c: "))
if a==b==c:
    print("a is equal to b and c")
elif a>b and a>c:
    print("a is greater than b and c")
elif b>c and b>a:
    print("b is greater than c and a")
elif c>a and c>b:
    print("c is greater than a and b")
elif a==b and a>c:
    print("a is equal to b and greater than c")
elif b==a and b>c:
    print("b is equal to c and greater than a")
elif c==a and c>b:
    print("c is equal to a and greater than b")
elif a==b and a<c:
    print("a is equal to b and smaller than c")
elif b==a and b<c:
    print("b is equal to c and smaller than a")
else:
    print("c is equal to a and smaller than b")'''







