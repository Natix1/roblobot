import rblxopencloud as rbx
import os
import dotenv
import src.helperfuncs as roblobot

dotenv.load_dotenv()
API_KEY = os.environ.get("API_KEY")

USER_ID = 7264731101
GROUPID = 34840649
RANK = 254

group = rbx.Group(GROUPID, API_KEY)
roblobot.setRank(group, USER_ID, RANK)