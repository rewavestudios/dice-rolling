# Importing the 'random' module to generate random numbers
import random 

# Initialize a counter to keep track of how many times the dice have been rolled
roll_count = 0

# Start an infinite loop so the game keeps running until the user chooses to exit
while True:
    # Ask the user if they want to roll the dice, and convert their input to lowercase
    choice = input('Roll the dice? (y/n): ').lower()

    # If the user types 'y', proceed to roll two dice
    if choice == 'y':
        # Generate a random integer between 1 and 6 for the first die
        die1 = random.randint(1, 6)
        # Generate a random integer between 1 and 6 for the second die
        die2 = random.randint(1, 6)
        # Increment the roll counter
        roll_count += 1
        # Print the result of both dice rolls
        print(f'({die1}, {die2})')
        # Print how many times the user has rolled so far
        print(f'You have rolled the dice {roll_count} time(s).')

    # If the user types 'n', exit the game
    elif choice == 'n':
        # Print a goodbye message and the total number of rolls
        print(f'Thanks for playing! You rolled the dice {roll_count} time(s).')
        # Use break to exit the while loop and end the program
        break

    # If the user types anything other than 'y' or 'n', show an error message
    else:
        print('Invalid choice!')
