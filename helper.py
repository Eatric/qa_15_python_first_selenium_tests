from random import randint


class Helper:

    @staticmethod
    def generate_email():
        return f"kamil+{randint(0, 9999)}@ya.ru"