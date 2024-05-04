with open("input.txt", "r") as input_f:
    lines = input_f.readlines()

request_lines= []
for line in lines:
    if len(line) > 20:
        request_lines.append(line)

with open("output.txt", "w") as output_f:
    for line in request_lines:
        output_f.write(line)