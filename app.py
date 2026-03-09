import streamlit as st
import requests

if st.button("START THE GAME"):
    start_number = 1
    payload={
        "start":start_number
    }
    requests.post("http://127.0.0.1:8000/start_game",json=payload)
if st.button("move_left"):
    move_number=1
    payload = {
        "act": move_number 
    }
    requests.post("http://127.0.0.1:8000/move", json=payload)
if st.button("move_down"):
    move_number=2
    payload = {
        "act": move_number 
    }
    requests.post("http://127.0.0.1:8000/move", json=payload)
if st.button("move_right"):
    move_number=0
    payload = {
        "act": move_number 
    }
    requests.post("http://127.0.0.1:8000/move", json=payload)
if st.button("move_up"):
    move_number=3
    payload = {
        "act": move_number 
    }
    requests.post("http://127.0.0.1:8000/move", json=payload)
if st.button("STOP_GAME"):
    start_number = 2
    payload={
        "start":start_number
    }
    requests.post("http://127.0.0.1:8000/start_game",json=payload)