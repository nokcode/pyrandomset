pyrandomset
===========
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyrandomset)
![GitHub tag (latest SemVer pre-release)](https://img.shields.io/github/v/tag/nokcode/pyrandomset?include_prereleases&label=version)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyrandomset)


Generate random characters based on character set.

Characters sets
---------------

Placeholder | Type                              | Character Set
----------- | --------------------------------- | ----------------------------------------------------------------
a           | Lower-Case Alphanumeric           | abcdefghijklmnopqrstuvwxyz 0123456789
A           | Mixed-Case Alphanumeric           | ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789
U           | Upper-Case Alphanumeric           | ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789
d           | Digit                             | 0123456789
h           | Lower-Case Hex Character          | 0123456789 abcdef
H           | Upper-Case Hex Character          | 0123456789 ABCDEF
l           | Lower-Case Letter                 | abcdefghijklmnopqrstuvwxyz
L           | Mixed-Case Letter                 | ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz
u           | Upper-Case Letter                 | ABCDEFGHIJKLMNOPQRSTUVWXYZ
v           | Lower-Case Vowel                  | aeiou
v           | Mixed-Case Vowel                  | AEIOU aeiou
Z           | Upper-Case Vowel                  | AEIOU
c           | Lower-Case Consonant              | bcdfghjklmnpqrstvwxyz
C           | Mixed-Case Consonant              | BCDFGHJKLMNPQRSTVWXYZ bcdfghjklmnpqrstvwxyz
z           | Upper-Case Consonant              | BCDFGHJKLMNPQRSTVWXYZ
p           | Punctuation                       | ,.;:
b           | Bracket                           | ()[]{}<>
s           | Printable 7-Bit Special Character | !\"#$%&'()*+,-./:;<=>?@\[\\\]^_`{\|}~
\           | Escape (Fixed Char)               | Use following character as is.

Example
-------

```python
from pyrandomset import generate

# Generate a ten-character alphanumeric with at least one lowercase character, 
# at least one uppercase character, and at least three digits:
print(generate("AAAAAluddd", shuffle=True))

# Generate three unique random syllable:
print(generate("zv\ zv\ zv", repeat=False))

# Generate 1 character from custom set, three uppercase letters, 
# three lowercase letters and two digits:
print(generate("?uuullldd", { "?": "!@#$%" }))
```
