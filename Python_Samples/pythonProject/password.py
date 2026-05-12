import string
import random


class Password:
    def __init__(self, size=16, low=True, upp=True, spe=True, num=True):
        self.__special = "!#$%&()/=*+@-_[].,;:"
        self.__digit = string.digits
        self.__lower = string.ascii_lowercase
        self.__upper = string.ascii_uppercase
        self.password = ""
        self.all_letters = ""
        self.size = size
        self.low = low
        self.upp = upp
        self.spe = spe
        self.num = num

    # Private method
    def letter_lower(self):
        return self.__lower[random.randint(0, len(self.__lower)-1)]

    def letter_upper(self):
        return self.__upper[random.randint(0, len(self.__upper)-1)]

    def letter_digit(self):
        return self.__digit[random.randint(0, len(self.__digit) - 1)]

    def letter_special(self):
        return self.__special[random.randint(0, len(self.__special) - 1)]

    def letters(self):
        if self.low:
            self.all_letters = self.all_letters + self.__lower
        if self.upp:
            self.all_letters = self.all_letters + self.__upper
        if self.spe:
            self.all_letters = self.all_letters + self.__special
        if self.num:
            self.all_letters = self.all_letters + self.__digit
        return self.all_letters[random.randint(0, len(self.all_letters) - 1)]

    def make_pass(self):
        index = 0
        if self.low:
            self.password = self.password + self.letter_lower()
            index += 1

        if self.upp:
            self.password = self.password + self.letter_upper()
            index += 1

        if self.num:
            self.password = self.password + self.letter_digit()
            index += 1

        if self.spe:
            self.password = self.password + self.letter_special()
            index += 1

        for index2 in range(index, self.size):
            self.password = self.password + self.letters()

        return self.password


p = Password(size=20)
con = p.make_pass()
print(con)

