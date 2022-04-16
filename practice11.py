#1 Сформувати функцію, що буде обчислювати факторіал заданого користувачем натурального числа n.
n = int(input('Enter number : '))
fact=1
for i in range(2,n+1):
    fact=fact*i
print("The factorial of ",n," is: ",fact)

#2 Сформувати функцію для обчислення цифрового кореню натурального числа.
n = int(input('Enter number : '))

s = str(n)
while len(s) > 1:
    n = 0;
    for i in s:
        n += int(i)
    s = str(n)
print('Digital root =' , s)


