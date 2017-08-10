def add_friend():
    friends_name =[]
    friends_age =[]
    friends_rating = []
    friends_is_online =[]

    new_name = raw_input("Please add your friend's name: ")
    new_salutation = raw_input("Are they Mr. or Ms.: ")
    new_name = new_name + " " + new_salutation
    new_age = raw_input("Age: ")
    new_rating = raw_input("Spy rating:")

    new_age = int(new_age)
    new_rating = float(new_rating)
    if len(new_name) > 0 :
            #Add friend
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
    else:
        print 'sorry! Invalid entry. we can\'t add spy with thw details you provided'