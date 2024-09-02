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

# from math import tan, pi
# n,a=int(input()), float(input())
# print((n*a**2)/(4*tan(pi/n)))

# letter=ord(input())
# if letter>=1071: print("Дальше букв нет")
# else: print(chr(letter+1))

# word=[input() for _ in range(4)]
# weight=[sum([ord(i) for i in j]) for j in word]
# words=dict(zip(word,weight))
# print(max(words,key=lambda x: words[x]))

# message=input()
# coin=sum([ord(i) for i in message])*3
# print(f"Текст сообщения: '{message}'\nСтоимость сообщения: {coin}🐝")

# message=input()
# coin=sum([ord(i) for i in message])*3
# eng = "eyopaxcETOPAHXCBM"
# rus = "еуорахсЕТОРАНХСВМ"
# for a,b in zip(eng,rus):
# 	message = message.replace(a,b)
# new_coin=sum([ord(i) for i in message])*3
# print(f"Старая стоимость: {coin}🐝\nНовая стоимость: {new_coin}🐝")

# message=input()
# for i in range(64):
# 	uni=ord('А')+i
# 	struni=f'[u-{uni}]'
# 	if struni in message:
# 		message=message.replace(struni,chr(uni))
# print(message)

# words=[]
# while True:
# 	n=input()
# 	if n=='КОНЕЦ': break
# 	else: words.append(n)
# print(f'Минимальная строка ⬇️: {min(words)}\nМаксимальная строка ⬆️: {max(words)}')

# words=[input() for _ in range(4)]
# print((ord(max(words)[-1])*ord(min(words)[-1]))**2)

# classes=[input() for _ in range(int(input()))]
# for clas in classes:
# 	if len(clas)==2 and 1039<ord(clas[1])<1056 and 0<=int(clas[0])<10 : print('YES')
# 	else: print('NO')

# str1=list(map(lambda x: x.lower(),filter(lambda x: x.isalpha(),[i for i in input()])))
# str2=list(map(lambda x: x.lower(),filter(lambda x: x.isalpha(),[i for i in input()])))
# print("YES" if str1==str2 else "NO")

# print(*sorted([input() for _ in range(3)]))

# libs=[input().split(', ') for j in range(int(input()))]
# libs=[[i[0][:i[0].index('.')-2],i[1]] for i in libs]
# sortlib=sorted(libs)
# print("YES" if sortlib==libs else "NO")











