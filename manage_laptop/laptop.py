class Laptop:
    def __init__(self, id, name, code, cost,link, img):
        self.id = id
        self.name = name
        self.code = code
        self.cost = cost
        self.link = link
        self.img = img

    def __str__(self) -> str:
        return f'{self.code}: {self.name}, {self.cost}'