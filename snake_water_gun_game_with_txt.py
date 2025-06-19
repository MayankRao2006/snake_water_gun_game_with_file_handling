import random

# Rules and welcome message
print("Welcome to Snake, Water, Gun Game!")
print("""Before we start, let's clarify the rules:
        1. Snake beats Water
        2. Water beats Gun
        3. Gun beats Snake
        4. If both players choose the same option, it's a tie
        5. The game continues until one player reaches 3 points""")

player_points = 0
computer_points = 0

print("Enter 's' for Snake, 'w' for Water, 'g' for Gun, or 'q' to quit the game")

# Start game log
with open("snake_water_gun.txt", "a") as z:
    z.write("Game started\n")

# Game loop
while True:
    player_choice = input("Your choice: ").lower()
    computer_choice = random.choice(['s', 'w', 'g'])

    if player_choice == 'q':
        print("Thanks for playing!")
        result = "Player quit the game early."
        break

    elif player_choice not in ['s', 'w', 'g']:
        print("Invalid choice, please try again.")
        continue

    elif player_choice == computer_choice:
        print(f"Both chose {player_choice}. It's a tie!")

    elif (player_choice == 's' and computer_choice == 'w') or \
         (player_choice == 'w' and computer_choice == 'g') or \
         (player_choice == 'g' and computer_choice == 's'):
        print("You win this round!")
        player_points += 1
    else:
        print("Computer wins this round!")
        computer_points += 1

    print(f"Player points: {player_points}, Computer points: {computer_points}")

# Log round result
    with open("snake_water_gun.txt", "a") as z:
        z.write(f"Player chose: {player_choice}, Computer chose: {computer_choice}\n")
        z.write(f"Player points: {player_points}, Computer points: {computer_points}\n\n")
# Check for winner and result
    if player_points == 3:
        result = "Congratulations! You reached 3 points and won the game!"
        print(result)
        break
    elif computer_points == 3:
        result = "Computer reached 3 points. Better luck next time!"
        print(result)
        break

# Log final result after loop ends
with open("snake_water_gun.txt", "a") as z:
    z.write(f"THE WINNER IS: {result}\n\n")

# Display game log
with open("snake_water_gun.txt", "r") as z:
    content = z.read()
    print(content)
