import sys

print("Rocks. Paper. Scissors. SHOOT!")
print("******************************")

user_one = input("Player One, enter your name: ")
user_two = input("Player Two, enter your name: ")
user_one_rps = input("%s. Choose rock, paper or scissors: " % user_one)
user_two_rps = input("%s. Choose rock, paper or scissors: " % user_two)

def compare(user1, user2):
    if user1 == user2:
        return("Tie.")
    elif user1 == 'rock':
        if user2 == 'scissors':
            return("Rock wins.")
        else:
            return("Paper wins")
    elif user1 == 'scissors':
        if user2 == 'paper':
            return("Scissors win.")
        else:
            return("Rock wins.")
    elif user1 == 'paper':
        if user2 == 'rock':
            return("Paper wins.")
        else: 
            return("Scissors win!")
    else:
        return("Wrong game. Enter either rock, paper or scissors.")
        sys.exit()

print(compare(user_one_rps, user_two_rps))