# import statements
#from globals import current_status_message
from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message
from read_chat_history import read_chat_history
from globale import friends
import time
from colorama import Fore, init
from globale import current_status_message

init()

#start_chat() function definition
def start_chat(name, age, rating, status):
        error_messgae = None #variable for storing error message
        if not (age > 12 and age < 50):
         #invalid age.
            error_message = "Invalid age. Provide valid age."
            print error_message
        else:
         welcome_message = "Authentication complete. Welcome\n " \
                           "Name : " + name + "\n" \
                           "Age: " + str(age) + "\n" \
                           "Rating: " + str(rating) + "\n" \
                           "Proud to have you "

         if rating > 4.0:
             welcome_message = welcome_message + "you are excellent"
         elif rating > 3.0:
             welcome_message = welcome_message + "you are good"
         else:
             welcome_message = welcome_message + "you need to work on it"
         print Fore.CYAN+welcome_message


        # displaying menu for user.
        show_menu = True
        while show_menu:
            menu_choices = Fore.LIGHTMAGENTA_EX + "What do you want to do? \n " + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + "1. Add a status update \n " + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + "2. Add a friend \n " + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + "3. Send a secret message \n " + Fore.RESET +\
                           Fore.LIGHTMAGENTA_EX + "4. Read a secret message \n " + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + "5. Read Chats from a user \n " + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + "6. Close Application \n"
            result = int(raw_input(menu_choices))

            # validating users input
            if result == 1:
                current_status_message = add_status()
                print 'your status has been updated to :\n', current_status_message

            elif result == 2:
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)

            elif result == 3:
                send_message()

            elif result == 4:
                read_message()

            elif result == 5:
                read_chat_history()

            elif result == 6:
                show_menu = False
                print Fore.RED + " APPLICATION IS CLOSED NOW. "
            else:
                print Fore.RED+ "wrong choice try again."





