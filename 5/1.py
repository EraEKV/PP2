from regular import replacing, matching, splitting

# 1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
    
text = 'wsabb'
pattern = r'.*a[b]*.*'

matching(pattern, text)