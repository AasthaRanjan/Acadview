print "Let's get started!"
spy_name = raw_input("provide your name here SPY :")

#check whether spy has input something or not
#concatination of salutation and name.
if len(spy_name)>0:

    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False
    spy_salutation = raw_input("what should we call you? (Mr. or Ms.):")
    spy_age = int(raw_input("Enter your age here:"))
    if spy_age >12 and spy_age <50:
        print "you are too good to go."
    else:
        print "You are not a valid user"

        spy_rating = raw_input("Give your rating here:")
        if spy_rating > 4.5 :

elif spy_rating > 2.5 and spy_rating <3.5:

    print type(spy_age)
    spy_name = spy_salutation + " "  + spy_name
    print  " WLECOME " + spy_name + " GLad to have you back with us!! "
    print " Alright " + spy_name + " I'd like know more about you "





else:
    print "A SPY needs to have valid name.Try again."

#
#name= "Ms. Aastha"
#if len(name) > 0:
   # new_message = "YAY!! Name is not empty"
    #print new_message

