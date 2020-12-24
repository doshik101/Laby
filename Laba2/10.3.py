n=int(input('Введите количество элементов в списке '))
L=list();
for i in range(0,n,1):
    x=int(input('Введите элемент списка '))
    L.append(x)
print(L)
for i in range(n//2):
    t=L[i]
    L[i]=L[n//2+i]
    L[n//2+i]=t
print(L)
