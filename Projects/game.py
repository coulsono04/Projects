import random

class Player():

    def __init__(self, health, attack_damage):
        self.health = health
        self.attack_damage = attack_damage


    def player_taking_damage(self):
        # may need to switch over to main player
        self.health = self.health - self.attack_damage
        print(f"Enemy took {self.attack_damage} damage! They are now on {self.health} health.")
        return self.health


    def player_turn(self, options):
        hit = input("rock, paper, scissors")
        print(f"You chose {hit}")
        correct = random.choice(options)
        print(f"The damage choice was {correct}")
        if hit == correct:
            print("Well done! It was a damaging blow!")
            #Enemy.taking_damage(self)
            player_current_health = self.player_taking_damage()
            return player_current_health
        else:
            print("unlucky")
            print(f"Player health is {self.health}")
            player_current_health = self.health
            return player_current_health

        
class Enemy():

    def __init__(self, health, attack_damage):
        self.health = health
        self.attack_damage = attack_damage

    def taking_damage(self):
        # may need to switch over to main player
        self.health = self.health - self.attack_damage
        print(f"Player took {self.attack_damage} damage! They are now on {self.health} health.")
        print(self.health)
        return self.health

    def enemy_turn(self, options):
        hit = random.choice(options)
        print(f"Enemy chose {hit}")
        correct = random.choice(options)
        print(f"The damage choice was {correct}")
        if hit == correct:
            print("Well done! It was a damaging blow!")
            # needs to be enemys
            enemy_current_health = self.taking_damage()
            print(enemy_current_health)
            return enemy_current_health

        else:
            print("unlucky")
            print(f"Player health is {self.health}")
            enemy_current_health = self.health
            return enemy_current_health


def scores(player_current_health, enemy_current_health):
    if player_current_health < 0:
        print("Enemy Wins... Player loses")
        return 0
    if enemy_current_health < 0:
        print("Enemy Loses, Player wins!")
        return 0
    else:
        return 1




# Pass this into functions
options = ["rock", "paper", "scissors"]

main_enemy = Enemy(100, 10)
player = Player(50, 20)

# Main Game

print("Welcome to the game!\n\n\n")
game_playing = 1
while game_playing == 1:
    player_current_health = player.player_turn(options)
    enemy_current_health = main_enemy.enemy_turn(options)
    game_playing = scores(player_current_health, enemy_current_health)
    print("\n\n New Round! \n\n")
    