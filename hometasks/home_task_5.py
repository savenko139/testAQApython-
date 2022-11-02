"""
Задание 1:
Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'
"""

word = input('Enter your word here: ')

if str(word) == str(word) [::-1] :
    print('+')
else:
    print('-')

"""
Задание 2:
Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'
"""

text = input('Enter your text here: ')
w = input('Which word you want to find? : ')

if text.find(w) == -1:
    print('NO')
else:
    print('YES')


""""
Задание 3:
ользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.
"""

s = input('Enter your string here: ')

if s.startswith('abc'):
    s = s.replace('abc', 'www' )
    print(s)
else:
    print(s + 'zzz')


""""
Задание 4:
Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.
"""

import re

text = input('Enter your text here: ')

newtext = re.sub(r'[^\w]+|[\d]+', r' ', text).strip()

print('Your updated text is: {}!'.format(newtext))


"""
Задание 5:
Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить, что в почте есть символ '@' и '.', 
и если это так, то вывести "YES", иначе "NO"
"""

mail = input('Enter your email adress: ')

if mail.find('@') == -1 and mail.find('.') == -1:
    print('NO')
else:
    print('YES')

"""Констрцкция выше выполняет задачу из условия, но не надежная. В данном случае дучше использовать паттерн регулярного выражения."""

import re

regexp = r'\b[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email = input('Enter your email adress: ')

if (re.fullmatch(regexp, email)):
    print("YES")
else:
    print("NO")

