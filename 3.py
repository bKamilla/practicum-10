with open('input.txt', 'r') as input_:
    lines = input_.readlines() 
result_word = ''.join([line[0] for line in lines])
with open('output.txt', 'w') as output_:
    output_.write(result_word)