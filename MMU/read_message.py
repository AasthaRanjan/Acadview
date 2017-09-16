
from steganography.steganography import Steganography
from select_friend import select_friend
from datetime import datetime
from globale import friends

def read_message():
    #choose friend from the list
    sender = select_friend()

    encrypted_image = raw_input("Provide encrypted image: ")
    secret_message = Steganography.decode(encrypted_image)


    new_chat = {
      'message': secret_message,
      'time': datetime.now(),
      'sent_by_me': True
    }

    friends[select_friend]['chats'].append(new_chat)
    print "your secret message has been saved"

