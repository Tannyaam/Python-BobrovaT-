def save_input_data(data):
    file = open('file_culc.txt', 'a')
    file.write(f'{str(data)} = ')

def save_res(result):
    file = open('file_culc.txt', 'a')
    file.write(str(f'{result} \n'))