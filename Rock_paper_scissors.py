#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass
        
       

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))



class RandomPlayer(Player):
    def move(self):
        choice = random.choice(moves)
        return choice


class HumanPlayer(Player):

    def move(self):
        my_move = str(input('rock, paper, scissors?'))
        if my_move in moves:
            return my_move
        else:
            self.move()
            

class  CyclePlayer(Player):
    my_move = None
        
    def move(self):
        if self.my_move == None:
            return random.choice(moves)
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"
    
                   

class ReflectPlayer(Player):

    def learn(self, my_move, their_move):
        my_move = their_move
      

    def move(self):
        if self.their_move == None:
            return random.choice(moves)
        else:
            return self.their_move

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
        self.round = 0
        

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        #print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"You played {move1}")
        print(f"opponent played {move2}")
        if self.p1.beats(move1, move2) == True:
            print("**Player 1 wins**")
            self.score_p1 += 1
            print(f" Score: Player 1 ={self.score_p1}, Player 2 ={self.score_p2}")
        elif self.p2.beats(move2, move1)== True:
            print ("**Player 2 wins**")
            self.score_p2 += 1
            print(f" Score: Player 1 ={self.score_p1}, Player 2 ={self.score_p2}")
        else:
            print("**TIE**")
            print(f" Score: Player 1 ={self.score_p1}, Player 2 ={self.score_p2}")
            
        

    def play_game(self):
        print("Game start!")
        while self.score_p1 - self.score_p2 < 3 or self.score_p1 - self.score_p2 < 3:
            print(f"Round {self.round}:")
            self.play_round()
            self.round += 1
        print("Game over!")
        print("Total Score")
        print(f"Player 1= {self.score_p1}")
        print(f"Player 2= {self.score_p2}")
        


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
