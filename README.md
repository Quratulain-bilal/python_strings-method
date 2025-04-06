
# Python String Methods Examples

This repository contains comprehensive examples of Python's built-in string methods, demonstrating their functionality with clear examples.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [String Methods Examples](#string-methods-examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

No installation required - these examples use Python's built-in string methods.

```bash
# Just ensure you have Python installed
python --version
# Python 3.6+ recommended
Usage
Clone this repository

Run the Python script:

bash
Copy
python string_methods.py
View the output to understand each string method's behavior

String Methods Examples
The script demonstrates 42 essential Python string methods:

Basic Modification
capitalize(): First character uppercase, rest lowercase

lower()/upper(): Case conversion

title(): Title case conversion

swapcase(): Swap cases

Searching and Checking
find()/rfind(): Locate substrings

index()/rindex(): Locate substrings (raises error if not found)

startswith()/endswith(): Check prefixes/suffixes

isalpha()/isnumeric(): Character type checks

Formatting
center(): Center string with padding

ljust()/rjust(): Left/right justify

zfill(): Zero-padding

format(): String formatting

Splitting and Joining
split()/rsplit(): Split strings

partition()/rpartition(): Split at first/last occurrence

join(): Combine iterables

Cleaning
strip()/lstrip()/rstrip(): Remove whitespace

replace(): Replace substrings

Encoding
encode(): Convert to bytes

casefold(): Aggressive lowercase

Example Code Snippet
python
Copy
# Example 1: capitalize()
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

# Example 2: casefold()
text = "HÄLLO"
print(text.casefold())    # Output: "hällo"

# Example 3: count()
text = "banana"
print(text.count('a'))    # Output: 3
Contributing
Contributions welcome! Please:

Fork the repository

Create your feature branch

Commit your changes

Push to the branch

Open a pull request

License
This project is licensed under the MIT License - see the LICENSE file for details.

