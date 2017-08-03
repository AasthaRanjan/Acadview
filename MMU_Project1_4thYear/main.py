print "Let's get started!"
spy_name = raw_input("provide your name here SPY :")
print 'Welcome ' + spy_name + " Glad to have you back with us :)"
spy_salutation =raw_input("what should we call you? (Mr. or Ms.):")
#check whether spy has input something or not
#concatination of salutation and name.
if len(spy_name)>0:
spy_name = spy_salutation + " " + spy_name
print 'Welcome ' + spy_name + " Glad to have you back with us!!"
#name= "Ms. Aastha"
#if len(name) > 0:
   # new_message = "YAY!! Name is not empty"
    #print new_message