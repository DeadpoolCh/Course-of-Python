# планиметрия, стериометрия, эконом, теорчисл, уравнение

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -10**5
# for i in list1:
# 	if max(i) > maximum: maximum = max(i)
# print(maximum)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in range(len(list1)):
# 	list1[i].reverse()
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in list1:
# 	total+=sum(i)
# 	counter+=len(i)
# print(total/counter)

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
# for row in my_list:
#     maximum = max(row)
#     minimum = min(row)
# print(maximum + minimum)

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
# maximum = my_list[0][0]
# minimum = my_list[0][0]
# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)#
# print(maximum + minimum)

# n=int(input())
# print(*[[i for i in range(1,n+1)]]*n,sep='\n')

# n=int(input())
# list=[[j for j in range(1,i+1)] for i in range(1,n+1)]
# print(*list,sep='\n')

# def pascal(number):
# 	trig=[1]
# 	for _ in range(number):
# 		trig=[0]+trig+[0]
# 		newtrig=[]
# 		for i in range(len(trig)-1):
# 			newtrig.append(trig[i]+trig[i+1])
# 		trig=newtrig
# 	return trig
# print(pascal(int(input())))

# def pascal(number):
# 	trig=[[1 for j in range(i+1)] for i in range(number+1)]
# 	for i in range(2,number+1):
# 		for j in range(1,i):
# 			trig[i][j]=trig[i-1][j-1]+trig[i-1][j]
# 	for i in range(len(trig)-1):
# 		print(*trig[i])
# pascal(int(input()))

# str=input().split()
# dooble=[]
# temp=[]
# for i in range(len(str)-1):
# 	temp.append(str[i])
# 	if str[i] != str[i + 1]:
# 		dooble.append(temp)
# 		temp = []
# temp.append(str[-1])
# dooble.append(temp)
# print(dooble)

# def chunked(list,chunk):
# 	output=[]
# 	for i in range(0,len(list),chunk):
# 		output.append(list[i:i+chunk])
# 	return output
# print(chunked(input().split(),int(input())))

# str=input().split()
# output=[[]]
# for i in range(1,len(str)+1):
# 	for j in range(len(str)-i+1):
# 		output.append(str[j:j+i])
# print(output)

# *************************************************************************

# n=int(input())
# m=int(input())
# matrix=[]
# for i in range(n):
# 	matrix.append([input() for _ in range(m)])
# for i in range(n):
# 	print(*matrix[i])

# n=int(input())
# m=int(input())
# matrix=[]
# for i in range(n):
# 	matrix.append([input() for _ in range(m)])
# for i in range(n):
# 	print(*matrix[i])
# print()
# for j in range(m):
# 	for i in range(n):
# 		print(matrix[i][j],end=' ')
# 	print()

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# sum=0
# for i in range(n):
# 	for j in range(n):
# 		if i==j:
# 			sum+=matrix[i][j]
# print(sum)

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# count=0
# for i in range(n):
# 	med=sum(matrix[i])/n
# 	for j in range(n):
# 		if matrix[i][j]>med: count+=1
# 	print(count)
# 	count=0

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# maximum=[]
# for i in range(n):
# 	for j in range(n):
# 		if i>=j:maximum.append(matrix[i][j])
# print(max(maximum))

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# maximum=[]
# for i in range(n):
# 	for j in range(n):
# 		if (i>j and i<n-1-j) or (i<j and i>n-1-j) or i==j or j==n-i-1:maximum.append(matrix[i][j])
# print(max(maximum))

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# quarterI=[]
# quarterII=[]
# quarterIII=[]
# quarterIV=[]
# for i in range(n):
# 	for j in range(n):
# 		if i<j and i<n-1-j:quarterI.append(matrix[i][j])
# 		elif i<j and i>n-1-j: quarterII.append(matrix[i][j])
# 		elif i>j and i>n-1-j: quarterIII.append(matrix[i][j])
# 		elif i>j and i<n-1-j: quarterIV.append(matrix[i][j])
# print(f'Верхняя четверть: {sum(quarterI)}\nПравая четверть: {sum(quarterII)}\nНижняя четверть: {sum(quarterIII)}\nЛевая четверть: {sum(quarterIV)}')

# n,m=int(input()),int(input())
# matrix=[[str(i*j).ljust(3) for j in range(m)] for i in range(n)]
# for _ in range(n):
# 	print(*matrix[_])

# n=int(input())
# m=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# index=[]
# for i in range(n):
# 	for j in range(m):
# 		if matrix[i][j]==max(max(matrix,key=max)):
# 			index.append(i)
# 			index.append(j)
# 			break
# print(index[0],index[1])

# n=int(input())
# m=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# ij=input().split()
# for k in range(n):
# 	matrix[k][int(ij[0])],matrix[k][int(ij[1])]=matrix[k][int(ij[1])],matrix[k][int(ij[0])]
# for _ in range(n):
# 	print(*matrix[_])

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# count=0
# for i in range(n):
# 	for j in range(n):
# 		if matrix[i][j]!=matrix[j][i]:
# 			count+=1
# if count==0: print("YES")
# else: print("NO")

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
# 	for j in range(n):
# 		if i==j: matrix[i][j],matrix[n-i-1][i]=matrix[n-i-1][i],matrix[i][j]
# for row in matrix:
# 	print(*row)

# n=int(input())
# matrix=[int(i) for i in input().split() for _ in range(n)]
# matrix.reverse()
# for row in matrix:
# 	print(*row)

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# for j in range(n):
# 	for i in range(n-1,-1,-1):
# 		print(matrix[i][j], end=' ')
# 	print()

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# numbers=sorted([int(matrix[i][j]) for j in range(n) for i in range(n)])
# count=0
# for i in range(1,n**2+1):
# 	if i in numbers and numbers.count(i)==1:
# 		count+=1
# 	else: print("NO"); break
# rowssum,collumssum=[],[]
# sumdiag,sumpobdiag=0,0
# if count==n**2:
# 	for i in range(n):
# 		rowssum.append(sum(matrix[i]))
# 		sumdiag+=matrix[i][i]
# 		sumpobdiag+=matrix[i][n-i-1]
# 		sumcollums=0
# 		for j in range(n):
# 			sumcollums+=matrix[j][i]
# 		collumssum.append(sumcollums)
# 	if collumssum==rowssum and rowssum.count(sumdiag)==n and sumdiag==sumpobdiag: print('YES')
# 	else: print('NO')

# ****************************************************************************

# input=[int(i) for i in input().split()]
# matrix=[['.' for i in range(input[1])] for _ in range(input[0])]
# for i in range(input[0]):
# 	for j in range(input[1]):
# 		if i%2==0 and j%2==1: matrix[i][j]='*'
# 		elif i%2==1 and j%2==0: matrix[i][j]='*'
# for row in matrix:
# 	print(*row,sep=' ')

# n=int(input())
# matrix=[['0' for _ in range(n)] for _ in range(n)]
# for i in range(n):
# 	for j in range(n):
# 		if i+j==n-1: matrix[i][j]=1
# 		elif ((i<j or i>j) and i>n-1-j) or (i==j and i>n//2-1): matrix[i][j]=2
# for row in matrix:
# 	print(*row, sep=' ')

# input=[int(i) for i in input().split()]
# matrix=[[0 for _ in range(input[1])] for _ in range(input[0])]
# numbers=[i for i in range(1,input[0]*input[1]+1)]
# for i in range(input[0]):
# 	for j in range(input[1]):
# 		matrix[i][j]=i*input[1]+j+1
# for row in matrix:
# 	for i in row:
# 		print(str(i).ljust(3), end=' ')
# 	print()

# input=[int(i) for i in input().split()]
# matrix=[[0 for _ in range(input[1])] for _ in range(input[0])]
# numbers=[i for i in range(1,input[0]*input[1]+1)]
# for i in range(input[0]):
# 	for j in range(input[1]):
# 		matrix[i][j]=j*input[0]+i+1
# for row in matrix:
# 	for i in row:
# 		print(str(i).ljust(3), end=' ')
# 	print()

# input=[int(i) for i in input().split()]
# matrix=[[0 for _ in range(input[1])] for _ in range(input[0])]
# numbers=[i for i in range(1,input[0]*input[1]+1)]
# for i in range(input[0]):
# 	for j in range(input[1]):
# 		matrix[i][j]=j*input[0]+i+1
# for row in matrix:
# 	for i in row:
# 		print(str(i).ljust(3), end=' ')
# 	print()

# n=int(input())
# matrix=[[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     matrix[i][i]=1
#     matrix[i][n-i-1]=1
# for r in matrix:
# 	for c in r:
# 		print(str(c).ljust(3), end=' ')
# 	print()

# n=[int(i) for i in input().split()]
# matrix = [[0] * n[1] for _ in range(n[0])]
# for i in range(n[0]):
#     for j in range(n[1]):
#         matrix[i][j] = (i + j) % n[1] + 1
# for row in matrix:
#     print(*row)

# n=[int(i) for i in input().split()]
# matrix = [[0] * n[1] for _ in range(n[0])]
# num = 1
# for i in range(n[0]):
#     if i % 2 == 0:
#         for j in range(n[1]):
#             matrix[i][j] = num
#             num += 1
#     else:
#         for j in range(n[1] - 1, -1, -1):
#             matrix[i][j] = num
#             num += 1
# for row in matrix:
#     print(*row)

# n,m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
# num = 1
# for i in range(n+m):
#     for j in range(n):
#         for k in range(m):
#             if j+k==i: matrix[j][k] = num; num += 1
# for row in matrix:
#     print(*row)

# n=int(input())
# matrix=[[1 for _ in range(n)] for _ in range(n)]
# for i in range(n):
# 		if (i>j and i<n-1-j) or (i<j and i>n-1-j): matrix[i][j]=0
# for r in matrix:
# 	for c in r:
# 		print(str(c).ljust(3), end=' ')
# 	print()

# input=[int(i) for i in input().split()]
# matrix=[[0 for _ in range(input[1])] for _ in range(input[0])]

# ***************************************************************************

# nm=[int(i) for i in input().split()]
# matrix1=[[int(i) for i in input().split()] for _ in range(nm[0])]
# input()
# matrix2=[[int(i) for i in input().split()] for _ in range(nm[0])]
# for i in range(nm[0]):
# 	for j in range(nm[1]):
# 		matrix1[i][j]+=matrix2[i][j]
# for row in matrix1:
# 	print(*row,end='\n')

# nm=[int(i) for i in input().split()]
# matrix1=[[int(i) for i in input().split()] for _ in range(nm[0])]
# input()
# mk=[int(i) for i in input().split()]
# matrix2=[[int(i) for i in input().split()] for _ in range(mk[0])]
# mult=[[0 for _ in range(mk[1])] for _ in range(nm[0])]
# for i in range(nm[0]):
# 	for j in range(mk[1]):
# 		for x in range(nm[1]):
# 			mult[i][j]+=matrix1[i][x]*matrix2[x][j]
# for row in mult:
# 	print(*row, end='\n')

# n=int(input())
# matrix=[[int(i) for i in input().split()] for _ in range(n)]
# stage=int(input())
# matrix2=matrix[:]
# mult=[[0 for _ in range(n)] for _ in range(n)]
# for _ in range(stage-1):
# 	for i in range(n):
# 		for j in range(n):
# 			for x in range(n):
# 				mult[i][j]+=matrix[i][x]*matrix2[x][j]
# 	matrix2=mult[:]
# 	mult=[[0 for _ in range(n)] for _ in range(n)]
# for row in matrix2:
# 	print(*row, end='\n')












