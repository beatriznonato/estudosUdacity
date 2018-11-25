class Parent():
    def __init__(self, lastName, eyeColor):
        print("Parent Constructor Called")
        self.lastName = lastName
        self.eyeColor = eyeColor

    def showInfo(self):
        print("Last Name - "+self.lastName)
        print("Eye Color - "+self.eyeColor)

class Child(Parent):
    def __init__(self, lastName, eyeColor, numberOfToys):
        print("Child Constructor Called")
        Parent.__init__(self, lastName, eyeColor)
        self.numberOfToys = numberOfToys

    def showInfo(self):
        print("Last Name - "+self.lastName)
        print("Eye Color - "+self.eyeColor)
        print("Number of toys - "+str(self.numberOfToys))

billyCyrus = Parent("Cyrus", "blue")
#billyCyrus.showInfo()

mileyCyrus = Child("Cyrus", "blue", "5")
mileyCyrus.showInfo()
