from regular import replacing, matching, splitting

# 2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
    
text = 'wsabbb'
pattern = r'.*a(b{2,3}).*'

matching(pattern, text)