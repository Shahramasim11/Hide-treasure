# create a chess board
Row1 = ["⬜","⬜","⬜"]
Row2 = ["⬜","⬜","⬜"]
Row3 = ["⬜","⬜","⬜"]
game_board = (f"{Row1}\n{Row2}\n{Row3}")
print(game_board)
user_input1 = int(input("Where do you want to enter value between 1-9: "))
if user_input1 == 1:
    Row1[0] = "x"
elif user_input1 == 2:
    Row1[1] = "x"
elif user_input1 == 3:
    Row1[2] = "x"
elif user_input1 == 4:
    Row2[0] = "x"
elif user_input1 == 5:
    Row2[1] = "x"
elif user_input1 == 6:
    Row2[2] = "x"
elif user_input1 == 7:
    Row3[0] = "x"
elif user_input1 == 8:
    Row3[1] = "x"
elif user_input1 == 9:
    Row3[2] = "x"
else:
    print("Invalid input. Please enter a number between 1 and 9.")

# Update the game_board string with the modified rows
game_board = (f"{Row1}\n{Row2}\n{Row3}")

# Display the updated game board
print(game_board)







