# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Задача 1:
Есть текст. Подсчитать сколько раз в тексте используется каждое слово
данного текста.
Вывести на экран результат в формате:
Word "you" used 4 times.
Word "quit" used 1 time.

Текст: If you quit from the Python interpreter and enter it again, the
definitions you have made (functions and variables) are lost. Therefore,
if you want to write a somewhat longer program, you are better off using
a text editor to prepare the input for the interpreter and running it
with that file as input instead. This is known as creating a script.
As your program gets longer, you may want to split it into several
files for easier maintenance. You may also want to use a handy function
that you’ve written in several programs without copying its
definition into each program.
To support this, Python has a way to put definitions in a file and
use them in a script or in an interactive instance of the interpreter.
Such a file is called a module; definitions from a module can be
imported into other modules or into the main module (the collection
of variables that you have access to in a script executed at the
top level and in calculator mode).
"""

# Шаг 1. Создаем строковую переменну paragraph и Вводим заданный
# текст, как строковую переменную
# paragraph = "word1. Word2, WORD3( WoRd4)word4" - тестовые значения
paragraph = "If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. This is known as creating a script. As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in several programs without copying its definition into each program. To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode)."


# Шаг 2. Делаем все буквы одинакового регистра, чтобы "Шаг" и "шаг" считались
# одним словом
paragraph = paragraph.lower()


# Очищаем текст от знаков препинания и скобок. Код не универсальный. Перед
# написанием проанализировала какие есть символы, кроме букв английского
# алфавита
paragraph = paragraph.replace(".", " ")\
                     .replace(",", " ")\
                     .replace("(", " ")\
                     .replace(")", " ")


# Делим строку на слова), используя символ пробел, как сепаратор
# тип переменной word - список.
words = paragraph.split()


# Представим слова и их количество в тексте в виде пар ключ-значение словаря
words_frequency = {}
for word in words:
    if word in words_frequency:
        words_frequency[word] += 1
    else:
        words_frequency[word] = 1


# Выведем на печать результаты
for word in words_frequency:
    if words_frequency[word] == 1:
        print ('Word "{}" used 1 time'.format(word))
    else:
        print ('Word "{}" used {} times'.format(word, words_frequency[word]))
