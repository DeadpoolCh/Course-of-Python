# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = []
# for i in range(len(tuples)):
# 	if len(tuples[i])!=0 or tuples[i].count('')>0:
# 		non_empty_tuples.append(tuples[i])
# print(non_empty_tuples)

#************************************************************************************

# poets = [("Есенин", 13),("Тургенев", 14),("Маяковский", 28),("Лермонтов", 20),("Фет", 15),]
# for i in range(len(poets)):
#     for j in range(i + 1, len(poets)):
#         if poets[i][1] > poets[j][1]:
#             poets[i], poets[j] = poets[j], poets[i]
# print(poets[0])
# print(poets[-1])

# poets = [("Тургенев", 14),("Есенин", 13),("Маяковский", 28),("Фет", 15),("Лермонтов", 20)]
# for i in range(len(poets)):
#     for j in range(i + 1, len(poets)):
#         if poets[i] > poets[j]:
#             poets[i], poets[j] = poets[j], poets[i]
# print(poets[0])
# print(poets[-1])

# **************************************************************************************

# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# mult=1
# for i in numbers:
# 	mult*=i
# print(mult)

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data=list(poet_data)
# poet_data[2]="Москва"
# print(tuple(poet_data))

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# medsum=[]
# for i in numbers:
# 	medsum.append(sum(i)/len(i))
# print(medsum)

# a,b,c=int(input()),int(input()),int(input())
# print((-b/(2*a),(4*a*c-b**2)/(4*a)))

# n=int(input())
# students=[tuple(input().split()) for _ in range(n)]
# goodboy=[]
# for student in students:
# 	if int(student[1])>3: goodboy.append(student)
# for row in students:
# 	print(*row,end='\n')
# print()
# for row in goodboy:
#     print(*row,end='\n')

# n = int(input())
# f1, f2, f3 = 1, 1, 1
# for i in range(n):
#     print(f1,end=' ')
#     f1, f2, f3 = f2, f3, f1 + f2 + f3



















































