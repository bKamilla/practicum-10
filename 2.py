with open('input.txt', 'r') as input_file:
    l = input_file.readlines()

# Открываем файл для записи
with open('output.txt', 'w') as output_file:
    for line in l:
        if line.strip().startswith('A'):
            output_file.write(line)