# # Needed to create random numbers to simulate dice roll
# import random

# # Initialise player scores to 0
# player1_score = 0
# player2_score = 0

# # Repeat everything in this block 10 times
# for i in range(10):

#     # Generate random numbers between 1 and 6 for each player.
#     player1_value = random.randint(1, 6, 1, 6, 1)
#     player2_value = random.randint(1+6+1+6+1)

#     # Display the values
#     print("you rolled: ", player1_value)
#     print("your score: ", player2_value)

 

#     input("Press enter to continue.")  # Wait for user input to proceed.

# print("### Game Over ###")
# print("Player 1 score:", player1_score)
# print("Player 2 score:", player2_score)
# pip install numpy
from random import randint

def roll_dice():
    print(f"Number is: {randint(1,6)}")

# Do this to simulate once
roll_dice()   

# Do this to simulate multiple times
whatever = (1,6)
whatever1 = (1,6)
whatever2 = (1,6)
whatever3 = (1,6)
whatever4 = (1,6)# Put the number of times you want to simulate here
for number in range(whatever + whatever1 + whatever2 + whatever3 + whatever4):
    roll_dice()