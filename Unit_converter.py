#Create a program that converts units. More specifically, kilometers into miles.

#First create a plan for this program. Together with the instructor define the steps the user will take when using the program.

while True:
    print ("Welcome to the Unit Counter. Here you can convert kilometers to miles!")
    #The program greets user and describes what's the purpose of the program.

    km = input("Enter a number of kilometers: ")
    #The program asks user to enter number of kilometers. User enters the amount of kilometers.

    km = float(km.replace (",", "."))  # replace comma with dot, if user entered a comma

    miles = km * 0.621371   #The program converts these kilometers into miles and prints them.

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")
    #The program asks user if s/he'd want to do another conversion.

    if choice.lower() != "y" and choice.lower() != "yes":
        #If yes, repeat the above process (except the greeting).

        print("Goodbye! See you next time.")  # If not, the program says goodbye and stops.

        break




