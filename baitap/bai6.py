

def tim_so_nguyen_to(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(tim_so_nguyen_to(11))