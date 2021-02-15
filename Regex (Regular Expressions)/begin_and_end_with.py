import re
beginsWithHelloRegex = re.compile(r"^Hello")  # ^ means start at beginning
print(beginsWithHelloRegex.search("Hello there!").group())

endsWithRegex = re.compile("world!$")
print(endsWithRegex.findall("Hello world!"))

allDigitsRegex = re.compile(r"^\d+$")  # both begins and ends with digits
print(allDigitsRegex.findall("1274617864716248"))
print(allDigitsRegex.findall("27163781c01293018"))

atRegex = re.compile(r".at")  # . means any character
print(atRegex.findall("The cat in the hat sat on the flat mat"))

atRegex = re.compile(r".{1,2}at")
print(atRegex.findall("The cat in the hat sat on the flat mat"))

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
# .* means any number of any characters (since * means 0 or more) (except spaces, newlines and tabs)
print(nameRegex.findall("First Name: Ali Faruk Last Name: Yucel"))

# .* is greedy
# .*? is non-greedy

prime = "Serbe the public trust.\nProtect the innocent.\nUphold the law."
dotStar = re.compile(r".*")
print(dotStar.search(prime).group())  # includes until a newline character
dotStar = re.compile(r".*", re.DOTALL)  # EVERYTHING
print(dotStar.search(prime).group())

vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelRegex.findall("Robocop EAts baby food."))


