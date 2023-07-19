
    
class Human:
    def __init__(self, my_name, my_age):
        self.name = my_name
        self.age = my_age
        self.eyes = None

    def speak(self):
        print('hello my name is', self.name)

    def run(self, speed):
        print(self.name, 'is running with speed', speed)


linh = Human('linh', 24)


print(linh.eyes)

linh.eyes = 'Black'

print(linh.eyes)

linh.age = 25
print(linh.age)
# minh = Human('minh', 2)
# minh.run('100km/h')

# minh.speak()

# tạo 1 class Car có các thuộc tính: name, number_of_wheels, color và các phương thức là run, start, get_color
# phương thức run sẽ có tham số là speed => in ra đối tượng đó chạy bn km/h
# phương thức start sẽ in ra là => object.name is running
# phương thức get_color sẽ in ra màu của xe