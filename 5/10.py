from regular import replacing, matching, splitting

# 10 Write a Python program to convert a given camel case string to snake case.
    
text = "exampleForCamelCaseString"
# replace = ""
# pattern = r""
pattern = r"(?=[A-Z])"

print("_".join(split(pattern, text)))
# replacing(pattern, text, replace)