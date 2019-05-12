n= input("enter number")
n=int(n)
avg=0
sum=0
for num in range(0,n+1,1):
    sum=sum+num;

avg=sum/n

print("sum is:",sum,"avg is:",avg)