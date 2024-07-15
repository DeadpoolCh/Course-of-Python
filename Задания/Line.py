# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# n=str(input())
# for i in range(0, len(n), 2):
#     print(n[i])

# n=str(input())
# for i in range(-1,-len(n)-1,-1):
#     print(n[i])

# name=str(input())
# surname=str(input())
# fathername=str(input())
# print(surname[0], name[0], fathername[0],sep='')

# n=str(input())
# sum=0
# for i in range(0, len(n)):
#     sum+=int(n[i])
# print(sum)

# n=str(input())
# count=0
# for i in range(0, len(n)):
#     print(i,n[i])
#     if n[i].isdigit():
#         count+=1
# if count>0:
#     print("Цифра")
# else: print("Цифр нет")

# n=str(input())
# countplus,countstar=0,0
# for i in range(0, len(n)):
#     if n[i] in '+':
#         countplus+=1
#     if n[i]=='*': countstar+=1
# print('Символ + встречается', countplus,"раз")
# print('Символ * встречается', countstar,"раз")

# n=str(input())
# count=0
# for i in range(0, len(n)-1):
#     if n[i]==n[i+1]:
#         count+=1
# print(count)

# n=str(input()).lower()
# countglas,countsogl=0,0
# for i in range(0, len(n)):
#     if n[i] in 'ауоыиэяюе': countglas+=1
#     if n[i] in 'бвгджзйклмнпрстфхцчшщ': countsogl+=1
# print('Количество гласных букв равно',countglas)
# print('Количество согласных букв равно',countsogl)

# n=str(bin(int(input())))
# print(n[2::])

# s = 'abcdefg'
# print(s[::-3])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])

# n=str(input())
# if n==n[::-1]: print("YES")
# else: print("NO")

# n=str(input())
# print(len(n),n*3,n[0],n[:3],n[len(n)-3:],n[::-1],n[1:len(n)-1],sep='\n')

# n=str(input())
# print(n[2],n[-2],n[:5],n[:len(n)-2:],n[::2],n[1::2],n[::-1],n[-1::-2],sep='\n')

# n=str(input())
# print(n[len(n)-len(n)//2::]+n[0:len(n)//2+len(n)%2])

# s = 'i LEARN Python LAnguaGE'
# print(s.lower())

# s = '$12344%^$#@!'
# print(s.lower())

# s1 = 'a'
# s2 = s1.upper()
# print(s1, s2)

# s = 'i LEARN Python LAnguaGE'
# print(s.upper())

# s = 'i LEARN Python LAnguaGE'
# print(s.swapcase())

# n=input()
# if n.title()==n:print("YES")
# else: print("NO")

# n=input()
# print(n.swapcase())

# n=input().lower()
# if 'хорош' in n: print("YES")
# else: print("NO")

# n=input()
# count=0
# for i in n:
#     if i.islower(): count+=1
# print(count)

# ********************************

# s = 'www.stepik.org'
# print(s.startswith('www'))

# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))

# n=input()
# print(n.count(' ')+1)

# n=input().lower()
# print("Аденин:", n.count('а'))
# print("Гуанин:", n.count('г'))
# print("Цитозин:", n.count('ц'))
# print("Тимин:", n.count('т'))

# n=int(input())
# count=0
# for i in range(n):
#     s=input()
#     if s.count('11')>=3: count+=1
# print(count)

# n=input()
# count=0
# for i in n:
#     if i.isdigit(): count+=1
# print(count)

# n=input()
# if n.endswith('.ru') or n.endswith('.com'): print("YES")
# else: print("NO")

# n=input()
# max=0
# for i in n:
#     if n.count(i)>=max:
#         max=n.count(i)
#         symbol=i
# print(symbol)

# n=input()
# if n.count('f')==0: print("NO")
# if n.count('f')==1: print(n.find('f'))
# if n.count('f')>1: print(n.find('f'), n.rfind('f'))

# n=input()
# print(n[0:n.find('h')]+n[n.rfind('h')+1:])

# *****************************

# n=int(input())
# for i in range(1,n+1):
#     s=input()
#     if s.isspace(): print(i,": COMMENT SHOULD BE DELETED",sep='')
#     elif len(s)==0: print(i,": COMMENT SHOULD BE DELETED",sep='')
#     else: print(i,": "+s,sep='')

# n=input()
# if 9<=len(n)<=10:
#     if n[0] in 'АВЕКМНОРСТУХ' and n[4] in 'АВЕКМНОРСТУХ' and n[5] in 'АВЕКМНОРСТУХ' and n[1].isdigit() and n[2].isdigit() and n[3].isdigit() and n[6]=='_' and n[7].isdigit() and n[8].isdigit():
#         if len(n)==10:
#             if n[9].isdigit():print("YES")
#             else: print("NO")
#         else: print("YES")
#     else: print("NO")
# else: print("NO")

# n=input()
# if n.startswith('@'):
#     if 5<=len(n)<=15:
#         if n==n.lower() and n[1::].isalnum():
#             print("Correct")
#         else:print("Incorrect")
#     else:print("Incorrect")
# else:print("Incorrect")

# ***********************************

# date,dollars,uan=input(),input(),input()
# print(f'На {date}: 1$ = {dollars}₽, 1¥ = {uan}₽')

# a,b=int(input()),int(input())
# print(f'Для чисел {a} и {b}:\n  Сумма кубов: {a}**3 + {b}**3 = {a**3+b**3}\n  Куб суммы: ({a} + {b})**3 = {(a+b)**3}')

# numdays,weight=int(input()),float(input())
# if weight<=100-0.2*numdays: print(f'Все идет по плану\n#{numdays} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100-0.2*numdays} кг')
# else:print(f'Что-то пошло не так\n#{numdays} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100-0.2*numdays} кг')

# **************************************************

# a,b=int(input()),int(input())
# for i in range(a,b+1):
#     print(chr(i),end=' ')

# n=str(input())
# for i in n:
#     print(ord(i),end=' ')

# Шифр Цезаря (Code of Ceasar)
# n,s=int(input()),str(input())
# for i in s:
#     print(chr(ord('a')+(ord(i)-ord('a')+26-n)%26),end='')

# ****************************************
# Экзамен

# s = 'Python rocks!'
# print(s.replace('o','@',1))

# n=input()
# for i in range(len(n)):
#     if i%3!=0: print(n[i],end='')

# s=input()
# print(s.replace('1', 'one'))

# s=input()
# print(s.replace('@', ''))

# s=input()
# if s.count('f')==0: print(-2)
# elif s.count('f')==1: print(-1)
# else: print(s.find('f',s.find('f')+1))

# s=input()
# print(s[0:s.find('h')]+s[s.rfind('h'):s.find('h'):-1]+s[s.rfind('h'):])