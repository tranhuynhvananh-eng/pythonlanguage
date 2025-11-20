import math 
n=int(input("nhập số nguyên n:"))
s=0
p=int(math.sqrt(n))
if n<2:
    print(n,"không phải là số nguyên tố")
else :
    for i in range(2,p):
        if n//i==0: #chỗ này là % mới là chia lấy dư, // là chia lấy số nguyên
            s=s+1 #nếu đã có số chia hết thì dừng luôn không cần đếm, sẽ dùng return
if s>=1:
    print(n,"không phải là số nguyên tố")
else: 
    print(n,"là số nguyên tố")
