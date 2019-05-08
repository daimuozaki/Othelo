# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:30:51 2019

@author: ReijerGrimbergen
"""

# In[3]
import numpy as np
import matplotlib.pyplot as mlp

#盤面状態の定義
OUT_OF_BOARD = -1
EMPTY = 0
BLACK = 1
WHITE = 2
#プレイヤー番号の定義
PLAYER_1 = 0
PLAYER_2 = 1
#プレイヤー種類の定義
NO_ENTRY = -1
HUMAN = 0

# In[4]
game_Board = [[EMPTY]*10]*10
turnPlayer = PLAYER_1

class Player:
    def __init__(self):
        self.kind = 0
        self.passed = False
        self.win_num = 0
        
        
player1 = Player()
player2 = Player()

Player_info = [player1,player2]

