import check_fun
import gui
import check_fun
import database

def button_click():
    data = gui.get_data()
    database.save_input_data(data)
    data = gui.trans_to_list(data)
    # func.init(num1, num2)
    result = check_fun.check_function(data)
    gui.return_result(result)
    database.save_res(result)
