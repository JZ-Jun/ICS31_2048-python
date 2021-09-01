# 2048-python
#uci first python project

Preamble
At this point in the course, you have enough knowledge about Python to do more than you might first expect. Many simple games, for example, can be written with your understanding of programming. So let's do it! Let's create the game 2048!
Concepts being tested
•	Data Structures
o	Nested Lists
o	Dictionaries
o	Potentially Sets
•	Branching
•	Loops
o	Nested Loops
•	Functions Basics
•	Critical thinking, planning, & organization
The Game
The game has 4 controls:
•	w - move the board up
•	s - move the board down
•	a - move the board left
•	d - move the board right
Moving the board will slide the pieces towards the chosen direction, combining pieces with the same number if they slide into each other. Sliding this board down!
![image](https://user-images.githubusercontent.com/49256407/131613203-cf174dcd-af34-42ed-a41d-dcc008af4f98.png)
The two 2's combine to form one 4. The game then randomly places another piece on the board, which is the 2 in the upper left of the second board. The goal of the game is to create a piece of the value 2048, in which case the player wins, and the game is over. The game may also terminate if there are no more empty spaces for the game to place a new piece in, and there are no more moves for the user to take, resulting in a loss for the player.
Our program will have one more input:
•	q - Terminates the program with the message: "Goodbye"
The Program
To help alleviate some of the pressure of creating a slightly larger program, we will provide you with:
•	base code
•	utility functions
•	a strategy guide
Game Loop
A round of 2048 can be broken up into the following actions:
•	Computer's turn
o	Place a new piece on the board
o	Check if the game is lost and act accordingly
•	Print the Updated Board
o	Remember to use the utilities.py module
•	User's turn
1.	Take input
2.	Validate input, return to step 1 of the User's turn if the input is invalid
3.	Quit the program if appropriate
4.	Update the board
o	If the board hasn't changed, return to step 1 of the User's turn
5.	Check if the game is won and act accordingly
Algorithms
User Moves The heart of this program is being able to manipulate the cells of the game board to create the player moves. There are many different ways to approach this, but all of them will require you to dig deep and apply many different concepts. You might, for example, need to apply concepts such as reversing a list, list concatenation, or list/set membership (the "in" operator).
Advise:
•	The obvious algorithm would involve moving pieces space by space across the board until no more empty spaces remain in an applied direction.
o	This approach may be simpler to think of, but implementing it leaves a lot of room for error.
•	A less obvious approach would be to delete unnecessary information from the board and add it back in after combining pieces.
o	Shifting the row [0, 2, 0, 4] left or right results in [2, 4, …] or […, 2, 4]. What information is important here? What can you ignore?
•	Most solutions will involve nested loops.
o	You should break the problem of updating the board down into the smaller problem of updating a single row or column, and then repeating the process for all rows or columns.



