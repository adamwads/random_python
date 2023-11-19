
# QUESTION:
# Have the function AlphabetSoup(str) take the str string (lower or upper case) parameter being passed.
# Ignore all non-alphabetic characters like numbers and punctuation.
# Return the string with the letters in lowercase in alphabetical order (e.g. 2B3CA? becomes abc). 

def AlphabetSoup(s):
    # Remove non-alphabetic characters using regular expression, convert to lowercase,
    # then sort and join the characters
    import re
    return ''.join(sorted(re.sub('[^a-zA-Z]', '', s).lower()))

# # Example usage
# input = "2B3CA?"
# output = AlphabetSoup(input)

# Get input from the user
input = input("Enter a string: ")
output = AlphabetSoup(input)
print(output)  # Output: "abc"
