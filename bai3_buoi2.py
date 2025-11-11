n=int(input("nhập số phần tử:"))
s=0
list=[]
for i in range(n):
    a=int(input())
    list.append(a)
for i in list:
    s=s+i
print ("tổng là:",s)

