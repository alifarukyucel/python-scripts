import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob."))

namesRegex.sub("CLASSIFIED", "Agent Alice gave the secret documents to Agent Bob.")  # substitution

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob."))
namesRegex.sub(r"Agent \1****", "Agent Alice gave the secret documents to Agent Bob.")  # \1 means use group 1

re.compile(r'''
(\d\d\d-)|  # area code without parens
(\(\d\d\d\)) # -or- area code with parens and no dash
\d\d\d      # first 3 digits
-
\d\d\d\d    # last 4 digits
''', re.VERBOSE)

