# Hàm không nhận giá trị đầu vào, và ko trả về kết quả
def hello():
    print('hello')

# Hàm nhận giá trị đầu vào: giá trị này gọi là tham sô, ko trả về kq
def hello(name):
    print('hello', name)

# Hàm nhận giá trị đầu vào (gọi là tham số), và trả về kq
def hello(name):
    return name
