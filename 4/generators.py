
# 1 Create a generator that generates the squares of numbers up to some number N.

# N = int(input())
# sq = [x**2 for x in range(1, N + 1)]
# print(sq)




# 2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

# n = int(input())
# evens = [x for x in range(0, n + 1) if x % 2 == 0]
# print(*evens, sep=", ")




# 3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

# n = int(input())
# numbers = [x for x in range(0, n + 1) if x % 3 == 0 and x % 4 == 0]
# print(*numbers, sep=", ")




# 4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

a, b = int(input()), int(input())
squares = [x ** 2 for x in range(a, b + 1)]

def squares(a, b):
    yield from (num ** 2 for num in range(a, b + 1))

for square in squares(a, b):
    print(square)
