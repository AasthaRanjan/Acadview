from globale import friends
from colorama import init

init()

def select_friend():
    counter = 1
    for friend in friends:
        print str(counter) + ". ",
        friend.displayDetails()
        counter = counter + 1

        while True:
            result = raw_input("select from the list :")
            result = int(result)
            if (result>0 and result< counter):
                return result - 1
            else:
                return " collapsed "
