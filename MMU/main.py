from spy_details import spy
import start_chat
print "Let's get started!"
question = "continue as " + spy.spy_salutation + " " + spy.spy_name + ":(Y/N)"
existing = raw_input(question)
# validating user input
if existing == "Y" or existing == "y":
   start_chat.start_chat(spy.spy_name,spy.spy_age, spy.spy_ratings)
elif(existing == "N" or existing == "n"):
    spy_name = raw_input("provide your name here SPY :")
    if len(spy_name)>0:
        if not spy_name.isalpha():
            print " invalid spy_name INPUT "
            spy_name = raw_input("provide your name here again :")
        else:
            print "VALID INPUT NAME "
            spy_age = 0
            spy_rating = 0.0
            spy_is_online = False
            spy_salutation = raw_input("what should we call you? (Mr. or Ms.):")
            spy_age = int(raw_input("Enter your age here:"))
            if spy_age >12 and spy_age <50:
                print "you are too good to go."
                spy_rating = float(raw_input("Give your rating here:"))
                if spy_rating >= 4.5:
                    print "good"
                elif spy_rating > 3.5 and  spy_rating > 4.5:
                    print "excellent"
                elif spy_rating > 2.5 and spy_rating > 3.5:
                    print "you can do better"
                else:
                    print "need improvment"
                spy_is_online = True
                print "Authentication completed welcome " + spy_name + " age: " + str(spy_age) + " rating of: " + str(spy_rating) + " proud to have you!!"
            else:
                print "INVALID USER"

    else:
        print "You are not a valid user"
    spy_name = spy_salutation + " " + spy_name
    print  " WLECOME " + spy_name + " GLad to have you back with us!! "
    print " Alright " + spy_name + " I'd like know more about you "

    print "A SPY needs to have valid name.Try again."
else:
    print "WRONG CHOICE"
