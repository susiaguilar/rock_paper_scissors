import random

def get_choices():
    player_choice = input("Enter a choice rock, paper, or scissors:")
    
    list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(list)
    
    choices = {"player" : player_choice, "computer" : computer_choice}
    
    return choices

choices = get_choices()
print(choices)

