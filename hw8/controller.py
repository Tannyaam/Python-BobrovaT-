import actions
import gui
import user_choice
import support_actions

def button_click():
    action_number = gui.action_request()
    act = user_choice.action_selection(action_number)
    action_number = gui.continue_work()
    act2 = user_choice.action_selection_stopcontinue_work(action_number)