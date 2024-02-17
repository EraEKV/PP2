from re import match, split, search, sub

def matching(pattern, text):
    if match(pattern, text):
        print(f'matched, {text}')
    else:
        print(f'not matched, {text}')


def replacing(pattern, text, replace):
    print(sub(pattern, replace, text).strip())
    

def splitting(pattern, text):
    print(split(pattern, text))






# Examples

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)




#    []	A set of characters	"[a-m]"	
#    \	Signals a special sequence (can also be used to escape special characters)	"\d"	
#    .	Any character (except newline character)	"he..o"	
#    ^	Starts with	"^hello"	
#    $	Ends with	"planet$"	
#    *	Zero or more occurrences	"he.*o"	
#    +	One or more occurrences	"he.+o"	
#    ?	Zero or one occurrences	"he.?o"	
#    {}	Exactly the specified number of occurrences	"he.{2}o"	
#    |	Either or	"falls|stays"	
#    ()	Capture and group




#    A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
#    \b	Returns a match where the specified characters are at the beginning or at the end of a word
#    (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"  r"ain\b"	
#    \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#    (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"  r"ain\B"	
#    \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
#    \D	Returns a match where the string DOES NOT contain digits	"\D"	
#    \s	Returns a match where the string contains a white space character	"\s"	
#    \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
#    \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
#    \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
#    \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"