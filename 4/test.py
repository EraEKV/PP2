# from datetime import datetime, timedelta

# cur = datetime.now()

# next = timedelta(days=4)

# back = timedelta(days = 6)

# print(cur + next)
# print(cur - back)



# from re import sub, match

# t = "aBdeF"

# pattern = r".*[A-Z].*"
# print(match(pattern, t))

# print(sub(r"[A-Z]", lambda x : f"{x.group().lower()}", t))



# nums = [x**2 for x in range(1, 11)]
# s = map(lambda x : int(x ** .5), nums)
# print(*s)




# first = (True, True, True)
# second = (1, 2, 3)

# print(all(first))
# print(all(second))



# class MyIterator:
#     def __init__(self, max_value):
#         self.max_value = max_value
#         self.current_value = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current_value < self.max_value:
#             self.current_value += 1
#             return self.current_value
#         else:
#             raise StopIteration("Error occured")


# my_iterator = MyIterator(-1)
# for value in my_iterator:
#     print(value)
# try:
#     my_iterator = MyIterator(-1)
#     for value in my_iterator:
#         print(value)
# except StopIteration as e:
#     print("Ошибка: итератор достиг максимального значения.", e)



# def my_generator(max_value):
#     current_value = 0
#     if(max_value < 0):
#         raise ValueError("ValueError occured")
#     else:
#         while current_value < max_value:
#             current_value += 1
#             yield current_value
    

# # Используем генератор
# try:
#     gen = my_generator(-1)
#     for value in gen:
#         print(value)
# except ValueError as e:
#     print(e)






# Lab physics


V = (0, 2, 4, 6, 8, 10, 12, 14)
C = (
    (-3, 0),
    (-2, 1),
    (-1, 0.8),
    (-1, 3),
    (0, 2.95),
    (1, 2),
    (2, 2),
    (2.1, 1)
)

def leg(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

length = []
elec = []
for i in range(1, 8):
    j = i - 1
    length.append(leg(C[i][0], C[i][1], C[j][0], C[j][1]))
    elec.append(2 / length[-1])

print(*length)
print(*elec)
avg = sum(map(lambda x : x, elec)) / 7

dei = []

for i in range(0, 7):
    dei.append(abs(avg - elec[i]))
    print(dei[-1], end = ", ")

sum = 0

for i in dei:
    sum += i**2
print("\n")
print(sum, (sum / 42)**0.5, (sum / 42)**0.5*2.4)