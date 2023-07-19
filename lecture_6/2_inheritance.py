class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def run(self):
        print(self.name + ' can run')

class BlackHuman(Human):
    def __init__(self, name, age) -> None:
        self.color = 'black'
        # self.name = name
        # self.age = age
        super().__init__(name, age)
    
    def speak(self):
        print(f'{self.name} is speacking')

class WhiteHuman(Human):

    def run(self):
        print('***********')


linh = BlackHuman('linh', 12)
# print(linh.color)
# print(linh.name)
# print(linh.age)
# linh.run()

# linh.speak()

tom = WhiteHuman('Ron', 34)
print(tom.name)
tom.run()

for i in range(10):
    if i > 5:
        pass
    else:
        print(i)