
# 1 Create a generator that generates the squares of numbers up to some number N.

# def squares(n):
#     for i in range(n):
#         yield i**2

# generator = squares(int(input()))
# for el in generator:
#     print(el)




# 2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

# def evens(n):
#     for i in range(n):
#         if(i % 2 == 0):
#             yield i
            
# generator = evens(int(input()))
# print(*generator, sep = ", ")




# 3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

# def divisible(n):
#     for i in range(n):
#         if(i % 3 == 0 and i % 4 == 0):
#             yield i
            
# generator = divisible(int(input()))
# print(*generator, sep = ", ")



# 4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

# def squares(a, b):
#     for i in range(a, b + 1):
#         yield i**2

# a = int(input())
# b = int(input())

# for el in squares(a, b):
#     print(el)



# 5 Implement a generator that returns all numbers from (n) down to 0.

# def generator(n):
#     while n >= 0:
#         yield n
#         n -= 1

# # Test the generator with a for loop
# for num in generator(int(input())):
#     print(num)