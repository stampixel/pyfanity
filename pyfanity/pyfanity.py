"""
Main file
"""

from replacements import default_character_replacements
from profanities import default_profanities


class Pyfanity:
    def __init__(self):
        self.sanitize_leetspeak = True
        self.sanitize_special_char = True

    def sanitize_string(self, s: str, remember_original_indexes: bool) -> str:
        s = s.lower()
        if self.sanitize_leetspeak and self.sanitize_special_char and not remember_original_indexes:
            s.replace("()", " ")

    def get_profanity(self, s: str) -> str:
        pass

    def isprofane(self, s: str) -> bool:
        pass
