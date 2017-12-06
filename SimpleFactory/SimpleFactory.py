import abc

class Cornflakes:
    """
    Cornflakes metaclass which is equivalent to a Java interface
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getMilk(self):
        pass

    @abc.abstractmethod
    def getCornflakes(self):
        pass


class Chocos(Cornflakes):
    """
    Chocos inherits Cornflakes and overrides its methods
    """
    def __init__(self, milk, cornflakes):
        self.milk = milk
        self.cornflakes = cornflakes

    def getCornflakes(self):
        return self.cornflakes

    def getMilk(self):
        return self.milk



class MakeChocos:
    """
    Class that handles creation of an object for the client
    """

    @classmethod
    def makeChocos(self, milk, cornflakes):
        chocos = Chocos(milk, cornflakes)
        return chocos



if __name__ == "__main__":
    chocos_bowl = MakeChocos.makeChocos(100, 100)
    print("Add Milk: {0} ml".format(chocos_bowl.milk))
    print ("Add Cornflakes:  {0} g".format(chocos_bowl.cornflakes))

