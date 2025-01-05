import asyncio
import websockets
import random
import json
from flask import Flask, render_template
import threading

# Flask setup
app = Flask(__name__)

# Game state (global)
game_state = {
    "paddle1": {"x": 50, "y": 200, "speed": 20},
    "paddle2": {"x": 750, "y": 200, "speed": 20},
    "ball": {"x": 400, "y": 250, "dx": 2, "dy": 2},
    "score1": 0,
    "score2": 0,
    "obstacles": [{"x": 200, "y": 150, "size": 30}, {"x": 500, "y": 350, "size": 30}],
    "players": []  # Keep track of connected players
}

# Check if ball intersects with obstacles
def check_obstacle_collision(ball):
    for obstacle in game_state["obstacles"]:
        if (obstacle["x"] < ball["x"] < obstacle["x"] + obstacle["size"] and
            obstacle["y"] < ball["y"] < obstacle["y"] + obstacle["size"]):
            return True
    return False

# Game loop (moving the ball and checking for collisions)
async def game_loop():
    while True:
        # Update ball position
        game_state["ball"]["x"] += game_state["ball"]["dx"]
        game_state["ball"]["y"] += game_state["ball"]["dy"]

        # Ball collision with top/bottom walls
        if game_state["ball"]["y"] <= 0 or game_state["ball"]["y"] >= 500:
            game_state["ball"]["dy"] = -game_state["ball"]["dy"]

        # Ball collision with paddles
        if (game_state["ball"]["x"] <= 60 and game_state["ball"]["y"] in range(game_state["paddle1"]["y"], game_state["paddle1"]["y"] + 60)) or \
           (game_state["ball"]["x"] >= 740 and game_state["ball"]["y"] in range(game_state["paddle2"]["y"], game_state["paddle2"]["y"] + 60)):
            game_state["ball"]["dx"] = -game_state["ball"]["dx"]

        # Ball collision with obstacles
        if check_obstacle_collision(game_state["ball"]):
            game_state["ball"]["dx"] = -game_state["ball"]["dx"]
            game_state["ball"]["dy"] = -game_state["ball"]["dy"]

        # Ball goes out of bounds (scoring)
        if game_state["ball"]["x"] <= 0:
            game_state["score2"] += 1
            game_state["ball"] = {"x": 400, "y": 250, "dx": 2, "dy": 2}
        elif game_state["ball"]["x"] >= 800:
            game_state["score1"] += 1
            game_state["ball"] = {"x": 400, "y": 250, "dx": 2, "dy": 2}

        # Broadcast updated state to both players
        if len(game_state["players"]) == 2:
            update = {
                "ball_position": {"x": game_state["ball"]["x"], "y": game_state["ball"]["y"]},
                "paddles": {
                    "paddle1": game_state["paddle1"],
                    "paddle2": game_state["paddle2"]
                },
                "score": {"score1": game_state["score1"], "score2": game_state["score2"]},
                "obstacles": game_state["obstacles"]
            }
            await asyncio.gather(*[player.send(json.dumps(update)) for player in game_state["players"]])

        # Delay to control game speed (adjust as needed)
        await asyncio.sleep(0.02)  # 50 FPS

# Handle WebSocket connections and game state
async def game_logic(websocket):
    # Add the new connection to the players list
    game_state["players"].append(websocket)
    print(f"New player connected, total players: {len(game_state['players'])}")

    # Notify all players about the new player
    if len(game_state["players"]) == 2:
        for player in game_state["players"]:
            await player.send(json.dumps({"message": "Game started!"}))

    try:
        while True:
            # Wait for incoming data (player actions)
            message = await websocket.recv()
            data = json.loads(message)

            # Update paddle positions based on input data
            if "paddle1_y" in data:
                game_state["paddle1"]["y"] = data["paddle1_y"]
            if "paddle2_y" in data:
                game_state["paddle2"]["y"] = data["paddle2_y"]

    except websockets.exceptions.ConnectionClosed as e:
        print(f"Player disconnected: {e.code} - {e.reason}")
        game_state["players"].remove(websocket)
        print(f"{len(game_state['players'])} players connected")

    except Exception as e:
        print(f"Unexpected error: {e}")
        await websocket.close()

# Start the Flask server
@app.route('/')
def index():
    return render_template("index.html")  # Make sure your HTML file is named 'index.html'

def start_flask():
    app.run(debug=True, use_reloader=False)

# Start WebSocket server
async def start_websocket():
    server = await websockets.serve(game_logic, "localhost", 8765)  # WebSocket server for game logic
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

# Start both Flask and WebSocket servers
def run_servers():
    loop = asyncio.get_event_loop()
    websocket_thread = threading.Thread(target=lambda: loop.run_until_complete(start_websocket()))
    websocket_thread.start()
    start_flask()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(game_loop())  # Start the game loop for ball movement
    run_servers()