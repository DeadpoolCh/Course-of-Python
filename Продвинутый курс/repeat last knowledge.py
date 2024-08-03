# a,b=int(input()),int(input())
# print(a+b,a-b,a*b,a/b,a//b,a%b,(a**10+b**10)**0.5,sep='\n')

# mass,height=float(input()),float(input())
# imt=mass/(height**2)
# if imt<18.5: print('Недостаточная масса')
# elif 18.5<=imt<=25: print('Оптимальная масса')
# else: print('Избыточная масса')

# s=input()
# len=len(s)*60
# print(f'{len//100} р. {len-len//100*100} коп.')

# print(len(input().split()))

# year=int(input())
# animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
# print(animals[year % 12])

# number=input()
# if len(number)==5: print(int(number[::-1]))
# else: print(int(number[0]+number[-1:-6:-1]))

# number=input()
# count=0
# sac=''
# if len(number)>3:
# 	for i in range(1,len(number)+1):
# 		sac=number[-i]+sac
# 		count+=1
# 		if count==3:
# 			sac=','+sac
# 			count=0
# 	print(sac.lstrip(','))
# else: print(number)

# n=[int(i) for i in range(int(input()))]
# k=int(input())
# for i in range(1,len(n),k):
# 	n.remove(n[i])
# 	print(len(n),n,sep='\n')
# Надо доделать

# ****************************************************************

# def count_points(list_points):
# 	countI,countII,countIII,countIV=0,0,0,0
# 	for i in range(0,len(list_points),2):
# 		if list_points[i]>0 and list_points[i+1]>0: countI+=1
# 		elif list_points[i]<0 and list_points[i+1]>0: countII+=1
# 		elif list_points[i]<0 and list_points[i+1]<0: countIII+=1
# 		elif list_points[i]>0 and list_points[i+1]<0: countIV+=1
# 	print(f'Первая четверть: {countI}\nВторая четверть: {countII}\nТретья четверть: {countIII}\nЧетвертая четверть: {countIV}')
# n=int(input())
# point=[]
# for i in range(n):
# 	temp=input().split()
# 	for _ in temp:
# 		point.append(int(_))
# count_points(point)

# n=[int(i) for i in input().split()]
# count=0
# for i in range(0,len(n)-1):
# 	if n[i]<n[i+1]:count+=1
# print(count)

# n=input().split()
# if len(n)%2==0:
# 	for i in range(0,len(n)-1,2):
# 		n[i],n[i+1]=n[i+1],n[i]
# else:
# 	for i in range(0,len(n)-2,2):
# 		n[i],n[i+1]=n[i+1],n[i]
# print(*n)

# n=input().split()
# print(*(n[-1::] + n[:-1]))

# n=input().split()
# count=1
# for i in range(len(n)-1):
# 	if n[i]!=n[i+1]: count+=1
# print(count)

# n=[int(input()) for i in range(int(input()))]
# number=int(input())
# count=0
# for i in range(len(n)):
# 	for j in range(i+1,len(n)):
# 		if n[i]*n[j]==number: count+=1
# if count>0: print("ДА")
# else: print("НЕТ")

# n=input()
# k=input()
# figure=['камень','ножницы','бумага','ящерица','Спок']
# if n==k: print('ничья')
# else:
# 	for i in range(5):
# 		for j in range(5):
# 			if figure[i]==n and figure[j]==k:
# 				if abs(i+j)%2==0: print('Руслан')
# 				else: print('Тимур')
# Доделать

# print(len(max(input().split('О'))))

# n=[input() for i in range(int(input()))]
# brokservers=[]
# count=0
# for i in n:
# 	count+=1
# 	for j in i:
# 		if j in ['a','n','t','o','n']:
# 			brokservers.append(count)
# print(*brokservers)
# Доделать

# word=input()+' запретил букву'
# abc=[chr(i) for i in range(ord('а'),ord('я')+1)]
# for i in abc:
# 	if i in word:
# 		print(word+' '+i)
# 		word=word.replace(i,'').lstrip()
# 		word=' '.join(word.split())












