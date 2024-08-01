class Charsets:
    def __init__(self, composition):
        self.composition = composition

    def count(self):
        chars = self.composition
        quantity = len(chars)
        return quantity


lowercase_chset = Charsets("abcdefghijklmnopqrstuvwxyz")
uppercase_chset = Charsets("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits_chset = Charsets("0123456789")
special_chset = Charsets("~!@#$%^&*()")
master_chset = Charsets("")
