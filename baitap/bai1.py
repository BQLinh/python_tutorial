# Chu vi và diện tích hình chữ nhật có 2 cạnh a,b. a,b nhập từ bàn phím

a = int(input('Moi ban nhap so a: '))
b = int(input('Moi ban nhap so b: '))

def dien_tich(a,b):
    return a * b

def chu_vi(a,b):
    return (a + b)* 2

s = dien_tich(a,b)
print('Dien tich la:', s)

c = chu_vi(a, b)
print('Chu vi la: ',c)