try:
    with open('input.txt', 'r') as input_f:
        n = int(input_f.readline().strip())

        lines = input_f.readlines()

        if n == len(lines):
            result = "YES"
        else:
            result = "NO"

    with open('output.txt', 'w') as output_f:
        output_f.write(result)

except ValueError:
    print("ERROR: Первая строка должна содержать целое число.")
except Exception as e:
    print(f"Произошла ошибка: {e}")