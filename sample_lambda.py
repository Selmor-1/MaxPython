# https://devpractice.ru/python-lesson-19-decorators/
a = [1, 2, 3, 4, 5]
sq = lambda x: x**2
x5 = sq(5)
print(x5)

b = list(map(sq, a))
print(*b)