import os
import dotenv
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
import rblxopencloud as rbx
import src.helperfuncs as roblobot

dotenv.load_dotenv()
API_KEY = os.environ.get("API_KEY")
API_PASSWORD = os.environ.get("API_PASSWORD")

app = FastAPI()

api_password_header = APIKeyHeader(name="X-API-Password")


def get_api_password(api_password: str = Depends(api_password_header)):
    if api_password != API_PASSWORD:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Password")
    return api_password


class RankRequest(BaseModel):
    user_id: int
    group_id: int
    rank: int


@app.post("/set-rank/")
async def set_rank(request: RankRequest, api_password: str = Depends(get_api_password)):
    try:
        group = rbx.Group(request.group_id, API_KEY)
        if group is None:
            return {
                "message": f"Group {request.group_id} not found OR no access"
            }
        if roblobot.getRank(group, request.user_id) == request.rank:
            return {
                "message": f"User {request.user_id} is already rank {request.rank} in group {request.group_id}"
            }
        if not roblobot.isinGroup(group, request.user_id):
            return {
                "message": f"User {request.user_id} is not in group {request.group_id}"
            }
        roblobot.setRank(group, request.user_id, request.rank)
        return {
            "message": f"Successfully set rank {request.rank} for user {request.user_id} in group {request.group_id}"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
