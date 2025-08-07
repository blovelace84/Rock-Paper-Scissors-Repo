import random

choices = ['rock', 'paper', 'scissors']
win_map = { 'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper' }
lose_map = { v: k for k, v in win_map.items() }

class SmartAI:
    def __init__(self):
        self.history = []

    def predict_player_choice(self):
        if not self.history:
            return random.choice(choices)
        #Predict the most frequent move
        return max(set(self.history), key=self.history.count)

    def choose_move(self, strategy='normal'):
        predicted = self.predict_player_choice()

        if strategy == 'win':
            # AI chooses what beats the player's likely move
            return lose_map[predicted]
        elif strategy == 'lose':
            #AI choose what loses to the player's likely move
            return win_map[predicted]
        else:
            #Normal:random
            return random.choice(choices)

    def update_history(self, player_choice):
        if player_choice in choices:
            self.history.append(player_choice)
