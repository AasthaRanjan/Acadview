#import statements
from globale import STATUS_MESSAGES
from colorama import init, Fore


#updated status message
updated_status_message = None


def add_status(current_status_message):

    if current_status_message is not None:
        print "your current status is " + current_status_message + "\n"
    else:
        print " provide some status "


    default = raw_input("Do you want to select from the older status (y/n)?")


    if default.upper() == "N":
        new_status_message = raw_input("what status message do u want to set")

        #validating user's input
        if len(new_status_message) > 0:
            #adding new friend to the list
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            print "your updated status message is %s" % updated_status_message
        else:
            print Fore.RED + " you did not provide any status message "

    elif default.upper() == "Y":
        #conter for serial number of message
        item_position = 1

        for message in STATUS_MESSAGES:
            print str(item_position) + " . " + message
            item_position = item_position + 1



        message_selection = int(raw_input("\nChoose from the above message "))

        #validating users' input
        if len( STATUS_MESSAGES) >= message_selection:
             updated_status_message =  STATUS_MESSAGES[message_selection - 1]
             print "your updated message is: " + updated_status_message
        else:
            print Fore.RED + "Invalid choice. Try again. "
    return updated_status_message