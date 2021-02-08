import re
# ? -> zero or one
# * -> zero or more
# + -> one or more
# {x} -> exactly x times
# {x,y} -> at least x at most y

batRegex = re.compile(r'Bat(wo)?man')  # question mark indicates that 'wo' can appear zero or one times in the text
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("My number is 415-365-4242")
print(mo.group())

mo = phoneNumRegex.search("My number is 365-4242")
print(mo.group())

batRegex = re.compile(r'Bat(wo)*man')  # asterisk is used to indicate that 'wo' can appear zero or more times
mo = batRegex.search("Batwowowowoman")
print(mo.group())

batRegex = re.compile(r'Bat(wo)+man')  # + is used to indicate that 'wo' can appear one or more times
mo = batRegex.search("Batman")
print(mo == None)

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search("HaHaHa")
print(mo.group())

phoneNumRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneNumRegex.search("My numbers are 415-365-4242,375-4242,435-645-1928")
print(mo.group())

# Greedy and non-greedy matches
# Python tries to match the longest possible expression
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search("1234567890")
print(mo.group())  # prints 12345, greedy

digitRegex = re.compile(r'(\d){3,5}?')  # ? causes it to be non-greedy
mo = digitRegex.search("1234567890")
print(mo.group())  # prints 123, non-greedy


