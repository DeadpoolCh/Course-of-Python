# n=int(input())
# if abs(n//100-n%10)==(n//10)%10: print('Число интересное')
# else: print('Число неинтересное')

# name,surname=str(input()),str(input())
# print('Hello',name,surname+"!", "You have just delved into Python")

# title=str(input())
# print('Футбольная команда <название', title, 'имеет длину', len(title), 'символов')

# city1,city2,city3=str(input()),str(input()),str(input())
# len1,len2,len3=len(city1),len(city2),len(city3)
# if min(len1,len2,len3)==len1: print(city1)
# elif min(len1,len2,len3)==len2: print(city2)
# elif min(len1,len2,len3)==len3: print(city3)
# elif max(len1,len2,len3)==len1: print(city1)
# elif max(len1,len2,len3)==len2: print(city2)
# elif max(len1,len2,len3)==len3: print(city3)

# a,b,c=len(str(input())),len(str(input())),len(str(input()))
# if a+b+c-max(a,b,c)-min(a,b,c)==(max(a,b,c)+min(a,b,c))/2: print("YES")
# else:print('NO')

# n=str(input())
# if "синий" in n: print("YES")
# else: print("NO")

# n=str(input())
# if "суббота" in n or "воскресенье" in n: print("YES")
# else: print("NO")

# n=str(input())
# if "@" in n and "." in n: print("YES")
# else: print("NO")

# from math import sqrt
# a,b,c,d=float(input()),float(input()),float(input()),float(input())
# print(sqrt((a-c)**2+(b-d)**2))

# from math import pi
# r=float(input())
# print(pi*r**2,2*pi*r, sep="\n")

# a,b,=float(input()),float(input())
# print((a+b)/2, (a*b)**0.5, 2*a*b/(a+b), ((a**2+b**2)/2)**0.5, sep='\n')

# from math import sin, cos, tan, radians
# g=float(input())
# r=radians(g)
# print(sin(r)+cos(r)+tan(r)**2)

# from math import floor,ceil
# a=float(input())
# print(floor(a)+ceil(a))

# from math import sqrt
# a,b,c=float(input()),float(input()),float(input())
# disc=b**2-4*a*c
# if disc>0: print(min((-b-sqrt(disc))/(2*a), (-b+sqrt(disc))/(2*a)),max((-b-sqrt(disc))/(2*a), (-b+sqrt(disc))/(2*a)), sep='\n')
# elif disc==0: print(-b/(2*a))
# else: print("Нет корней")

from math import tan, pi
n,a=int(input()), float(input())
print((n*a**2)/(4*tan(pi/n)))