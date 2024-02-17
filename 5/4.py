from regular import replacing, matching, splitting

# 4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
    
text = 'AfewAjweif'
pattern = r'([A-Z]{1}[a-z]+)+'

matching(pattern, text)