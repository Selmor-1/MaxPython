# a = []
# for i in range(1, 1999+1):
#     if i % 2 != 0 and i % 5 != 0:
#         a.append(i/1000)

# print(sum(a))

res = 0
for i in range(1, 1999+1):
    # if not i % 2 == 0 and not i % 5 == 0:
    #     res += i / 1000
    if i % 2 == 0 or i % 5 == 0:
        continue
    res += i
    
print(res/1000)