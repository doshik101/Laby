s=input("Введите текст: ")
s2=s.split()
max=""
for i in range(len(s2)):
    w=len(s2[i])
    if w>len(max):
        max=s2[i]
print(max)
