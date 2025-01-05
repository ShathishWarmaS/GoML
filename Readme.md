Features:
	1.	Two Players: Controlled via keyboard input.
	2.	Scoring System: Points are awarded when the ball goes out of bounds.
	3.	Obstacles: Two square obstacles are placed randomly on the field. The ball will bounce off these obstacles if it collides with them.


Steps:
	1.	Paddle Movement: Each player controls their paddle using specific keys.
	2.	Ball Movement: The ball moves across the screen, bouncing off walls and paddles.
	3.	Score: Points are awarded when the ball goes out of bounds.
	4.	Obstacles: Two square obstacles are placed randomly in the game area. The ball will bounce off these obstacles if it collides.

Key Features Implemented:
	1.	Obstacles: Two obstacles are placed randomly within the game field. The ball’s movement is checked for collisions with the obstacles. When the ball collides with an obstacle, it bounces off in the opposite direction.
	2.	Ball Movement: The ball is updated every frame, and its position is checked for collisions with walls, paddles, and obstacles.
	3.	Score System: The score is updated when the ball goes out of bounds, and the ball is reset to the center of the screen.


Summary:
	•	Obstacles: Two obstacles are placed randomly at the start of the game and don’t overlap with the ball’s starting position.
	•	Ball Bouncing: The ball will bounce off the obstacles, paddles, and walls.
	•	Scoring: A point is awarded when the ball goes out of bounds.
	•	Two-Player Control: Player 1 controls their paddle with the “ArrowUp” and “ArrowDown” keys. Player 2 controls their paddle with a similar setup (not implemented in the frontend for simplicity).

Key Changes:
	1.	Player 1’s Controls: Arrow keys (ArrowUp and ArrowDown).
	2.	Player 2’s Controls: W (up) and S (down).
	3.	Paddle Movement Update: Both paddles are now controlled independently by Player 1 and Player 2.

Explanation of Changes:
	1.	Player 1: Still uses the ArrowUp and ArrowDown keys to move their paddle.
	2.	Player 2: Now uses the W key to move up and the S key to move down.
	3.	Both paddles update: The paddle positions are sent to the backend whenever the user presses a key, and the backend updates the game state accordingly.

Summary of Controls:
	•	Player 1:
	•	Up: Arrow Up (ArrowUp)
	•	Down: Arrow Down (ArrowDown)
	•	Player 2:
	•	Up: W
	•	Down: S

Now, both Player 1 and Player 2 can control their paddles independently. Player 1 uses the ArrowUp and ArrowDown keys, while Player 2 uses W and S.# GoML
