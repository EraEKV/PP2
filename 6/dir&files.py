import os




# 1 Write a Python program to list only directories, files and all directories, files in a specified path.

# path = os.getcwd()
# print(f"Files: {[f for f in os.listdir(path) if os.path.isfile(f)]}, directories: {[d for d in os.listdir(path) if os.path.isdir(d)]} all elements are: {os.listdir(path)}")




# 2 Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

# path = os.getcwd()
# print(f"Path accessibility: Existance: {os.path.exists(path)}, Reading: {os.access(path, mode=os.R_OK)}, Writing: {os.access(path, mode=os.W_OK)}, Executability: {os.access(path, mode=os.X_OK)}")




# 3 Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

# path = os.getcwd()
# if os.path.exists("jk.txt"): 
#     print(os.listdir(path))
# else:   
#     print("The file or such directory doesn't exist")




# 4 Write a Python program to count the number of lines in a text file.

# with open("file.txt", 'r') as file:
#     count = sum(1 for line in file) 
# print(count)




# 5 Write a Python program to write a list to a file.

# li = [x ** 2 for x in range(11)]
# with open('jk.txt', 'w') as file:
#     for i in li:
#         file.write(str(i) + " ")





# 6 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for letter in alphabet:
#     with open(f"{letter}.txt", 'x'):
#         pass





# 7 Write a Python program to copy the contents of a file to another file

# with open("file.txt", 'r') as file:
#     with open("newFile.txt", 'w') as newfile:
#         for line in file:
#             newfile.write(line)




# 8 Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

# os.remove("jk.txt") if os.path.exists("jk.txt") else print("The file does not exist")
