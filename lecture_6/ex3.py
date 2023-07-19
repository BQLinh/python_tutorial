

class Human:
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        self.height = 150
    
    def run(self, v):
        print(f'{self.name} is running with {v} km/h!')

hai = Human('Hai', 25)
linh = Human('linh', 25)
ta = Human('Tu Anh', 24)

linh.run(50)
print(linh.height)

# tạo ra 5 đối tượng học sinh sau đó thêm vào 1 list 
# in ra màn hình ID và tên của các học sinh trong list

# tạo ra 5 đối tượng học sinh sau đó thêm vào 1 list bằng lệnh insert và append

# tạo thêm 1 list mới có 2 phần HS
# dùng lệnh extend để thêm list mới này vào list HS cũ
# dùng lệnh remove và pop để xoá 2 HS tuỳ ý