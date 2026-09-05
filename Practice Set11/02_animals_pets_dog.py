class Animals:
    pass

class pets(Animals):
    pass

class dog(pets):

    @staticmethod
    def bark():
        print("Bow Bow......")

d = dog()
d.bark()