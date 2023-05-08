"""
Main file
"""


class Pyfanity:
    def __init__(self):
        self.ignoreLeetspeak = False

    def sanitize_string(self) -> str:
        pass

    def get_profanity(self, s: str) -> str:
        pass

    def isprofane(self, s: str) -> bool:
        return len(self.get_Profanity()) > 0
