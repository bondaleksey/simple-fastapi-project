class Flower:
    def __init__(self, name="Kaktus", age=25, values=("1", "2", "3")):
        self.name = name
        self.age = age
        self.values = values

    def print_flower(self):
        print(
            f"Here we have:\nname = {self.name}\nage={self.age}\nvalues={self.values}"
        )
