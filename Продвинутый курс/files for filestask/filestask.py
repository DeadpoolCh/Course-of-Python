# file=open(input())
# print(*list(map(str.strip,file.readlines())))
# file.close()
from unittest.mock import right

# file=open(input())
# strfile=list(map(str.strip,file.readlines()))
# print(strfile[-2])
# file.close()

# from random import randrange
# file=open(r'files for filestask/lines.txt',encoding='utf-8')
# strfile=list(map(str.strip,file.readlines()))
# print(strfile[randrange(len(strfile))])
# file.close()

# file=open(r'files for filestask/numbers.txt')
# strfile=[int(i.strip()) for i in file.readlines()]
# print(sum(strfile))
# file.close()

# file=open(r'files for filestask/nums.txt')
# strfile=[int(i.strip()) for i in file.readlines() if i.strip()!='']
# print(sum(strfile))
# file.close()

# file=open(r'files for filestask/prices.txt',encoding='utf-8')
# strfile=[i.strip().split('\t') for i in file.readlines()]
# total=0
# for name,count,price in strfile:
#     total+=int(count)*int(price)
# print(total)
# file.close()

# *************************************************************

# with open(r'files for filestask/text.txt') as file:
#     strfile=[i.split() for i in file.readlines()][0]
#     invert=[i[::-1] for i in strfile]
#     print(*invert[::-1])

# with open(r'files for filestask/data.txt') as file:
#     strfile=[i.strip() for i in file.readlines()]
#     print(*strfile[::-1],sep='\n')

# with open(r'files for filestask/lines (1).txt') as file:
#     strfile=[i.strip() for i in file.readlines()]
#     for str in strfile:
#         if len(str)==len(max(strfile,key=len)): print(str)

# import re
# with open(r'files for filestask/nums (1).txt') as file:
#     numstr=[re.findall(r'\d+', i) for i in file.readlines()]
#     sumsstr=sum([int(j) for i in numstr for j in i])
#     print(sumsstr)

# with open(r'files for filestask/file.txt') as file:
#     lines=[i.strip() for i in file.readlines()]
#     words=[i.split() for i in lines]
#     countwords=sum([len(i) for i in words])
#     letters=sum([sum(len(j.strip(',.!?/-')) for j in i if not(j.isdigit())) for i in words])-9
#     print(f'Input file contains:\n{letters} letters\n{countwords} words\n{len(lines)} lines ')

# with open(r'files for filestask/first_names.txt') as names, open(r'files for filestask/last_names.txt') as surname:
#     from random import choice
#     firstnames=[i.strip() for i in names.readlines()]
#     lastnames=[i.strip() for i in surname.readlines()]
#     for _ in range(3):
#         print(f'{choice(firstnames)} {choice(lastnames)}')

# with open(r'files for filestask/population.txt') as country:
#     countries=[i.strip().split('\t') for i in country.readlines()]
#     for countr in countries:
#         if countr[0][0]=='G' and int(countr[1])>500000:
#             print(countr[0])

# def read_csv():
#     with open(r'files for filestask/data.csv') as data:
#         titles=data.readline()[:-1].split(',')
#         datas=[]
#         for lines in data:
#             line = lines.strip().split(',')
#             linedict = {key: value for key, value in zip(titles, line)}
#             datas.append(linedict)
#         return datas

# *******************************************************************************************

# with open(r'files for filestask/17.4.txt','w') as output:
#     print(input(),file=output)

# with open(r'files for filestask/random.txt','w') as output:
#     from random import randrange
#     for _ in range(25):
#         print(randrange(111,778),file=output)

# with open(r'files for filestask/input.txt') as input, open(r'files for filestask/output.txt', 'w') as output:
#     lines =[i.strip() for i in input.readlines()]
#     for i in range(1,len(lines)+1):
#         print(f'{i}) {lines[i-1]}', file=output)

# with open(r'files for filestask/class_scores.txt', encoding='utf8') as score, open(r'files for filestask/new_scores.txt','w', encoding='utf8') as score2:
#     lines=[i.strip().split() for i in score.readlines()]
#     for line in lines:
#         line[1]=min(100,int(line[1])+5)
#         print(*line,file=score2)

# with open(r'files for filestask/goats.txt') as file, open(r'files for filestask/answer.txt','w') as answer:
#     lines=[i.strip() for i in file.readlines()]
#     count={}
#     for i in range(lines.index('COLOURS')+1,lines.index('GOATS')):
#         count.setdefault(lines[i],0)
#         count[lines[i]]=lines.count(lines[i])-1
#     sums=sum(count.values())
#     for i in count.keys():
#         if count[i]/sums>0.07: print(i,file=answer)

# n=[input() for _ in range(int(input()))]
# for file in n:
#     with open(file,'r') as input,open('output.txt','a') as output:
#         for line in input:
#             output.write(line)

# with open(r'files for filestask/logfile.txt',encoding='utf-8') as log,open('output.txt','w',encoding='utf-8') as output:
#     for lines in log:
#         line=lines.strip().split(', ')
#         time=[[int(j) for j in i.split(':')] for i in line[1:]]
#         time=(time[1][0]*60+time[1][1])-(time[0][0]*60+time[0][1])
#         print(line,time)
#         if time>=60:print(line[0],file=output)

# *******************************************************************
# Экзамен
# *******************************************************************

# with open(input(), encoding='utf8') as file:
#     print(len(file.readlines()))

# with open(r'files for filestask/ledger.txt') as file:
# 	print(f'${sum([int(i.strip('$')) for i in file.readlines()])}')

# with open(r'files for filestask/grades.txt') as file:
# 	lines=[[int(j) for j in i.split()[1:]] for i in file.readlines()]
# 	print(len(list(filter(lambda x:x[0]>=65 and x[1]>=65 and x[2]>=65,lines))))

# with open(r'files for filestask/words.txt') as file:
# 	words=file.read().strip().split()
# 	print(*list(filter(lambda x:len(x)==len(max(words,key=len)),words)),sep='\n')

# with open(input(),encoding='utf8') as file:
# 	print(*[i.strip() for i in file.readlines()[-10:]],sep='\n')

# n=input()
# n='data (1).txt'
# with open(r'forbidden_words.txt',encoding='utf8') as badword, open(n,encoding='utf8') as strs:
# 	forbidden_words={i:'*'*len(i) for i in badword.read().split()}
# 	s=strs.read()
# 	s_lower=s.lower()
# 	for ban in forbidden_words:
# 		if ban in s_lower: s_lower=s_lower.replace(ban,forbidden_words[ban])
# 	print(*list(map(lambda c1,c2:'*' if c2=='*' else c1,s,s_lower)),sep='')

# with open('cyrillic.txt',encoding='utf8') as file, open('transliteration.txt','w') as output:
# 	trans_lower={'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#     'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#     'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#     'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'}
# 	trans_upper={'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya'}
# 	file_str=file.read()
# 	file_set=sorted(set(file_str))
# 	for i in file_set:
# 		if i in trans_lower: file_str=file_str.replace(i, trans_lower[i])
# 		elif i in trans_upper: file_str=file_str.replace(i, trans_upper[i])
# 	print(file_str,file=output)

# n='def.txt'
# n=input()
# with open(n,encoding='utf8') as file:
# 	def_line=list(filter(lambda x: 'def' in x or '#' in x,[i.strip() for i in file.readlines()]))
# 	right_def=[]
# 	bad_def=[]
# 	if 'def' in def_line[0]:bad_def.append(def_line[0])
# 	for i in range(1,len(def_line)):
# 		if 'def' in def_line[i] and '#' in def_line[i-1]:
# 			right_def.append(def_line[i-1])
# 			right_def.append(def_line[i])
# 		elif '#' not in def_line[i]: bad_def.append(def_line[i])
# 	if len(bad_def)==0: print('Best Programming Team')
# 	else:
# 		for defs in bad_def:
# 			print(defs[defs.index(' ')+1:defs.index('(')])

































