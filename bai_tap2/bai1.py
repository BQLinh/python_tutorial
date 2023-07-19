# s = 0

# for i in range(200, 301):
#     s += i


# print(s)

n = int(input("nhap n: "))
check = True
for i in range(2, n):
    if n % i == 0:
        print('X khong phai nguyen to')
        check = False
        break

if check == True:
    print('X la 1 so nguyen to')


def check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("nhap n: "))
x = check(n)
if x == True:
    print('X la so nguyen to')
else:
    print('X khong phai nguyen to')