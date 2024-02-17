from regular import replacing, matching, splitting

# 3 Write a Python program to find sequences of lowercase letters joined with a underscore.
    
text = 'wsabbb_fe_dfwefw_wefwe'
pattern = r'([a-z]+_[a-z]+)+'

matching(pattern, text)