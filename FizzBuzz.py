
print ("Welcome to the fizzbuzz game!")

X = int(input("Choose a number between 1 and 100: "))         #User enters a number between 1 and 100

for number in range (1,X+1):     #FizzBuzz program starts to count to that number (it prints them in the Terminal).
    if number % 3 == 0:         #In case the number is divisible with 3, it prints "fizz" instead of the number.
        print("fizz")
    elif number % 5 == 0:       #If the number is divisible with 5, it prints "buzz".
        print ("buzz")
    elif number % 3 == 0 and number % 5 == 0:   #If it's divisible with both 3 and 5, it prints "fizzbuzz".
        print("Fizzbuzz")
    else:
        print(number)

