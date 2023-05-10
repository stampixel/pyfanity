import pyfanity

# from pyfanity import example


print(pyfanity.add_one(12))

print(pyfanity.version)
print(pyfanity.get_version())

from pyfanity.replacements import default_character_replacements
from pyfanity.profanities import default_profanities
from pyfanity.pyfanity import Pyfanity

test_obj = Pyfanity(default_character_replacements, default_profanities)

print(test_obj.sanitize_string("asda()@@   $s@!#!$@#d", True))
