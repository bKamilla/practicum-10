# Открываем файл input.txt для чтения
with open('input.txt', 'r') as f:
    data = f.read()

# Преобразуем данные к верхнему регистру
data_upper = data.upper()

# Открываем файл output.txt для записи
with open('output.txt', 'w') as f:
    f.write(data_upper)