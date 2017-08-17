from globale import friends

def select_friend():
    counter = 1
    for friend in friends:
        print str(counter) + ". " + friend['name'] + " Age : " + str (friend['age'])
        counter = counter + 1
    result = int(raw_input("select from the list : "))
    return result - 1

x = select_friend()
