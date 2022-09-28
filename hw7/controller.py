import actions
import gui

def button_click():
    action_number = gui.action_request()
    act = actions.action_selection(action_number)
