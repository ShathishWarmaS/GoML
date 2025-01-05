# Ping Pong Game

A simple two-player ping pong game where players can control paddles and try to score points. The game includes obstacles that cause the ball to bounce.

## Setup Instructions

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ShathishWarmaS/GoML.git
    ```

2. Install the required dependencies:

    - For the backend, this game uses Flask and WebSocket:
      ```bash
      pip install flask websockets
      ```

3. To run the game locally, run the following command in your project directory:

    ```bash
    python app.py
    ```

4. Open two browser tabs and navigate to:
    ```bash
    http://localhost:5000
    ```

    The game will start, and you can control paddles using the keyboard.

## How to Run the Game

1. The game will automatically start once the server is running.
2. Players can control:
    - **Player 1**: Arrow Up and Arrow Down keys.
    - **Player 2**: `W` (up) and `S` (down) keys.
3. The game will start with random obstacles. The first player to score 5 points wins.

## Technical Choices

- **Backend**: Flask (for serving the frontend and WebSocket communication).
- **Frontend**: HTML5 Canvas for drawing the game state and WebSocket for real-time updates.
- **WebSocket**: Used to send paddle movements and game updates between the server and client for smooth real-time interactions.

## Known Limitations

- Minor bugs might exist, such as potential paddle overshooting the boundaries (depending on game speed).
- The game may not handle reconnections gracefully if a player disconnects.
- Only basic collision detection is implemented for obstacles.

## AI Assistance

- The core functionality, including game state updates, ball movement, and paddle control, was implemented with AI assistance to help structure the game logic and WebSocket communication.
