import requests
import dotenv
import os


dotenv.load_dotenv()

API_PASSWORD = os.environ.get("API_PASSWORD")

USER_ID = 7264731101
GROUP_ID = 34840649
RANK = 254

def test_no_password():
    url = "http://localhost:8000/set-rank/"
    response = requests.post(url, json={
        "user_id": USER_ID, 
        "group_id": GROUP_ID, 
        "rank": RANK})
    
    if response.status_code == 403:
        print("Test passed: No password provided")
    else:
        print("Test failed: No password provided")

def test_invalid_password():
    url = "http://localhost:8000/set-rank/"
    response = requests.post(url, json={
        "user_id": USER_ID, 
        "group_id": GROUP_ID, 
        "rank": RANK}, headers={"X-API-Password": "invalidpassword"})
    
    if response.status_code == 403:
        print("Test passed: Invalid password provided")
    else:
        print("Test failed: Invalid password provided")

def test_valid_password():
    url = "http://localhost:8000/set-rank/"
    response = requests.post(url, json={
        "user_id": USER_ID, 
        "group_id": GROUP_ID, 
        "rank": RANK}, headers={"X-API-Password": API_PASSWORD})
    
    if response.status_code == 200:
        print("Test passed: Valid password provided")
    else:
        print("Test failed: Valid password provided")

test_no_password()
test_invalid_password()
test_valid_password()