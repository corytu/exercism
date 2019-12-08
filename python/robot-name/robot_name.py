import random
import string

ascii_uppercases = list(string.ascii_uppercase)
digits = list(string.digits)

class Robot:

    used_names = set()

    def __init__(self):
        self.reset()

    @property
    def name(self):
        return self._name

    def reset(self):
        while True:
            proposed_name = "".join(random.choices(ascii_uppercases, k=2) + random.choices(digits, k=3))
            if proposed_name not in self.used_names:
                self.used_names.add(proposed_name)
                self._name = proposed_name
                break
