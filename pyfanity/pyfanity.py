"""
Main file
"""
from typing import Tuple, List

from pyfanity.replacements import default_character_replacements
from pyfanity.profanities import default_profanities


class Pyfanity:
    def __init__(self, default_character_replacements, default_profanities):
        self.default_profanities = default_profanities
        self.default_character_replacements = default_character_replacements
        self.sanitize_leetspeak = True
        self.sanitize_special_char = True
        self.sanitize_accents = False
        self.sanitize_spaces = True

    def sanitize_string(self, s: str, remember_original_indexes: bool) -> tuple[str, list[int]]:
        """
        Sanitizes the string, applying leetspeak and special character replacements.

        :param s: str
        :param remember_original_indexes: bool
        :return: tuple[str, list[int]]
        """
        s = s.lower()
        if self.sanitize_leetspeak and self.sanitize_special_char and not remember_original_indexes:
            s.replace("()", "o")
        temp_s = ""
        for char in s:
            if char in self.default_character_replacements:
                if self.sanitize_special_char and self.default_character_replacements[char] == " ":
                    temp_s += self.default_character_replacements[char]
                    continue
                elif self.sanitize_leetspeak and self.default_character_replacements[char] != " ":
                    temp_s += self.default_character_replacements[char]
                    continue
            temp_s += char
        s = temp_s
        s = self.remove_accents(s) if self.sanitize_accents == True else s
        original_indexes = []

        # Keeps track of original indexes of characters, preventing errors
        if remember_original_indexes:
            for i in range(len(s)):
                if s[i] != " " or not self.sanitize_spaces:
                    original_indexes.append(i)

        if self.sanitize_spaces:
            s = s.replace(" ", "")
        return s, original_indexes

    def get_profanity(self, s: str) -> str:
        s, _ = self.sanitize_string(s, False)
        for word in default_profanities:
            if word == s:
                return word
        return ""

    def is_profane(self, s: str) -> bool:
        return len(self.get_profanity(s)) > 0

    def remove_accents(self, s: str) -> str:
        pass
