from functools import reduce

# 1 Write a Python program with builtin function to multiply all the numbers in a list

# numbers = [x for x in range(1, 6)]
# result = reduce(lambda x, y: x * y, numbers)
# print(result)




# 2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

# string = "mifnweIONGoOIngiorne"
# lowers = sum(map(lambda x : x.islower(), string))
# uppers = sum(map(lambda x : x.isupper(), string))
# print(f"Uppers: {uppers}, lowers: {lowers}")



# 3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.

# word = "kazak"
# print(word == word[::-1])




# 4 Write a Python program that invoke square root function after specific milliseconds.

# from time import sleep

# def after_root(number, tm):
#     sleep(tm / 1000)
#     return number**0.5
# number, tm = int(input()), int(input())

# print(f"Square root of {number} after {tm} miliseconds is {after_root(number, tm)}")





# 5 Write a Python program with builtin function that returns True if all elements of the tuple are true.

# first = (True, True, True)
# second = (False, True, True)

# print(all(first))
# print(all(second))