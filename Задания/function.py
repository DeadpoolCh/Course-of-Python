# # объявление функции
# def draw_box():
#     print('*'*10)
#     for _ in range(12):
#         print('*',' '*6,'*')
#     print('*'*10)
# # основная программа
# draw_box()  # вызов функции

# def draw_triangle():
#     for i in range(1,11):
#         print('*'*i)
# # основная программа
# draw_triangle()  # вызов функции

# ****************************************************************

# def draw_triangle(fill, base):
#     for i in range(1,base//2+2):
#         print(fill*i)
#     for j in range(base-(base//2+1),0,-1):
#         print(fill*j)
# fill = input()
# base = int(input())
# draw_triangle(fill, base)

# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(),name[0].upper(),patronymic[0].upper(),sep='')
# name, surname, patronymic = input(), input(), input()
# print_fio(name, surname, patronymic)

# def print_digit_sum(num):
#     sum = 0
#     while num!=0:
#         sum += num%10
#         num//=10
#     print(sum)
# n = int(input())
# print_digit_sum(n)

# **********************************************************

# def convert_to_miles(km):
#     return km * 0.6214
# num = int(input())
# print(convert_to_miles(num))

# def get_days(month):
#     if month == 2: return 28
#     if month % 2 == 1 and month < 8:
#         return 31
#     elif month % 2 == 0 and month > 7:
#         return 31
#     else:
#         return 30
# num = int(input())
# print(get_days(num))

# def get_factors(num):
#     return [i for i in range(1,num//2+1) if num%i==0]
# n = int(input())
# print(get_factors(n))
# def get_factors(num):
#     return len([i for i in range(1,num+1) if num%i==0])
# n = int(input())
# print(get_factors(n))

# def find_all(target, symbol):
#     return [i for i in range(len(target)) if target[i]==symbol]
# s = input()
# char = input()
# print(find_all(s, char))

# def merge(list1, list2):
#     list=[]
#     for i in list1:list.append(i)
#     for j in list2:list.append(j)
#     for i in range(len(list)):
#         for j in range(i+1, len(list)):
#             if list[i]>list[j]:
#                 list[i], list[j] = list[j], list[i]
#     return list
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
# print(merge(numbers1, numbers2))

# def lists_of_number(count):
#     result = []
#     for i in range(count):
#         numbers=[int(c) for c in input().split()]
#         for i in numbers:
#             result.append(i)
#     print(*sorted(result))
# lists_of_number(int(input()))

# *******************************************************

# def is_valid_triangle(side1, side2, side3):
#     if side1+side2>side3 and side1+side3>side2 and side3+side2>side1: return True
#     else: return False
# a, b, c = int(input()), int(input()), int(input())
# print(is_valid_triangle(a, b, c))

# def is_prime(num):
#     delit=[]
#     if num<2: return False
#     else:
#         for i in range(1, num+1):
#             if num%i==0: delit.append(i)
#     if 1 in delit and num in delit and len(delit)==2: return True
#     else: return False
# n = int(input())
# print(is_prime(n))

# def is_prime(num):
#     delit=[]
#     if num<2: return False
#     else:
#         for i in range(1, num+1):
#             if num%i==0: delit.append(i)
#     if 1 in delit and num in delit and len(delit)==2: return True
#     else: return False
# def get_next_prime(num):
#     while True:
#         num+=1
#         if is_prime(num): return num
# n = int(input())
# print(get_next_prime(n))

# def is_password_good(password):
#     if len(password)>=8 and [i.isupper() for i in password].count(True)>0 and [i.isdigit() for i in password].count(True)>0 and [i.islower() for i in password].count(True)>0: return True
#     else: return False
# txt = input()
# print(is_password_good(txt))

# def is_one_away(word1, word2):
#     count=0
#     if len(word1)==len(word2):
#         for i in range(len(word1)):
#             if word1[i]==word2[i]:count+=1
#     else: return False
#     if count==len(word1)-1: return True
#     else: return False
# txt1 = input()
# txt2 = input()
# print(is_one_away(txt1, txt2))

# def is_palindrome(text):
#     text=text.lower()
#     for i in ['.',',','!','?','-',' ']:
#         text=text.replace(i, '')
#     if text==text[::-1]: return True
#     else: return False
# txt = input()
# print(is_palindrome(txt))

# def is_prime(num):
#     delit=[]
#     if num<2: return False
#     else:
#         for i in range(1, num+1):
#             if num%i==0: delit.append(i)
#     if 1 in delit and num in delit and len(delit)==2: return True
#     else: return False
# def is_valid_password(password):
#     password=password.split(':')
#     if len(password)!=3: return False
#     if password[0]==password[0][::-1] and is_prime(int(password[1])) and int(password[2])%2==0: return True
#     else: return False
# psw = input()
# print(is_valid_password(psw))

# def is_correct_bracket(text):
#     backet=0
#     for i in text:
#         if i=='(': backet+=1
#         if i==')': backet-=1
#         if backet<0: return False
#     if backet==0: return True
#     else: return False
# txt = input()
# print(is_correct_bracket(txt))

# def convert_to_python_case(text):
#     result = ''
#     for i in text:
#         if i.isupper():
#             result += '_' + i.lower()
#         else:
#             result += i
#     return result.lstrip('_')
# txt = input()
# print(convert_to_python_case(txt))

# def get_middle_point(x1, y1, x2, y2):
#     return (x1 + x2) / 2, (y1 + y2) / 2
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# def get_circle(radius):
#     from math import pi
#     return 2*pi*radius, pi*radius**2
# r = float(input())
# length, square = get_circle(r)
# print(length, square)

# def solve(a, b, c):
#     disk=b**2-4*a*c
#     if disk>=0: return min((-b-disk**0.5)/(2*a), (-b+disk**0.5)/(2*a)), max((-b-disk**0.5)/(2*a), (-b+disk**0.5)/(2*a))
# a, b, c = int(input()), int(input()), int(input())
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# ***********************************************************************
# Экзамен
# ***********************************************************************

# def draw_triangle():
#     for i in range(1,9):
#         print(' '*(8-i) + '*'*(2*i-1))
# draw_triangle()

# def get_shipping_cost(quantity):
#     if quantity==1: return 1000
#     elif quantity>1: return 1000 + (quantity-1)*120
#     else: return 0
# n = int(input())
# print(get_shipping_cost(n))

# def compute_binom(n, k):
#     from math import factorial
#     return factorial(n) // (factorial(k) * factorial(n-k))
# n = int(input())
# k = int(input())
# print(compute_binom(n, k))

# def number_to_words(num):
#     ones = [' ','один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if num<10: return ones[num]
#     elif num<20: return teens[num-10]
#     elif num<100: return tens[num//10] +' ' + ones[num%10]
# n = int(input())
# print(number_to_words(n))

# def get_month(language, number):
#     en_months=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     ru_month=['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     if language=='en': return en_months[number-1]
#     else: return ru_month[number-1]
# lan = input()
# num = int(input())
# print(get_month(lan, num))

# def is_magic(date):
#     date=date.split('.')
#     date[1]=date[1].replace('0','')
#     if int(date[0])*int(date[1])==int(date[2])%100: return True
#     else: return False
# date = input()
# print(is_magic(date))

# def is_pangram(text):
#     text=text.lower().strip()
#     alphabet='abcdefghijklmnopqrstuvwxyz'
#     for i in alphabet:
#         if i not in text: return False
#     return True
# text = input()
# print(is_pangram(text))