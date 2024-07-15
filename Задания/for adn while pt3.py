# for n in range(1,14):
#     for k in range(1,13):
#         for m in range(1,13):
#             if 28*n+30*k+31*m==365: print(n,k,m)

# for b in range(1,11):
#     for k in range(1,21):
#         for t in range(1,200):
#             if 10*b+5*k+0.5*t==100 and b+k+t==100:print(b,k,t)

# for a in range(1,151):
#     for b in range(a+1,151):
#         for c in range(b+1,151):
#             for d in range(c+1,151):
#                 e=int((a**5+b**5+c**5+d**5)**0.2)
#                 if e**5==int(a**5+b**5+c**5+d**5): print(a,b,c,d,e,a+b+c+d+e); break

# ***********************************

# n=int(input())
# num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num, end=' ')
#         num+=1
#     print()

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end='')
#     for k in range(i-1,0,-1):
#         print(k, end='')
#     print()

# a,b=int(input()),int(input())
# max, total=0, 0
# for i in range(a,b+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=j
#         if count>=total: total=count; max=i
# print(max,total)

# n=int(input())
# for i in range(1,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0: count+=1
#     print(i, '+'*count, sep='')

# n,ost=int(input()),0
# while n!=0:
#     ost=n%10
#     n=n//10+ost
#     if n<10:
#         break
# print(n)

# n,fac,facsum=int(input()),1,0
# for i in range(1,n+1):
#     fac=fac*i
#     facsum+=fac
# print(facsum)

# a,b,count=int(input()),int(input()),0
# for i in range(a,b+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

# ************************
# Экзамен

# n=int(input())
# for i in range(1,n+1):
#     if i==1 or i==n: print('*'*19)
#     else:
#         print('*'+' '*(19-2)+'*')

# n=str(input())
# len=len(n)
# n=int(n)
# if len==3: print(n%10)
# elif len==4: print((n//10)%10)
# else: print((n//10**(len-3))%10)

# n=int(input())
# count3=0
# countlast=0
# count2=0
# summore5=0
# multmore7=1
# count0and5=0
# countmore7=0
# lastdigit=n%10
# while n>0:
#     digit=n%10
#     if digit==3: count3+=1
#     if digit==lastdigit: countlast+=1
#     if digit==0 or digit==5: count0and5+=1
#     if digit%2==0: count2+=1
#     if digit>7:
#         countmore7+=1
#         multmore7*=digit
#         if countmore7==1: more7=digit
#     if digit>5: summore5+=digit
#     n=n//10
# print(count3,countlast,count2,summore5,sep='\n')
# if countmore7==0: print(1)
# elif countmore7==1: print(more7)
# else: print(multmore7)
# print(count0and5)

# for a in range(1,33):
#     for b in range(a,33):
#         for c in range(1,33):
#             for d in range(c,33):
#                 if a**3+b**3==c**3+d**3 and a!=b and b!=c and c!=d and a!=c and b!=d: print(a**3+b**3)