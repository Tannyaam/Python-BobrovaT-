import actions
import controller

def action_selection(action_number):
    if action_number == 1:
        act = actions.add_new_contact()
    elif action_number == 2:
        act = actions.delete_contact()
    elif action_number == 3:
        act = actions.change_information()
    elif action_number == 4:
        act = actions.find_contact()
    elif action_number == 5:
        act = actions.show_all()
    return act

def action_selection_stopcontinue_work(action_number):
    if action_number == 1:
        act2 = controller.button_click()