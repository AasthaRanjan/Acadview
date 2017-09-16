from globale import friends

def select_friend():
    counter = 1
    for friend in friends:
        print str(counter) + ". " + friend['name'] + " Age : " + str (friend['age'])
        counter = counter + 1
        while True:
            result = raw_input("select from the list :")
            pattern19 = "^[0-9]+$"
        if re.match(pattern19,result, flag=0)!=None:
            break
        else:
            print " Input Integer Value "
            result = int(result)
            if (result>0 and result< counter):
                return result - 1
            else:
                return " collapsed "
