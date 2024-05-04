with open('input.txt', 'r') as f:
    data = f.read()
data_upper = data.upper()
with open('output.txt', 'w') as f:
    f.write(data_upper)