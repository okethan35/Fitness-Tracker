
from sqlFunc import insert_record, get_exercise_by_name, display_records, create_record 

def displayMenu():
    menuBar = "-" * 80
    spacing = " " * 33
    print(menuBar + "\n" + spacing + "DATABASE MENU\n" + menuBar + "\n"
          + "Please select one of the following options:\n" +
          "a. View current database\n" +
          "b. View all instances of an exercise\n" +
          "c. Insert a new exercise\n" +
          "d. To exit\n")

def processChoice(database):
    while(True):
        userInput = ''
        userInput = input("Please enter your choice: ")
        print("")
        match userInput:
            case 'a':
                display_records(database)
                userInput = ''
                userInput = input("Would you like to continue? (y/n)? ")
                print("")
                if userInput == 'y':
                    displayMenu()
                else:
                    print("Thank you for using our software! Good bye.")
                    break
            case 'b':
                get_exercise_by_name(database)
                userInput = ''
                userInput = input("Would you like to continue? (y/n)? ")
                print("")
                if userInput == 'y':
                    displayMenu()
                else:
                    print("Thank you for using our software! Good bye.")
                    break
            case 'c':
                insert_record(create_record(), database)
                userInput = ''
                userInput = input("Would you like to continue? (y/n)? ")
                print("")
                if userInput == 'y':
                    displayMenu()
                else:
                    print("Thank you for using our software! Good bye.")
                    break
            case 'd':
                print("Thank you for using our software. Good bye.")
                break
            case _:
                print("Sorry, that is not a valid selection.\n\n")
                userInput = ''
                userInput = input("Would you like to continue? (y/n)? ")
                print("")
                if userInput == 'y':
                    displayMenu()
                else:
                    print("Thank you for using our software! Good bye.")
                    break

