from regular import replacing, matching, splitting

# 8 Write a Python program to split a string at uppercase letters.
    
text = "exampleForString"
pattern = r"(?=[A-Z])"

splitting(pattern, text)