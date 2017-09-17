
from steganography.steganography import Steganography
from select_friend import select_friend
from datetime import datetime
from globale import friends
import re
from colorama import init, Fore
init()

image_pattern='^[a-zA-Z0-9]+.jpg$'

def read_message():
    #choose friend from the list
    sender = select_friend()

    if (sender == -1):
        print Fore.RED + "Wrong Choice" + Fore.RESET
    else:
        friends[sender].avgChatWords()
        while(True):
            encrypted_image = raw_input("Provide encrypted image: ")
            if re.match(image_pattern,encrypted_image, flags=0) is not None:
                break
            else:
                print Fore.RED + "Image name must be alpha numeric"
        try:
             secret_message = Steganography.decode(encrypted_image)
             print "The secret message is: " + secret_message
             new_chat = {
                'message': secret_message,
                'time': datetime.now(),
                'sent_by_me': True
             }
             friends[select_friend]['chats'].append(new_chat)
             print Fore.RED + "your secret message has been saved"
        except IOError:
            print Fore.RED + "Sorry!! Image is not available" + Fore.RESET
        except TypeError:
            print Fore.RED + "Sorry!! Image is not available" + Fore.RESET

