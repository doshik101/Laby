import random
k=random.randint(1,10)
print("Угадай число от 1 до 10")
n=0
while k!=n:
    s=str(input('Чтобы выйти, напишите Exit ' ))
    if s=='Exit' or s=='exit':
        break
    else:
        n=int(input(Введите число))
        if n>k:
            print('ваше больше задуманного')
        elif n<k:
            print('ваше число меньше задуманного')
        else:
            print('Вы угадали задуманное число!')
            break
            
