# n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
# IandII=n+m-t-x
# IIandIII=m+k-t-y
# IandIII=n+k-t-z
# I,II,III=n-IandII-IandIII-t,m-IandII-IIandIII-t,k-IandIII-IIandIII-t
# print(I+II+III)
# print(IandII+IIandIII+IandIII)
# print(a-(I+II+III+t+IandII+IIandIII+IandIII))

# **************************************************************

# n,m=input(),input()
# setnm=set(n+m)
# print('YNEOS'[len(setnm)!=10::2])

# print('YNEOS'[set(input())!=set(input())::2])

# s=input().split()
# word1,word2,word3=sorted(set(s[0])),sorted(set(s[1])),sorted(set(s[2]))
# print('YES' if word1==word2==word3 else 'NO')

# word=[set(input().lower()) for i in range(int(input()))]
# lens=[len(word[i]) for i in range(len(word))]
# print(*lens, sep='\n')

# word=[input().lower() for i in range(int(input()))]
# sets=set()
# for i in word:
# 	sets.update(i)
# print(len(sets))

# s=[i.strip('.,;:-?-!') for i in input().lower().split()]
# sets=set()
# for i in s:
# 	sets.add(i)
# print(len(sets))

# ***************************************************************
# Экзамен
# ***************************************************************

# data=input().split()
# set_data=set(data)
# print(len(data)-len(set_data))


# cities=set([input() for _ in range(int(input()))])
# if input() in cities: print("REPEAT")
# else: print("OK")

# m,n=int(input()),int(input())
# homelib=set([input() for _ in range(m)])
# sunwork=[input() for _ in range(n)]
# for book in sunwork:
#     if book in homelib: print("YES")
#     else: print("NO")

# set1=set([int(i) for i in input().split()])
# set2=set([int(i) for i in input().split()])
# if len(set1.intersection(set2))>0: print(*sorted(set1.intersection(set2),reverse=True))
# else: print("BAD DAY")

# set1=set([int(i) for i in input().split()])
# set2=set([int(i) for i in input().split()])
# print("YES" if set1==set2 else "NO")

# m, n = int(input()), int(input())
# mathematics_pupil = {input() for _ in range(m)}
# informatics_pupil = {input() for _ in range(n)}
# print(len(mathematics_pupil.difference(informatics_pupil)))

# m, n = int(input()), int(input())
# mathematics_pupil = {input() for _ in range(m)}
# informatics_pupil = {input() for _ in range(n)}
# print(len(mathematics_pupil.symmetric_difference(informatics_pupil)) if len(mathematics_pupil.symmetric_difference(informatics_pupil))>0 else "NO")

# print(*sorted(set(input().split()).union(set(input().split()))))

# m, n = int(input()), int(input())
# students=[input() for _ in range(m+n)]
# set_stud=sorted(set(students))
# count_stud=[students.count(stud) for stud in set_stud]
# print(count_stud.count(1) if count_stud.count(1)>0 else "NO")

# m=int(input())
# students=[[input() for _ in range(int(input()))] for _ in range(m)]
# sets=set(students[0])
# for stud in students:
#     sets=sets.intersection(stud)
# print(*sorted(sets),sep='\n')



































