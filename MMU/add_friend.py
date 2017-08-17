
# import statements.
from globale import friends

# add new friends.
def add_friend():

    new_friend = {
        'name': '',
        'salutation': '.',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }
    new_friend['name']= raw_input("Please add your friend's name:")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.: ")
    #concatination

    new_friend['name'] = new_friend['name'] + " " + new_friend['salutation']

    new_friend['age'] = int(raw_input("Age: "))

    new_friend['ratings'] =float (raw_input("Spy rating:"))


    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] <50:
            #Add friend
        friends.append(new_friend)
        print 'Friend Added'

    else:
        print 'sorry! Invalid entry. we can\'t add spy with thw details you provided'
     #returning total number of friend
    return len(friends)