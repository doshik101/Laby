s=input("Введите текст ")
ls=[]
k=0
s1=0
for i in s:
    if i in '1234567890':
        ls.append(int(i))
        k=k+1
        s1=s1+int(i)
print("Все цифры:")
print(ls)
print("Количество:")
print(k)
print("Сумма: ")
print(s1)
print("Максимум: ")
print(max(ls))
