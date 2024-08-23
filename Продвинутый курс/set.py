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

