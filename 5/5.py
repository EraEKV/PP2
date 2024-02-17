from regular import replacing, matching, splitting

# 5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
    
text = 'areferfadb'
pattern = r'(a.*b$)'

matching(pattern, text)