# Пространство имен: глобальное, локальное, встроенное
#Глобальное:
a = 5
b = 10
#Локальное (c, d существуют внутри ф-ии, в основной программе их нельзя вызвать:
# def printer():
#     a = 'Str'
#     b = 'Str 2'
#     c = 15
#     d = 20
#     print(c, d, 'local')
#     print(a, b, 'global')
# print(a, b)
# printer()
# print(a, b)


# def printer():
#     global a, b
#     a = 'Str'
#     b = 'Str 2'
#     c = 15
#     d = 20
#     print(c, d, 'local')
#     print(a, b, 'global')
# print(a, b)
# printer()
# print(a, b)

#Homework

#Пример
# calls = 0   # 1
# def count_calls():  #2
#     global calls
#     calls += 1
#
# def string_info(string):    #3
#     stroka = str(string)
#     result = (len(stroka), stroka.upper(), stroka.lower())
#     count_calls()
#     return result
#
# def is_contains(string, list_to_search):    # 4
#     string = str(string).lower()
#     list_to_search = list(list_to_search)
#     count_calls()
#     for i in range(len(list_to_search)):
#         if str(list_to_search[i]).lower() == string:
#             result = True
#             break
#         else:
#             result = False
#             continue
#     return result
#
# print(string_info('Kalinka'))
# print(string_info('Cavaleria'))
# print(is_contains('cube', ['recycling', 'cyclic', 'sphere'])) # No matches
# print(is_contains('GaZEL', ['List', 'Snow', 'Gazelist', 'gAzeL'])) # Urban ~ urBAN
#
# print(calls)


#Мое
calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = string.lower()
    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Capybara'))
print(string_info('Armaggedon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # No matches
print(is_contains('cycle', ['recycling', 'cyclic'])) # Urban ~ urBAN

print(calls)