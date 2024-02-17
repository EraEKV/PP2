from regular import replacing

# 9 Write a Python program to insert spaces between words starting with capital letters.

text = "ExampleStringWithoutSpaces"
replace = " "
pattern = r"(?=[A-Z])"

replacing(pattern, text, replace)