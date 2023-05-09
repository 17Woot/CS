class Pet(object):
    def __init__(self, Name, Age, Number_of_legs):
        self.name = Name
        self.age = Age
        self.number_of_legs = Number_of_legs

    def description(self):
        return "Describe my self as : I am " + self.name + " and I am " + str(self.age) + " years old and I have " + str(self.number_of_legs) + " legs"

    def speak(self, sound):
        return f"Listen to me ... I am speaking: (sound)"


class Dog(Pet):
    def __init__(self, Name, Age, Number_of_legs, Breed):
        self.breed = Breed
        super().__init__(Name, Age, Number_of_legs)


    def speak(self):
        return " I am a dog I cannot speak, I mean ... wOOF ..woof?"

    def sniff(self):
        return "Sniffing"




if __name__ == "__main__":
    dog_1 = Dog("Sam",7,4,"German Shepherd")
    print(dog_1.description())
    print(dog_1.speak())
    print(dog_1.sniff())




