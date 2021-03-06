"""


Martti Suosalo is a (drinking) game played as follows:

1. Players are arranged in a ring. Let the first player be 1, and the last N,
   clockwise. Player 1 starts the game.

The game with 8 players:

     (1)
 (8)     (2)
(7)       (3)
 (6)     (4)
     (5)


2. In each turn of the game, the player in turn calls out the number one greater
   than the previous player. Then the turn passes to the next player. The
   called out numbers start from 1 and are consequtive natural numbers.

4. The game starts clockwise: first player 1, then 2 etc.

5. If the called out number has more than 1 digits, and all of the digits are
   the same (such as 11, 33, or 444), the game direction changes AFTER such
   number is called out. Example: if player 2 called 10, player 3 called 11,
   player 2 will call 12.

6. Whenever the called out number satisfies at least one of the following conditions:
        a. divisible by 7
        b. contains 7 as one of its digits
        c. the sum of the digits is seven
   The player will call "Martti Suosalo" instead of the number. The number is
   still incremented. A number (such as 77) may both change the direction and be
   called "Martti Suosalo" // Suunnanvaihto ja Martti Suosalo

7. The game ends, when someone violates some rule. The loser has to down a drink!



The task is to write a program, which plays sober (read: flawless!) Martti
Suosalo game with the given number of players and turns.

The program shall take the number of players and turns as parameters
(command line or compile-time constants). Then it shall print out the course of
the game: which player shouted what.

Constraints:
- The game has 1 or more turns, and 1 or more players.
- There shall be no artifical constraints, except machine integer size.
- Although the real life game is perhaps interesting only with 3 to 10 players,
  the cases of 1, 2 and >10 players are well defined, and should be handled.



Sample output (P is the player):

> marttiSuosalo.exe 5 20
nPlayers: 5     nRounds: 20
P: 1    "1"
P: 2    "2"
P: 3    "3"
P: 4    "4"
P: 5    "5"
P: 1    "6"
P: 2    "Martti Suosalo"
P: 3    "8"
P: 4    "9"
P: 5    "10"
P: 1    "11"
P: 5    "12"
P: 4    "13"
P: 3    "Martti Suosalo"
P: 2    "15"
P: 1    "Martti Suosalo"
P: 5    "Martti Suosalo"
P: 4    "18"
P: 3    "19"
P: 2    "20"


> marttiSuosalo.exe 7 30
nPlayers: 7     nRounds: 30
P: 1    "1"
P: 2    "2"
P: 3    "3"
P: 4    "4"
P: 5    "5"
P: 6    "6"
P: 7    "Martti Suosalo"
P: 1    "8"
P: 2    "9"
P: 3    "10"
P: 4    "11"
P: 3    "12"
P: 2    "13"
P: 1    "Martti Suosalo"
P: 7    "15"
P: 6    "Martti Suosalo"
P: 5    "Martti Suosalo"
P: 4    "18"
P: 3    "19"
P: 2    "20"
P: 1    "Martti Suosalo"
P: 7    "22"
P: 1    "23"
P: 2    "24"
P: 3    "Martti Suosalo"
P: 4    "26"
P: 5    "Martti Suosalo"
P: 6    "Martti Suosalo"
P: 7    "29"
P: 1    "30"
"""