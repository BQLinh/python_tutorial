class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def run(self):
        print(self.name + ' can run')

class BlackHuman(Human):
    def __init__(self, name, ge) -> None:
        super().__init__(name, ge)

class WhiteHuman(Human):
    pass


linh = BlackHuman('linh', 12)
linh.run()


tom = WhiteHuman('Ron', 34)
