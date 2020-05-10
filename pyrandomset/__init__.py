"""Create random characters based on character set.
"""

__all__ = ["generate"]

from secrets import choice
import random
import string

lowercase_vowels = "aeiou"
uppercase_vowels = "AEIOU"
lowercase_consonants = "bcdfghjklmnpqrstvwxyz"
uppercase_consonants = "BCDFGHJKLMNPQRSTVWXYZ"
digits = "0123456789"
lowercase_hex = digits + "abcdef"
uppercase_hex = digits + "ABCDEF"
punctuation = ",.;:"
bracket = "()[]\{\}<>"
printable = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

builtin_sets = {
    'a': lowercase_vowels + lowercase_consonants + digits,
    'A': lowercase_vowels + uppercase_vowels + lowercase_consonants + uppercase_consonants + digits,
    'U': uppercase_vowels + uppercase_consonants + digits,
    'd': digits,
    'h': lowercase_hex,
    'H': uppercase_hex,
    'l': lowercase_vowels + lowercase_consonants,
    'L': lowercase_vowels + lowercase_consonants + uppercase_vowels + uppercase_consonants,
    'u': uppercase_vowels + uppercase_consonants,
    'v': lowercase_vowels,
    'V': lowercase_vowels + uppercase_vowels,
    'Z': uppercase_vowels,
    'c': lowercase_consonants,
    'C': lowercase_consonants + uppercase_consonants,
    'z': uppercase_consonants,
    'p': punctuation,
    'b': bracket,
    's': printable
}

class PyRandomSetException(BaseException):
    pass

def generate(pattern, sets={}, shuffle=False, repeat=True):
    sets = { **sets, **builtin_sets }
    placeholders = ''.join(key for key in sets.keys())
    generated = []
    i = 0
    while i < len(pattern):
        if pattern[i] in placeholders:
            if repeat:
                generated.append(choice(sets[pattern[i]]))
            else:
                arr = [char for char in sets[pattern[i]] if char not in generated]
                if len(arr) > 0:
                    generated.append(choice(arr))
        elif pattern[i] == '\\':
            generated.append(pattern[i + 1])
            i += 2
            continue
        else:
            raise PyRandomSetException(
                f"No support for placeholder '{pattern[i]}' in pattern '{pattern}'")
        i += 1
    if shuffle: 
        random.shuffle(generated) 
    return ''.join(generated)
