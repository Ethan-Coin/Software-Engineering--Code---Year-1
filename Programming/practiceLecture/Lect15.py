from enum import Enum


class Mood(Enum):

    HAPPY = "happy"
    SAD = "sad"
    ANNOYED = "annoyed"


class Dog:
    def __init__(self, name):
        self.name = name
        self.mood = Mood.HAPPY


class DogKennel:
    def __init__(self):
        self.dogs = []

    def addDog(self, dog):
        self.dogs.append(dog)

    def updateMood(self, name, newMood):
        for dog in self.dogs:
            if dog.name == name:
                dog.mood = newMood
                return

    def __str__(self):
        output = ""
        for dog in self.dogs:
            output += F"\n{dog.name} {dog.mood.value}"
        return output


def main():
    dog = Dog("Guy")
    dog1 = Dog("Rus")
    dogs = DogKennel()
    dogs.addDog(dog)
    dogs.addDog(dog1)
    dogs.updateMood("Rus", Mood.SAD)
    print(dogs)


main()
