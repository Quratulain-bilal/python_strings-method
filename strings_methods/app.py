# Example 1: capitalize() - Converts the first character to uppercase and rest to lowercase
text1 = "hello world"
print(text1.capitalize())  # Output: "Hello world"

# Example 2: casefold() - Converts string to casefolded (aggressive lowercase) for caseless matching
text2 = "HÄLLO"
print(text2.casefold())    # Output: "hällo"

# Example 3: center() - Centers the string in a specified width, filling with spaces (or specified char)
text3 = "Python"
print(text3.center(10, '-'))  # Output: "--Python--"

# Example 4: count() - Returns the number of times a substring appears in the string
text4 = "banana"
print(text4.count('a'))      # Output: 3

# Example 5: encode() - Returns an encoded version of the string (default is UTF-8)
text5 = "pythön"
print(text5.encode())        # Output: b'pyth\xc3\xb6n'

# Example 6: endswith() - Returns True if string ends with the specified suffix
text6 = "Hello, world!"
print(text6.endswith("!"))   # Output: True

# Example 7: expandtabs() - Replaces tab characters with spaces (default 8 spaces per tab)
text7 = "H\te\tl\tl\to"
print(text7.expandtabs(2))  # Output: "H e l l o"

# Example 8: find() - Returns lowest index of substring (or -1 if not found)
text8 = "Have a nice day"
print(text8.find("nice"))    # Output: 7

# Example 9: format() - Formats specified values in string
text9 = "My name is {} and I'm {} years old"
print(text9.format("Ali", 25))  # Output: "My name is Ali and I'm 25 years old"

# Example 10: index() - Like find() but raises ValueError if substring not found
text10 = "Python programming"
print(text10.index("pro"))   # Output: 7

# Example 11: isalnum() - Returns True if all characters are alphanumeric
text11 = "Python3"
print(text11.isalnum())      # Output: True

# Example 12: isalpha() - Returns True if all characters are alphabetic
text12 = "Python"
print(text12.isalpha())      # Output: True

# Example 13: isdecimal() - Returns True if all characters are decimal numbers
text13 = "1234"
print(text13.isdecimal())    # Output: True

# Example 14: isdigit() - Returns True if all characters are digits
text14 = "²345"
print(text14.isdigit())      # Output: True

# Example 15: isidentifier() - Returns True if string is valid Python identifier
text15 = "var_name"
print(text15.isidentifier()) # Output: True

# Example 16: islower() - Returns True if all characters are lowercase
text16 = "hello"
print(text16.islower())      # Output: True

# Example 17: isnumeric() - Returns True if all characters are numeric
text17 = "½¾"
print(text17.isnumeric())    # Output: True

# Example 18: isprintable() - Returns True if all characters are printable
text18 = "Hello\n"
print(text18.isprintable())  # Output: False (because of \n)

# Example 19: isspace() - Returns True if all characters are whitespace
text19 = "   "
print(text19.isspace())      # Output: True

# Example 20: istitle() - Returns True if string follows title case rules
text20 = "This Is Title"
print(text20.istitle())      # Output: True

# Example 21: isupper() - Returns True if all characters are uppercase
text21 = "HELLO"
print(text21.isupper())      # Output: True

# Example 22: join() - Joins elements of iterable with string as separator
words = ["Python", "is", "great"]
print(" ".join(words))       # Output: "Python is great"

# Example 23: ljust() - Returns left-justified string of given width
text23 = "Python"
print(text23.ljust(10, '*')) # Output: "Python****"

# Example 24: lower() - Converts string to lowercase
text24 = "HELLO"
print(text24.lower())        # Output: "hello"

# Example 25: lstrip() - Removes leading whitespace (or specified chars)
text25 = "   Python"
print(text25.lstrip())       # Output: "Python"

# Example 26: maketrans() and translate() - Character translation
trans_table = str.maketrans("aeiou", "12345")
text26 = "apple"
print(text26.translate(trans_table))  # Output: "1ppl2"

# Example 27: partition() - Splits string at first occurrence of separator
text27 = "Python is fun"
print(text27.partition("is"))  # Output: ('Python ', 'is', ' fun')

# Example 28: replace() - Replaces substring with another string
text28 = "I like Java"
print(text28.replace("Java", "Python"))  # Output: "I like Python"

# Example 29: rfind() - Like find() but searches from right
text29 = "Hello world, hello universe"
print(text29.rfind("hello"))  # Output: 13

# Example 30: rindex() - Like index() but searches from right
text30 = "Hello world, hello universe"
print(text30.rindex("hello"))  # Output: 13

# Example 31: rjust() - Returns right-justified string of given width
text31 = "Python"
print(text31.rjust(10, '-'))  # Output: "----Python"

# Example 32: rpartition() - Like partition() but searches from right
text32 = "Python is fun is great"
print(text32.rpartition("is"))  # Output: ('Python is fun ', 'is', ' great')

# Example 33: rsplit() - Splits string from right at separator
text33 = "apple,banana,cherry"
print(text33.rsplit(",", 1))  # Output: ['apple,banana', 'cherry']

# Example 34: rstrip() - Removes trailing whitespace (or specified chars)
text34 = "Python   "
print(text34.rstrip())        # Output: "Python"

# Example 35: split() - Splits string at separator into list
text35 = "Python is awesome"
print(text35.split())         # Output: ['Python', 'is', 'awesome']

# Example 36: splitlines() - Splits string at line breaks
text36 = "Hello\nWorld\n!"
print(text36.splitlines())    # Output: ['Hello', 'World', '!']

# Example 37: startswith() - Returns True if string starts with prefix
text37 = "Python programming"
print(text37.startswith("Py"))  # Output: True

# Example 38: strip() - Removes leading and trailing whitespace (or specified chars)
text38 = "   Python   "
print(text38.strip())         # Output: "Python"

# Example 39: swapcase() - Swaps case of all characters
text39 = "Hello World"
print(text39.swapcase())      # Output: "hELLO wORLD"

# Example 40: title() - Converts string to title case
text40 = "python programming"
print(text40.title())         # Output: "Python Programming"

# Example 41: upper() - Converts string to uppercase
text41 = "hello"
print(text41.upper())         # Output: "HELLO"

# Example 42: zfill() - Fills string with zeros to specified width
text42 = "42"
print(text42.zfill(5))        # Output: "00042"