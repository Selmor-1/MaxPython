'''
https://docs-python.ru/standart-library/modul-time-python/funktsija-perf-counter-modulja-time/
'''

import time

start_time = time.perf_counter()
i = 1
for _ in range(1000):
    print(i)
    i *= 10
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")