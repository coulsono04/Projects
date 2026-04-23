import random

class Player():

    def __init__(self, health):
        self.health = health
    
    def player_damage_taken(self):
        self.health = self.health - 10
        print (f"players health is now {self.health}


    def player_turn(self, choices, enemy):
        print("It is players turn\n")
        choice = input("rock, paper, or scissors")

class Enemy():

    def __init__(self, health):
        self.health = health

    def enemy_damage_taken():


    def enemy_turn(self, choices, enemy):
        print("It is players turn\n")
        choice = input("rock, paper, or scissors")
        correct = random.choice(choices)
        print(f"The correct choice was {correct}")
        if correct == choice:
            print("Hit!")
            return Player.player_damage_taken()
            



### Game

print("Welcome to the game!")
choices = ["rock", "paper", "scissors"]
playing = 1
while playing == 1:
