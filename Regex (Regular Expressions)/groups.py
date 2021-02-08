import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match_object = phoneNumRegex.search("My number is 434-565-4242")
print(match_object.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # use parentheses to mark out groups
match_object = phoneNumRegex.search("My number is 434-565-4242")
print(match_object.group(1))

batRegex = re.compile(r'Bat(man|mobile|copter|motorcycle)')
match_object = batRegex.search("Batmobile lost a wheel")
print(match_object.group())

match_object = batRegex.search("Batmotorcycle lost a wheel")
print(match_object.group())

match_object = batRegex.search("Batmotorcycle lost a wheel")
print(match_object.group(1))  # to find which one


