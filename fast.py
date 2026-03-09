from fastapi import FastAPI
import schemas
from main import my_game 

app = FastAPI()
@app.post("/start_game",response_model=schemas.start)
def start(game_start:schemas.start):
    start_game=game_start.start
    my_game.starts(start_game)
    return{
        "start":start_game
    }
   
@app.post("/move", response_model=schemas.moves)  
def moving(player_moves: schemas.moves):
    player_act = player_moves.act
    my_game.play(player_act)
    return {
        "act": player_act
    }