from start_chat import start_chat
from spy_details import Spy
from globale import spy
from colorama import init, Fore
import re #for implementing regular expression
init()

name_pattern = '^[a-zA-Z]+[\sa-zA-Z]*$'
age_pattern = '^[0-9]+$'
rating_pattern = '^[0-9]+\.[0-9]+$'


print "Let's get started!"
question = Fore.LIGHTBLUE_EX + "Do you want to continue as " + spy.salutation + spy.name + "(Y/N)"
existing = raw_input(question)

# validating user input
if (existing.upper() == "Y") :

    spy_name = spy.salutation + " " + spy.name
    #default user
    start_chat(spy.name, spy.age, spy.rating, spy.is_online)

elif existing.upper() == "N":
    #new user
    while True:
     spy.name = raw_input("provide your name here :")
     if re.match(name_pattern, spy.name)!=None:
         break
     else:
         print(Fore.RED+ "Name can only contains alphabets,name cannot be null and name cannot start with space.Please provide a valid name." + Fore.RESET)

    if len(spy.name) > 0:
            spy.salutation = raw_input("what should we call you? (Mr. or Ms.):")
            spy.name = spy.salutation + " " + spy.name
            print "Okay" +  spy.name  + " I would like to know more about you"

    while True:
         try:
            spy.age = raw_input("Enter your age here:")
            if re.match(age_pattern,spy.age)!= None:
                spy.age=int(spy.age)
                break

            else:
             print (Fore.RED +"Age can only be a integer.please re-enter your age" +Fore.RESET)

         except ValueError:
             print Fore.RED + "Invalid age. Try again"

    while True:
        spy.rating = raw_input("What is your spy rating?")             # converting users input to float (typecasting)
        if re.match(rating_pattern, spy.rating) != None:
            spy.rating = float(spy.rating)
            break
        else:
            print Fore.RED + "Enter Again!!!"
    if spy.rating <=5.0 and spy.age > 12 and spy.age < 50:
        start_chat(spy.name, spy.age, spy.rating, spy.is_online)

    else:
        print Fore.RED + "Invalid name.Try again."
else:
    print Fore.RED + "Wrong choice.Try again."




