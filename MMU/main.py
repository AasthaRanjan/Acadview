from spy_details import spy
from start_chat import start_chat

print "Let's get started!"
question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + ":(Y/N)"
existing = raw_input(question)
# validating user input
if (existing.upper() == "Y") :

    spy_name = spy['salutation'] + " " + spy['name']
    start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])

elif existing.upper() == "N":
    spy['name'] = raw_input("provide your name here :")

    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("what should we call you? (Mr. or Ms.):")

        while True:
            try:
             spy['age'] = int(raw_input("Enter your age here:"))
             break
            except ValueError:
             print "Invalid agr. Try again"


        spy['name'] = spy['salutation'] + " " + spy['name']

        spy['rating'] = float(raw_input("What is your spy rating?"))  # converting users input to float (typecasting)
        spy['is_online'] = True

        # starting chat application.
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
    else:
        print "Invalid name.Try again."
else:
    print "Wrong choice.Try again."




