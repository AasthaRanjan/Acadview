
from add_status import add_status
from add_friend import add_friend
#start_chat() function definition
def start_chat(name, age, rating):
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do ? \n 1. ADD STATUS \n 2. CLOSE APPLICATION \n 3. ADD FRIEND"
        result = int(raw_input(menu_choices))

        #validating user input
        if result == 1:
            current_status_message = add_status(current_status_message)
        elif (result == 2):
            show_menu = False
        elif result == 3:
            friends = add_friend()
            print " you have %d friends " %friends
        else:
             print "wrong choice.Try again later."

