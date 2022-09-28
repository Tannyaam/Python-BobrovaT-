data = []

def get_data():
    global data
    data = input('Введите выражение ')
    return data

def trans_to_list(data):
    data = data.split()
    for i in range(len(data)):
        data[i] = int(data[i]) if data[i].isdigit() else data[i]
    return data

def return_result(result):
    print(f'Результат = {result}')