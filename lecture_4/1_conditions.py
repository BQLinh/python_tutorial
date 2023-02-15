# if : nếu điều kiên này đúng => chạy code trong điều kiện này, nếu không sẽ chuyển sang kiểm tra điều kiện khác

# elif : nếu if ko sảy ra, và nhảy vào đk này

# else : nếu tất cả các đk khác ko xảy ra, code sẽ chạy ở đây


x = int(input('Nhap 1 so bat ki: '))

if x > 0:    
    print('X là 1 số dương')
elif x == 0:
    print('X bằng 0')
else:
    print('X là 1 số âm')

