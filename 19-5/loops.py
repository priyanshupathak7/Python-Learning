#_loops

##_while loop
'''i=1
while i<=5:
    print("hello world")
    i=i+1'''

##_1_to_5
'''i=1
while i<=5:
    print(i)
    i+=1'''

##_end()
'''i=1
while i<=100:
    print(i,end=" ")
    i+=1'''

#_ans1
'''i=1
while i<=100:
    print(i,end=" ")
    i+=1'''
#_ans2
'''i=100
while i>=1:
    print(i,end=" ")
    i-=1'''
#_ans3
'''n=int(input("enter a no.: "))
i=1
while i<=10:
    print(n*i,end=" ")
    i+=1'''
#_ans4
'''n=int(input("enter a no.: "))
i=1
while i<=4:
    print(n**i,end=" ")
    i+=1'''
#_ans5
'''p=1
while p<=10:
    print(p*p,end=" ")
    p+=1'''
##_input_method
'''p=int(input("enter a no.: "))
while p<=10:
    print(p*p,end=" ")
    p+=1'''
#_ans6
'''p=5
while p<=625:
    print(p,end=",")
    p*=p'''
#_2,7,17,32,52.....77
'''t=2
d=5
i=1
while i<=6:
    print(t,end=",")
    t+=d
    d+=5
    i+=1'''

#_dry_run_method_mam_way
#_1,4,9,16,25,36......100_(diff-3,5,7,9,11......100)
'''i=3
while i<=100:
    print(i,end=" ")
    i+=2'''
'''i=3
j=1
while j<=100:
    print(j,end=" ")
    j=j+i
    i+=2'''

'''j=1
i=3
while j<=100:
    print(j,end=" ")
    j=i+j
    i+=2'''
#_2,7,17,32,52,77_(diff-5,10,15,20,77)
'''i=5
while i<=77:
    print(i,end=" ")
    i+=5'''
'''j=2
i=5
while j<=77:
    print(j,end=" ")
    j=i+j
    i+=5'''

#_0,1,1,2,,3,5,8,13,21,34_(fibonacci series)
'''i=0
j=1
while i<=34:
    print(i,end=" ")
    k=i+j
    i=j
    j=k'''

##_factorial_of_any_no. 5(1,2,6,24,120)_diff_(1,4,18,96)
#                         1*2=2*3=6*4=24*5=120
'''j=int(input("enter a no.: "))
i=1
f=1
while i<=j: #5
    f*=i
    print(f, end=" ")
    i+=1'''

##_by_mam
'''j=int(input("enter a no.: "))
i=1
f=1
while i<=j:
    f+=i
    i+=1
print("factorial of",j,"is",f)'''

#####################################################_class_5_(23/05)_##########################################################

##_sum_of_entered_no.:
'''n=int(input("enter no. of entries: "))
i=1
k=0
while i<=n:
    x=int(input("enter a no.: "))
    k=k+x
    i+=1
print("sum of entered no.: ",k)'''

##_prime_no.
'''a=int(input("enter a no.: "))
i=2
while i<=a//2:
    if a%i==0:
        print("no. is not prime")
        break
    i+=1
else:
    print("no. is prime")'''

##_between_1_to_100_prime_no's_in_series:
'''k=2
while k<=100:
    i=2
    while i<=k//2:
        if k%i==0:
            break
        i+=1
    else:
        print(k,end=" ")
    k+=1'''

#########################################################_class_26/5_###########################################################
##_reverse_of_a_number
'''q=int(input("enter a number: "))           #_a=q
rev=0
while q>0:
    rem=q%10                                  #_remainder(rem)
    q=q//10                                   #_quetiont(q)
    rev=rev*10+rem
print(rev)'''

##_check weather a number is armstrong or not?
##_armstrong number- it is a no. where the no. is separated and each separation's cube will result into the separated no. after adding the cubes.
##_153-1,5,3 so the cube of 1,5,3 after being add
'''a=int(input("enter a number: "))
r=0
sum=a
while sum>0:
    num=sum%10
    sum=sum//10
    r=r+num*num*num
if r==a:
    print("it is an armstrong")
else:
    print("not an armstrong")'''

################################################################################################################################################

###############################___________________class-30/5______________________________###################################

######################___________________for_loop______________________________###########################

'''for i in range(5):    #_it will start with 0(default)
    print(i)'''         #_in range if your number end with 5 then it will stop on 4
                      #_in_(start,stop,step)_ex.-(1,11,2)-1,3,5,7,9__

'''for i in range (1,11,2):
    print(i,end=" ")'''

#_my way for any table
'''n=int(input("enter your no.: "))
for i in range (n,n*11,n):
    print(i)'''

#_mam for any table
'''n=int(input("enter your no.: "))
for i in range (1,11):
    print(n*1)'''

#_reverse number
'''for i in range(100,0,-1):
    print(i)'''

#_factorial of any no.
'''n=int(input("enter your no.: "))
fact=1
for i in range(1,n+1):
    fact*=i
    print("the factorial of",n,"is",fact)'''  #_this is for series

'''n=int(input("enter your no.: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("the factorial of",n,"is",fact)''' #_this is for direct result

#_sum
'''n=int(input("enter your no.: "))
sum=0
for i in range (1,n+1):
    sum+=i
print("the sum of",n,"is",sum)'''

#######################################_break,Pass,Continue_##################################

#__________________________break___________________________#
'''i=1
while i<=5:
    print(i)
    if i==2:
        break #_look break then finish
    i+=1'''

#______________________continue(Skip)__________________#
'''p=1              
while p<=5:
    if p==4:
        p+=1
        continue  #_skip
    print(p)
    p+=1'''

#___________________________pass________________________#
'''for i in range(5):
    pass
print("end of loop")'''

############################################################################################################################################
