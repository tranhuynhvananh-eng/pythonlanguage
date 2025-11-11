n=int(input("nhập n :"))
list=[1,1]
if n==1 or n==0:
    print(list[n])
else :
    for i in range(2,n):
        list.append(list[i-1]+list[i-2])
    print(list[n-1])