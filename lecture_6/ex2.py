class Cat:
    def __init__(self, name, legs, age) -> None:
        self.name = name
        self.age = age
        self.legs = legs
    
    def run(self):
        print(f'Cat {self.name} is running')

pi = Cat('Pi', 4, 2)
print(pi.name)