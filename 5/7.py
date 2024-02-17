from re import sub

# 7 Write a python program to convert snake case string to camel case string.
    
text = "example_for_snake_case_string"
print(sub(r"_([a-z])", lambda x : x.group(1).upper(), text))