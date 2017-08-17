def add_status(current_status_message):

    STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

    default = raw_input("Do youwant to select from the older status (y/n)?")

    if default.upper() == "N":
        new_status_message = raw_input("what status message do u want to set")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
        else:
             pass

    elif default.upper() == "Y":
         item_position = 1

         for message in STATUS_MESSAGES:
             print item_position + " . " + message
             item_position = item_position + 1
         message_selection = int(raw_input("\nChoose from the above message "))
         if len(STATUS_MESSAGES) >= message_selection:
             updated_status_message = STATUS_MESSAGES[message_selection - 1]