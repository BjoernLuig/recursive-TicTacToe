# recursive-tic-tac-toe

A simple unbeatable Tic Tac Toe game in python using recursion.

Exemple:

    TIC TAC TOE
    choose your Character (X or O): X
    who is first? (X or O): X

    -------------
    | ₁ | ₂ | ₃ |
    -------------
    | ₄ | ₅ | ₆ |
    -------------
    | ₇ | ₈ | ₉ |
    -------------

    it's your turn
    your move? (1,...,9): 3
    thinking...

    -------------
    | ₁ | ₂ | X |
    -------------
    | ₄ | O | ₆ |
    -------------
    | ₇ | ₈ | ₉ |
    -------------

    it's your turn
    your move? (1,...,9): 7
    thinking...

    -------------
    | ₁ | O | X |
    -------------
    | ₄ | O | ₆ |
    -------------
    | X | ₈ | ₉ |
    -------------

    it's your turn
    your move? (1,...,9): 8
    thinking...

    -------------
    | ₁ | O | X |
    -------------
    | ₄ | O | ₆ |
    -------------
    | X | X | O |
    -------------

    it's your turn
    your move? (1,...,9): 1
    thinking...

    -------------
    | X | O | X |
    -------------
    | O | O | ₆ |
    -------------
    | X | X | O |
    -------------

    it's your turn
    your move? (1,...,9): 6

    -------------
    | X | O | X |
    -------------
    | O | O | X |
    -------------
    | X | X | O |
    -------------

    it's a draw!
    press enter to exit

Don't worry, if it takes a few minutes to calculate the best first move.
It's in one of the corners but every possible move has to be calculated to get to this *obvious* solution by recursion.
