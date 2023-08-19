# https://devpractice.ru/python-lesson-19-decorators/

'''
# Примеры с вложенными функциями
def sq2(a: list):
    def sq(n):
        print(n*n)
    for it in a:
        sq(it)
a = [1, 2, 3, 4, 5]
sq2(a)
# sq(3) # НЕЛЬЗЯ!

def mul(a):
    def helper(b):
        return a * b
    return helper

f = mul(1)
print(f(2))
n = mul(2)(4)
print(n)
'''

def first_test():
    print("Test 1")

def second_test():
    print("Test 2")

'''
# 1. Задача: добавить вывод перед и после функций
first_test()
second_test()

# 2. Объединяем
def simple_decore(fn):
    print('run function')
    fn()
    print('stop function')
simple_decore(first_test)
simple_decore(second_test)

# 3. Добавляем обертку-wrapper
def simple_decore(fn):
    def wrapper():
        print('run function')
        fn()
        print('stop function')
    return wrapper
first_test_wrapper = simple_decore(first_test)
second_test_wrapper = simple_decore(second_test)
first_test_wrapper()
second_test_wrapper()

# 4. Подменяем имя функции
def simple_decore(fn):
    def wrapper():
        print('run function')
        fn()
        print('stop function')
    return wrapper
first_test()
first_test = simple_decore(first_test)
print('-'*10)
first_test()
'''

# 5. Пример декоратора с оберткой
def simple_decore(fn):
    def wrapper():
        print('run function')
        fn()
        print('stop function')
    return wrapper

@simple_decore
def new_test():
    print("Test new")

new_test()
