### Remote-Controlled Pygame Engine
A modular, multi-tier Python project that allows you to control a local Pygame application through a web-based user interface.
## why?
I originally created this project with the goal of rendering the Pygame environment on my mobile device, but I soon realized that Pygame must render locally on the host machine.

This project demonstrates how to decouple game logic from user input by using FastAPI as a bridge between a Streamlit web controller and a Pygame rendering window.

 ## Architecture
The project is broken down into four main components:

**Game Engine (main.py)**: Handles the Pygame window, state management, and rendering of the player character .

**API Layer (app.py)**: A FastAPI application that receives HTTP POST requests and translates them into Python commands to update the game state.

**Data Models (schemas.py)**: Pydantic models that ensure the data being sent to the API is strictly typed and validated.

**Web Controller (frontend.py)**: A Streamlit dashboard containing interactive buttons that send HTTP requests to the FastAPI backend to move the player or start/stop the game.

 **Prerequisites**
Make sure you have Python installed, then install the required dependencies:

**Bash**
## pip install pygame fastapi uvicorn streamlit requests pydantic
**How to Run the Project**
Because this project uses both a backend API and a frontend UI, you will need to run two separate terminal windows.

**Step 1: Start the Game API (Backend)**
Open your first terminal, navigate to the project directory, and start the FastAPI server using Uvicorn. This will also initialize the Pygame instance when triggered.

**Bash**
## uvicorn app:app --reload
(Note: Replace app:app with the actual name of your FastAPI file if it is not named app.py. For example, if it's api.py, use uvicorn api:app --reload)

***Step 2: Start the Web Controller (Frontend)***
Open a second terminal, navigate to the same directory, and spin up the Streamlit interface:

**Bash**
## streamlit run frontend.py
(Note: Replace frontend.py with the actual name of your Streamlit file)

***Step 3: Play the Game***
A web browser window will automatically open showing your Streamlit buttons.

Click START THE GAME on the webpage. This will open the Pygame window on your desktop.

Use the move_up, move_down, move_left, and move_right buttons on the webpage to control the red square in the Pygame window!

Click STOP_GAME when you are finished.