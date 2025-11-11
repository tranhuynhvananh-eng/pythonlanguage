import math 
n=int(input("nhập số nguyên n:"))
s=0
p=int(math.sqrt(n))
if n<2:
    print(n,"không phải là số nguyên tố")
else :
    for i in range(2,p):
        if n//i==0:
            s=s+1
if s>=1:
    print(n,"không phải là số nguyên tố")
else: 
    print(n,"là số nguyên tố")
