from steganography.steganography import Steganography
from globale import friends
from select_friend import select_friend
from datetime import datetime

def send_message():
    #choose a friend

    friend_choice = select_friend()

    #prepare the message
    original_image = raw_input("Provide the name of the image to hide the message: ")
    output_image = raw_input("Provide name of the output image: ")
    text = raw_input("What do you want to write ")
    #Encrypt message
    Steganography.encode(original_image, output_image, text)


    #successful message
    print " your message is encrypted successfully "


    # save the messages
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True

    }

    friends[friend_choice]['chats'].append(new_chat)
    print "your secret message is ready!! "




