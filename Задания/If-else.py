# password, passver =input(), input()
# if password==passver:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# n=int(input())
# if n%2==0:
#     print('Четное')
# else:
#     print('Нечетное')

# n=int(input())
# a,b,c,d=n//1000,(n//100)%10,(n//10)%10, n%10
# if a+d==b-c:
#     print('ДА')
# else:
#     print('НЕТ')

# n=int(input())
# if n>=18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# a,b,c=int(input()),int(input()),int(input())
# if b==((a+c)/2): print('YES')
# else: print("NO")

# a,b=int(input()),int(input())
# print(min(a,b))

# n=int(input())
# if n<=13: print("Детство")
# if n<=24 and n>13: print("Молодость")
# if n<=59 and n>24: print("Зрелость")
# if n>=60: print("Старость")

# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)

# n=int(input())
# if n>-1 and n<17:print('Принадлежит')
# else:print("Не принадлежит")

# a,b,c,d=int(input()),int(input()),int(input()),int(input())
# if 0<a<9 and 0<b<9 and 0<c<9 and 0<d<9:
#     if (a==c and b==d) or (a==d and (b==c-1 or b==c+1)) or (b==c and (a==d+1 or a==d-1)) or ((a==d+1 or a==d-1) and (b==c+1 or b==c-1)): print("YES")
#     else:print("NO")

# a,b,c=int(input()),int(input()),int(input())
# min,med,max=min(a,b,c),a+b+c-min(a,b,c)-max(a,b,c),max(a,b,c)
# print(med)

# a,b,c=int(input()),int(input()),input()
# if c=="/" or c=="+" or c=="*" or c=='-':
#     if c=="+": print(a+b)
#     if c=="-": print(a-b)
#     if c=="*": print(a*b)
#     if c=="/":
#         if b==0:print("На ноль делить нельзя!")
#         else: print(a/b)
# else:print("Неверная операция")

# n=int(input())
# if 0<=n<=36:
#     if n==0: print('зеленый')
#     if 0<n<=10 or 18<n<=28:
#         if n%2==0: print('черный')
#         elif n%2==1: print('красный')
#     if 10<n<=18 or 28<n<=36:
#         if n%2==0: print('красный')
#         elif n%2==1: print('черный')
# else: print('ошибка ввода')

# a1,b1,a2,b2=int(input()),int(input()),int(input()),int(input())
# if a2<a1: a2,a1=a1,a2
# if b1<a2: print("пустое множество")
# elif b1==a2 or a2==b2: print(a2)
# elif a1<=a2<b1 and b2<b1: print(a2, b2)
# elif a1<=a2<b1 and b1<b2: print(a2,b1)

# n=int(input())
# if n%100==0: print('YES')
# else: print("NO")

# a,b,c,d=int(input()),int(input()),int(input()),int(input())
# if (a%2==0 and b%2==0) or (a%2==1 and b%2==1):
#     if (c%2==0 and d%2==0) or (c%2==1 and d%2==1): print("YES")
#     else: print("NO")
# elif (a%2==1 and b%2==0) or (a%2==0 and b%2==1):
#     if (c%2==1 and d%2==0) or (c%2==0 and d%2==1): print("YES")
#     else:print("NO")

# age,sex=int(input()), input()
# if 10<=age<=15 and sex=="f": print("YES")
# else: print('NO')

# n=int(input())
# if n==1:print("I")
# elif n==2:print("II")
# elif n==3:print("III")
# elif n==4:print("IV")
# elif n==5:print("V")
# elif n==6:print("VI")
# elif n==7:print("VII")
# elif n==8:print("VIII")
# elif n==9:print("IX")
# elif n==10:print("X")
# else: print("ошибка")

# n=int(input())
# if n%2==1: print("YES")
# elif n%2==0 and 2<=n<=5: print("NO")
# elif n%2==0 and 6<=n<=20: print("YES")
# elif n%2==0 and n>20: print("NO")

# a,b,c,d=int(input()),int(input()),int(input()),int(input())
# if a==b and c==d: print("YES")
# else: print("NO")

# a,b,c,d=int(input()),int(input()),int(input()),int(input())
# double=max(a,c)-min(a,c)
# double2=max(b,d)-min(b,d)
# one=max(b,d)-min(b,d)
# one2=max(a,c)-min(a,c)
# if double==2 and one==1 or double2==2 and one2==1: print("YES")
# else: print("NO")

a,b,c,d=int(input()),int(input()),int(input()),int(input())
if (-1<=a-c<=1) and (-1<=b-d<=1) or (a==c and b!=d) or (b==d and a!=c): print("YES")
else:print("NO")