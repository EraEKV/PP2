from re import sub

# 10 Write a Python program to convert a given camel case string to snake case.
    
text = "exampleForCamelCaseString"
print(sub(r"[A-Z]", lambda x : f"_{x.group().lower()}", text))