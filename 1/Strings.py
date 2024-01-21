# 1
x = "Hello world"
print(len(x))


# 2
txt = "Hello World"
x = txt[0]


# 3
txt = "Hello World"
x = txt[2:5]


# 4
txt = " Hello World "
x1 = txt[1:len(txt) - 1]
x2 = txt.strip()


# 5
txt = "Hello World"
txt = txt.upper()


# 6
txt = "Hello World"
txt = txt.lower()


# 7 
txt = "Hello World"
txt = txt.replace("H", "J")


# 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
print(f"My name is John, and I am {age}")