class Pet(object):
    def __init__(self, Name, Age, Number_of_legs, price="none"):
        self.name = Name
        self.age = Age
        self.number_of_legs = Number_of_legs
        self.__price = price

    def description(self):
        return "Describe my self as : I am " + self.name + " and I am " + str(self.age) + " years old and I have " + str(self.number_of_legs) + " legs"

    def speak(self, sound):
        return f"Listen to me ... I am speaking: (sound)"

    def sleep(self):
        return "Sleeping silently"

    # setter and getter

    def set_price(self, p):
        self.price = p

    def get_price(self):
        return self.price


class Cat(Pet):
    def __init__(self, Name, Age, Number_of_legs, Breed):
        self.breed = Breed
        super().__init__(Name, Age, Number_of_legs)

    def sleep(self):
        return "Sleeping, not so silently"




