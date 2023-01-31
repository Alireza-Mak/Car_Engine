# *****************************CAR**********************************
# ********************Start or Stop The Car Engine*************************
command = ''
started = False
while True:
    command = input('Please enter your command: ').lower()

    if command == 'help':
        print(""" 
Start -> start the car
Stop -> stop the car
quit ->quit the car
        """)
    elif command == 'start':
        if not started:
            print('Car start')
            started = True
        else:
            print('Your car has already started.')
    elif command == 'stop':
        if started:
            print('Car stopped')
            started = False
        else:
            print('Your car has already stopped.')

    elif command == 'quit':
        print('You quit the car')
        break
    else:
        print('I dont understand the command')