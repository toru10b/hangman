'''
Created on 2021/01/03

@author: ToruShinmura
'''
#第１０章　知識を１つにまとめる
"""引数wordはプレイヤー２に答えてほしい単語
    変数wrongはプレイヤー２の回答回数の算出に使用
    変数rlettersはwordを一文字ずつ分解し、答えなければならない残りの文字を覚えておくもの"""
def hangman(word):
    wrong = 0
    stages = ["",
              "____________         ",
              "|                    ",
              "|        |           ",
              "|       〇           ",
              "|      /|＼          ",
              "|      / ＼          ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '＄'
        else:
            wrong += 1

        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print("".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))


import random
word_list = ["blue","apple","marvel","fire","king"]
hangman(random.choice(word_list))
