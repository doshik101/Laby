l = [-8, 8, 6.0, 5, 'строка', -3.1]
sum=0
for i in range(0,len(l),1):
    if type(l[i]) == int or type(l[i]) == float:
        sum=sum+l[i]
print(sum)
