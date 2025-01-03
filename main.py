#function welcoem, welcomes the guest
def welcome():
    print("Welcome to the Tech Support")
    name = input("What's your name? ")
    print("Welcome, " + name)
    print("How can I help you today?")
#provides user option and answer
def option():
    while True:
        welcome()
        print("1. Software Support")
        print("2. Hardware Support")
        
        user_choice = input("Enter the number of your choice: ")

        if user_choice == "1":
            print("What kind of help do you want?")
        elif user_choice == "2":
            print("What hardware problem are you facing?")
        else:
            print("Invalid option. Please try again.")
        
        # Got the exit choice idea from youtube
        exit_choice = input("Do you want to exit? (yes/no): ")
        if exit_choice.lower() == 'yes':
            break
    # same with this one got the idea from youtube
if __name__ == "__main__":
    option()



    
    


