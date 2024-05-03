fname = input() 
try:
    with open (fname) as f:
        num1 = int(f.readline())
        num2 = int(f.readline())
        num3 = int(f.readline())

    result = num1 / num2 + num3

except ValueError:
    print("Ошибка: В файле input.txt должны быть целые числа.")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль.")
else:
    with open("output.txt", "w") as output:
        output.write(str(result))`