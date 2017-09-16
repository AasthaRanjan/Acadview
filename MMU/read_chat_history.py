from select_friend import select_friend
from globale import friends
import spy_details
from colorama import init, Fore

spydetails = spy_details
init()



def read_chat_history():
    choice = select_friend()
    if choice == "error":
        print Fore.RED + " Wrong Choice " + Fore.RESET
    else:
        print (Fore.BLUE + " Message sent are shown in blue color \n " + Fore.GREEN + "Recived message are shown in green color :" + Fore.RESET)
        choice = int(choice)
        chats = friends[choice].get_chats()
        for chat in chats:
            if chat['send_by_me']:
                print (Fore.RED + str(chat['time']) + " " + Fore.BLUE + spydetails.get_name() + " " + Fore.RESET + chat['message'])
            else:
                print (Fore.RED + str(chat['time']) + " " + Fore.GREEN + friends[choice].get_name() + " " + Fore.RESET + chat['message'])