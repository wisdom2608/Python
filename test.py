command = ""
while True:
    command = input('>').lower()
    if command == 'start':
        print('Car started…Ready to go')
    elif command == 'stop':
        print('Car stop.')
    elif command == 'help':
        print("""
start - to star the car
stop - to stop the car
quit- to exit
""")
           
    elif command == 'quit':
        break
    else:
        print(" Sorry, I don't understand that")