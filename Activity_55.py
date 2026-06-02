valid = False

while not valid:

    try:

        # Ask the user to enter a number

        n = int(input("Enter a number: "))

        # Check if the number is even

        while n % 2 == 0:
            print("bye")

            # Change n so loop can stop

            n = n + 1

        # Stop the outer loop
        
        valid = True

    except ValueError:
        print("Invalid")