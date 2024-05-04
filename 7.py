with open("input.txt", "r") as f:
    lines = f.readlines()

request_lines = []
for line in lines:
    if "100" not in line:
        request_lines.append(line)

with open("input.txt", "w") as f:
    for line in request_lines:
        f.write(line)