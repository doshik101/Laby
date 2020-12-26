krt=("Ruslan", "Rustam", "Rishat", "Arslan", "Rufat", "Rauf")
mas=["Sergey", "Fedor", "Ruslan", "Marusia", "Arslan", "Nikolay", "Rauf", "Maria"]
for i in mas:
    if i not in krt:
        print("Элемент, который есть в списке, но отсутствует в кортеже: ", i)
print()
