from regular import replacing, matching, splitting

# 9 Write a Python program to insert spaces between words starting with capital letters.

text = "exampleStringWithoutSpaces"
replace = " "
pattern = r"(=?[A-Z])"

replacing(pattern, text, replace)