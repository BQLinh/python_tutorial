# variable: biến, tức là giá trị có thể thay đổi được. ví dụ:
x = 1 # ban đầu giá trị của x = 1
x = 3 # ta thay đổi giá trị của x đi

# tại sao lại cần biến: để chúng ta lưu trữ các giá trị vào các biến này
# và phục vụ cho tính toán, viết các chức năng. ví dụ:

def total(a, b, c): 
    total = a + b + c
    print(total) 
    return total 

print(total(2,3,4))

#1. trong trường hợp này, nếu chúng ta ko tạo ra biến a,b,c thì muốn tính 1+2+3 chúng ra sẽ phải viết ra 1 hàm mới. ví dụ:
def total_123():
    total = 1 + 2 + 3
    print(total)
    return total
# tương tự nếu muốn tính tổng 4 + 5 + 6 ta lại phải viết 1 hàm nữa:
def total_456():
    total = 4 + 5 + 6
    print(total)
    return total

# còn với hàm total() chúng ta có thể truyển 3 số bất kì để tính tồng mà chỉ sử dụng hàm total thôi. 
# ví dụ muốn tính tổng 4+5+6 ta có:
total(4,5,6)


#2. nếu chúng ta không tạo ra biến total thì sao: chúng ta sẽ phải viết lại a + b + c 2 lần. Kết quả:

def total(a, b, c): 
    # total = a + b + c
    print(a + b +c) 
    return a +b +c 

# việc lặp lại code thể này có thể gây mất thời gian và nhầm lẫn. ví dự như ta muốn tính 1 phép tính rất phức tạp
# ta sẽ phải viết lại nhiều lần, và rất mất thời gian. ví dụ như

# sử dụng biến result
def calculate(a,b,c,d,e):
    result = a * a + a - b + 2*c -d/2 + e*e
    print(result)
    print(result * 2)
    print(result + 2)
    print(result * result)

# không sử dụng biến result
def calculate(a,b,c,d,e):
    result = a * a + a - b + 2*c -d/2 + e*e
    print(result)
    print((a * a + a - b + 2*c -d/2 + e*e) * 2)
    print((a * a + a - b + 2*c -d/2 + e*e) + 2)
    print((a * a + a - b + 2*c -d/2 + e*e) * (a * a + a - b + 2*c -d/2 + e*e))


# biến giống như 1 ngôi nhà(1 cái hộp....):
# - tên biến: giống như địa chỉ của 1 ngôi nhà, dùng để gọi, để xác định
# - giá trị: giống như những gì bên trong nhà đó chứa


# các loại kiểu hay dùng
name = 'linh' # kiểu string

age = 22 # kiểu số

is_true = False # kiểu boolean

# để kiểm tra kiểu dữ liệu của biến dùng hàm type()

# cách đặt tên biến