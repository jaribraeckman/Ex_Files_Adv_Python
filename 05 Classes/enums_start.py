# define enumerations using the Enum base class

from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # RED_DELICOUS = 1
    PEAR = auto()

def main():
    pass
    # TODO: enums have human-readable values and types
    # print(Fruit.APPLE)
    # print(type(Fruit.APPLE))
    # print(repr(Fruit.APPLE))

    # TODO: enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)
    print(Fruit.PEAR.name, Fruit.PEAR.value)

    # TODO: print the auto-generated value

    # TODO: enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])

if __name__ == "__main__":
    main()
