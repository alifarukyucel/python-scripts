import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall("415-123-8849 and 726-849-2020"))  # if you use groups it returns a list of tuples

# Common Character Classes
# \d any numeric digit from 0 to 9.
# \w any letter, numeric digit, or the underscore character 'word'
# \s any space, tab, or newline character 'space'
# Capital version are opposites. \D Any character that is NOT a numeric digit from 0 to 9.

lyrics = '''On the 12th day of Christmas my true love sent to me
12 drummers drumming
11 pipers piping
10 lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves, and
A partridge in a pear treee'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))


# Creating your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall("Robocop eats baby food."))
print(doubleVowelRegex.findall("Robocop eats baby food."))

consonantsRegex = re.compile(r'[^aeiouAEIOU]')  # ^ means NOT
print(consonantsRegex.findall("Robocop eats baby food."))
