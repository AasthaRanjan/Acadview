# import statements.
from globale import friends
import re
#importing spy_details.py file
from spy_details import spy
from colorama import Fore, init


# add new friends.

def add_friend():
    new_friend = \
        {
            'name': '',
            'salutation': '.',
            'age': 0,
            'rating': 0.0,
            'is_online': False,
            'chats': []
        }
    new_friend['name']= raw_input("Please add your friend's name:")
    if len(spy["name"])>0:
       #regular expression for matching alphabets
       pattern5 = '^[a-zA-Z\S]+$'
       if re.match(pattern5, new_friend["name"]) is not None:
            #string matched
            new_friend['salutation'] = raw_input("Are they Mr. or Ms.: ")
            pattern6 = '^[M][r s]$'
            if re.match(pattern6, new_friend["salutation"]) is not None:
               print "Checking"
               new_friend["name"] = new_friend["salutation"] + " " + new_friend["name"]
               new_friend["age"] = int(raw_input("Age? "))# checking
               pattern7 = '^[0-9]+$'
               if re.match(pattern7, new_friend["age"]) is not None:
                   print "Checking"
                   new_friend['ratings'] =float (raw_input("Spy rating:"))
                   pattern8 = '^[0-9]+\.[0-9]+$'
                   if re.match(pattern8, new_friend["rating"]) is not None:
                       print "Checking"
                       if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['age'] <50:
                         #Add friend
                            friends.append(new_friend)
                            return len(friends)
                       else:
                           print Fore.RED + " Sorry! Invalid entry.we can't add spy with the details you provided"
                   else:
                       print Fore.RED + " Input friend rating format is invalid "
               else:
                   print Fore.RED + " Input friend age format is invalid "
            else:
                print Fore.RED + " Input friend salutation format is invalid "
       else:
           print Fore.RED + " Input friend name format is invalid "
    else:
        print Fore.RED + " Enter valid name to continue "

