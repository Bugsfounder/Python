import re

mystr = '''Tata Limited
    Dr. David Landsman, executive director
    18, Grosvenor Place
    London SW1X 7HSc
    Phone: +44 (20) 7235 8281
    Fax: +44 (20) 7235 8727
    Email: tata@tata.co.uk
    Website: www.europe.tata.com
    Directions: View map
    
    Tata Sons, North America
    1700 North Moore St, Suite 1520
    Arlington, VA 22209-1911
    USA
    Phone: +1 (703) 243 9787
    Fax: +1 (703) 243 9791
    66-66
    455-4545
    Email: northamerica@tata.com
    Website: www.northamerica.tata.com
    Directions: View map fass
    harry bhai lekin 
    Bahut hi badia aadmi haiaiin
    Manisha is a very good girl haiinaiiiii'''

# ALL FUNCTIONS OF REGULAR EXPRESSIONS
# findall, search, split, finditer, sub

# RAW STR
# print("\n")
# print(r"\n")

# patt = re.compile(r'fass')
# patt = re.compile(r'.adm')  # ANY CHARACTER AND ADM
# patt = re.compile(r'^Tata')  # STARTSWITH
# patt = re.compile(r'girl$')  # ENDSWITH
# patt = re.compile(r'ai*')  # Zero or more occurrences
# patt = re.compile(r'a*i*')  # Zero or more occurrences
# patt = re.compile(r'ai+')  # One or more occurrences
# patt = re.compile(r'ai{2}')  # Exactly the specified number of occurrences
# patt = re.compile(r'ai{2}')  # Exactly the specified number of occurrences
# patt = re.compile(r'(ai){2}')  # Capture and group
# patt = re.compile(r'(ai){1}')  # Capture and group
# patt = re.compile(r'ai{1}|t')  # Capture and group
# patt = re.compile(r'ai{1}|Fax')  # Capture and group

# Special Sequences

# patt = re.compile(r'\ATata')
# patt = re.compile(r'\AFax')
# patt = re.compile(r'\bFax')
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')

# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)
# print(mystr[532:536])

# Task
# Given a string with a lot of indian phone numbers starting from +91

str = '''+91 2432432423,
        +91 7532432423,
        +91 8732432423'''

pattern = re.compile(r'\W{1}91 \d{10}')
match = pattern.finditer(str)
for m in match:
    print(m)
