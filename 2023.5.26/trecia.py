class Student:
    def __init__(self, name, credits):
        self.name = name
        self.credits = self._validate_credits(credits)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, value):
        self._credits = self._validate_credits(value)

    def print_info(self):
        print(f"Studento vardas: {self.name}")
        print(f"Kreditai: {self.credits}")

    def _validate_credits(self, credits):
        if credits <= 0:
            return 0
        elif credits >= 30:
            return 30
        else:
            return credits


s = Student("Mantas", -5)
s.print_info()
