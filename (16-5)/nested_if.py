#_Nested_if
'''age=int(input("enter your age:"))
age=35
if (age>=18):
    if age>80:
        print("he can't drive due to age limit")
    else:
        print("he can drive")
else:
    print("he cannot drive")'''

'''##_4_nestedifs
age = int(input("Enter your age: "))
if age >= 18:
    if age >= 80:
        print("He can't drive due to age limit")
    else:
        if age <= 25:
            print("He can drive but must be supervised")
        else:
            if age >= 60:
                print("He can drive but needs a medical certificate")
            else:
                print("He can drive")
else:
    print("He cannot drive")'''

##_ans1
'''a=int(input("1st no.:"))
if a>=0:
    if a>=90:
        print("A")
    else:
        if a>=80 :
            print("b")
        else:
            if a>=60 :
                print("c")
            else:
                if a>=50 :
                    print("d")
                else:
                    print("e")
else:
    print("fail")'''

##_ans2_(nested_if)
'''a=int(input("enter no. a:"))
b=int(input("enter no. b:"))
c=int(input("enter no. c:"))
if (a>b):
    if (a>c):
        print("a is greater")
    else:
        print("c is greater")
else:
    if (b>c):
        print("b is greater")
    else:
        print("c is greater")'''

##_ans2_by_mam_(elif)
a=int(input("enter no. a:"))
b=int(input("enter no. b:"))
c=int(input("enter no. c:"))
if (a>b):
    if (a>c):
        print("a is greater",a)
    else:
        print("c is greater",c)
elif c>b:
    print("c is greater",b)
else:
    print("b is greater",c)

