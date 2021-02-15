import re
import pyperclip
# ? -> zero or one
# * -> zero or more
# + -> one or more
# {x} -> exactly x times
# {x,y} -> at least x at most y

# Common Character Classes
# \d any numeric digit from 0 to 9.
# \w any letter, numeric digit, or the underscore character 'word'
# \s any space, tab, or newline character 'space'
# Capital version are opposites. \D Any character that is NOT a numeric digit from 0 to 9.

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
(\+(\d\d\d)?)?      # country code
\s*                 # zero or more spaces
\d\s*\d\d           # area code
\s*
\d\d\s*\d\d\s*\d\d  # subscriber number
)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+          # name part
@                        # @ symbol
[a-zA-Z0-9_.+]+          # domain name part
''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
extractedPhones = phoneRegex.findall(text)
extractedEmails = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNum in extractedPhones:
    allPhoneNumbers.append(phoneNum[0])

allEmails = []
for email in extractedEmails:
    allEmails.append(email)

# TODO: Copy the extracted email/phone to the clipboard.
allPhoneNumbers = '\n'.join(allPhoneNumbers)
allEmails = '\n'.join(allEmails)
all = 'PHONE NUMBERS:\n' + allPhoneNumbers + '\nEMAILS:\n' + allEmails
pyperclip.copy(all)

