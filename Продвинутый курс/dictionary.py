# Экзамен

# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# my_dict={key: [value for value in value if value<21] for key,value in my_dict.items()}

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# emails=[f'{value}@{key}' for key,values in emails.items() for value in values]
# print(*sorted(emails),sep='\n')

# DNA_RNA={'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# DNA=input()
# for nucl in DNA:
#     print(DNA_RNA[nucl], end='')

# string=input().replace('  ',' ').split()
# dicts={}
# for word in string:
#     dicts[word] = dicts.get(word, 0) + 1
#     print(dicts.get(word),end=' ')

# scrabble={'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
# word=input()
# score=0
# for letter in word:
#     score+=scrabble[letter]
# print(score)

# def build_query_string(params):
#      query=sorted([f'{key}={value}' for key,value in params.items()])
#      return '&'.join(query)

# def merge(values):
#     dicts={}
#     for item in values:
#         for key,value in item.items():
#             if key not in dicts:
#                 dicts[key]=set([value])
#             elif key in dicts:
#                 dicts[key].add(value)
#     return dicts

# files={}
# access={'write': 'W', 'read': 'R','execute': 'X'}
# for _ in range(int(input())):
#     n=input().split()
#     files.update({n[0]:n[1:]})
# for _ in range(int(input())):
#     acc,file=input().split()
#     if access[acc] in files.get(file): print("OK")
#     else: print("Access denied")

# shop={}
# for _ in range(int(input())):
#     name,item,count=input().split()
#     if name not in shop: shop[name]=shop.setdefault(name,{item:int(count)})
#     elif item not in shop[name]: shop[name].update({item:int(count)})
#     else: shop[name][item]=shop[name].get(item,0)+int(count)
# for name in sorted(shop):
#     print(f'{name}:')
#     for key in sorted(shop[name]):
#         print(f"{key} {shop[name][key]}")

















