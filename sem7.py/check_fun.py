import functions

def check_function(data):
    # data = [int(data[i]) for i in range(len(data)) if data[i].isdigit()]
    index_func = 0
    for i in range(len(data)):
        if type(data[i]) != int:
            index_func = i
            break
    # if data[index_func] == '+':
    #     return functions.function_sum(int(data[index_func - 1]), int(data[index_func + 1]))
    # elif data[index_func] == '-':
    #     return functions.function_sub(int(data[index_func - 1]), int(data[index_func + 1]))
    # elif data[index_func] == '*':
    #     return functions.function_mult(int(data[index_func - 1]), int(data[index_func + 1]))
    # elif data[index_func] == '/':
    #     return functions.function_div(int(data[index_func - 1]), int(data[index_func + 1]))
    match data[index_func]:
        case '+':
            return functions.function_sum(int(data[index_func - 1]), int(data[index_func + 1]))
        case '-':
            return functions.function_sub(int(data[index_func - 1]), int(data[index_func + 1]))
        case '*':
            return functions.function_mult(int(data[index_func - 1]), int(data[index_func + 1]))
        case '/':
            return functions.function_div(int(data[index_func - 1]), int(data[index_func + 1]))