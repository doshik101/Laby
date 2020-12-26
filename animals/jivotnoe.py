class Animal:
    name=''
    def Eat(self):
        print("Я кушою");

    def setName(self, newName):
        self.name=newName

    def getName(self):
        return self.name

    def Noize(self):
        print(self.name+ 'Мррррряу')

    def __init__(self, newName):
        self.name=newName
        print('Родилось животное ', self.name)

Cat=Animal('Пушок')
print(Cat.getName())

Cat.setName('Пуша')
print(Cat.getName())

Cat.Eat()
Cat.Noize()
