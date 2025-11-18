def thapsangnhi(n):
    if n == 0:
        return "0"

    kq = ""
    while n > 0:
        kq = str(n % 2) + kq   
        n //= 2             
    return kq
so = int(input("Nhập số thập phân: "))
print("Dạng nhị phân:", thapsangnhi(so))