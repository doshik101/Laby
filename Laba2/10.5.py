a=int(input('Введите число '))
a1=a
sum=0
n=0
while a1!=0:
    a1=a1//10
    n=n+1
for i in range(n-1):
    b=a%10
    if b%2==1:
        sum=sum+b**2
    a=a//10
print(sum)
