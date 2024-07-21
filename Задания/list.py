# print(list(range(1,int(input())+1)))

# n=int(input())
# abc=[]
# for i in range(97,97+n):
#     abc+=[chr(i)]
# print(abc)

# ********************************

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers),numbers[-1],numbers[::-1], "YES" if [17,5] in numbers else 'NO',numbers[1:-1:],sep="\n")

# n=int(input())
# list=[]
# for i in range(n):
#     list.append(input())
# print(list)

# print([chr(97+i)*(i+1) for i in range(26)])

# n=int(input())
# list=[]
# for i in range(n):
#     list.append(int(input())**3)
# print(list)

# n=int(input())
# list=[]
# for i in range(1,n//2+1):
#     if n%i==0: list.append(i)
# list.append(n)
# print(list)

# n=int(input())
# list=[]
# for i in range(n):
#     list.append(int(input()))
# print([list[i]+list[i+1] for i in range(n-1)])

# n=int(input())
# list=[]
# for i in range(n):
#     list.append(int(input()))
# print([list[i] for i in range(0,n) if i%2==0])

# n=int(input())
# list=[]
# for i in range(n):
#     list.append(input())
# k=int(input())
# for i in range(n):
#     print(list[i][k-1:k],end='')

# n=int(input())
# list=[]
# for i in range(n):
#     list.extend(input())
# print(list)

# ************************

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# print(sum([i**2 for i in numbers]))

# n,number,fun=int(input()),[],[]
# for i in range(n):
#     number.append(int(input()))
#     fun.append(number[i]**2+2*number[i]+1)
# print(*number,'',*fun,sep='\n')

# n=int(input())
# list=[]
# for i in range(n):
#     list.append(int(input()))
# list.remove(max(list))
# list.remove(min(list))
# print(*list,sep='\n')

# n=int(input())
# list=[]
# for i in range(n):
#     s=input()
#     if s not in list:
#         list.append(s)
# print(*list,sep='\n')

# n=int(input())
# list=[]
# for i in range(n):
#     list.append(input())
# k=input()
# for i in range(n):
#     if k.lower() in list[i].lower():
#         print(list[i],sep='\n')

# n=int(input())
# list=[]
# for i in range(n):
#     list.append(input())
# o=int(input())
# search=[]
# for j in range(o):
#     search.append(input())
# for i in list:
#     for j in search:
#         if j.lower() not in i.lower():
#             break
#     else: print(i)

# n=int(input())
# numbers,neg,zero,pos=[],[],[],[]
# for i in range(n):
#     numbers.append(int(input()))
# for j in numbers:
#     if j<0: neg.append(j)
#     elif j==0: zero.append(j)
#     else: pos.append(j)
# print(*neg,*zero,*pos,sep='\n')

# *****************************************

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# print(*input().split(),sep='\n')

# s=input().split()
# for i in range(len(s)):
#     print(s[i][0], end='.')

# print(*input().split('\\'),sep='\n')

# s=input().split()
# for i in s:
#     print(int(i)*'+')

# s=input().split('.')
# count=0
# for i in s:
#     if 0<=int(i)<256: count+=1
# if count==4: print("ДА")
# else: print("НЕТ")

# s=input()
# r=input()
# print(r.join(s))

# s=input().split()
# count=0
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[j]==s[i]:count+=1
# print(count)

# **********************************

# n=input()
# n=int(n[n.find('#')+1:])
# code=[]
# for i in range(n):
#     s=input()
#     if '#' in s: s=s[0:s.find('#')].rstrip()
#     code.append(s)
# print(*code, sep='\n')

# n=[int(i) for i in input().split()]
# n.sort()
# print(*n)
# n.sort(reverse=True)
# print(*n)

# *****************************************

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [m[1:] for m in keywords]
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(i) for i in keywords]
# print(lengths)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords =[i for i in keywords if len(i)>=5]
# print(new_keywords)

# palindromes = [i for i in range(100,1001) if i%10==i//100]
# print(palindromes)

# print(*[i**2 for i in range(1,int(input())+1)],sep='\n')

# print(*[int(i)**3 for i in input().split()])

# print(*[i for i in input().split()],sep='\n')

# print(*[i for i in input() if i.isdigit()],sep='')

# print(*[int(i)**2 for i in input().split() if int(i)%2==0 and (int(i)**2)%10!=4])

# **************************************

# Сортировка выбором
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
# for i in range(n):
#     indexmin=i
#     for j in range(i+1,n):
#         if a[j]<a[indexmin]:indexmin=j
#     a[i],a[indexmin]=a[indexmin],a[i]
# print(a)

# ********************************
# Экзамен

# print([i for i in range(2,int(input())+1,2)])

# l,m=[int(i) for i in input().split()],[int(i) for i in input().split()]
# print(*[l[i]+m[j] for i in range(len(l)) for j in range(len(m)) if i==j])

# ns=[int(i) for i in input().split()]
# print(*[i for i in ns],sep='+',end='=')
# print(sum(ns))

# n=input()
# if len(n)!=len(n.split('-')): ns=n.split('-')
# else: print('NO')
# count=0
# if n[0]=='7' and n[1]=='-':
#     for i in range(len(ns)):
#         if ns[i].isdigit(): count+=1
#     if count==4 and len(ns[1])==3 and len(ns[2])==3 and len(ns[3])==4: print("YES")
#     else: print("NO")
# elif len(ns[0])==3 and len(ns[1])==3 and len(ns[2])==4:
#     for i in range(3):
#         if ns[i].isdigit(): count+=1
#     if count==3: print("YES")
#     else: print("NO")
# else: print("NO")

# print(max([len(i) for i in input().split()]))

# print(*[i[1:]+i[0]+'ки' for i in input().split()])



















