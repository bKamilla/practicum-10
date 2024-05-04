with open("input.txt", "r") as f_in:
    data = f_in.read().splitlines()

with open("output.txt", "w") as f_out:
    for i in range(0, len(data), 30):
        month = data[i:i+30]
        avg = sum(map(int, month)) // 30
        f_out.write(str(avg) + "\n")