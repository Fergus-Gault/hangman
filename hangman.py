import random

def hangman (word):
    wrong = 0
    
    stages = ["",
              "________     ",
              "|            ",
              "|       |    ",
              "|       0    ",
              "|      -|-   ",
              "|      | |   ",
              "|____________"]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter\n"
        char = input(msg)
        print("DEBUG: The word is "+ randomword)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win! The word was " + randomword)
            print(" ".join(board))
            win = True
            print("Would you like to play again?(Y/N)")
            playagain = input()
            if playagain == "Y":
                hangman(word)
            else:
                break
    if not win:
        print("\n"
              .join(stages[0: \
                           wrong]))
        print("You lose! It was {}."
              .format(word))


wordchoice = ["motorcycle", "cookie", "cheese", "snail", "island", "Earth", "nose", "crayon", "venture", "century", "monk", "button", "fresh", "cutting", "business", "return", "wrong", "happen", ""]

randomword = random.choice(wordchoice)
 
hangman(randomword)
