
from fastapi import FastAPI, APIRouter, HTTPException
import uvicorn
import uuid
from expiringdict import ExpiringDict

api = FastAPI()
router = APIRouter()

messages = ExpiringDict(max_len=100, max_age_seconds=604800) # message expire after 7 days


@router.post("/message/create")      # message creation  and  get url of message
def create_message(message: str):
    id = str(uuid.uuid4())                            # make infeasible to guess the URL to a message by generating randome id
    messages[id] = message
    return f'http://127.0.0.1:8080/message/{id}'


@router.get("/message/{id}")      #client can view any message by using meassge id
def read_item(id: str):
    if id in messages:
        return messages[id]
    raise HTTPException(status_code=404, detail="Message not found")


def configure():
    api.include_router(router)

def run():
    configure()
    uvicorn.run(api, port=8080, host='0.0.0.0')


if __name__ == "__main__":
    run()
