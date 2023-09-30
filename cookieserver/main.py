from fastapi import FastAPI, Body
from starlette.responses import FileResponse
from Crypto.Util.number import bytes_to_long, long_to_bytes
from hashlib import sha256
from typing import Annotated

app = FastAPI()

from secrets import n,e
from flag import flag

def fdh(message, bitsize):
    bytesize = (bitsize // 8)
    output = sha256(message).digest()

    while len(output) < bytesize:
        output += sha256(output).digest()

    return bytes_to_long(output)

def verify(message, signature):
    h = fdh(message, 1024)
    test = pow(signature, e, n)
    return test == (h % n)


@app.post("/cookie")
def cookie(question: Annotated[str, Body()], cookie: Annotated[str, Body()]):
    try:
        question = bytes.fromhex(question)
        cookie = bytes_to_long(bytes.fromhex(cookie))
        if verify(question, cookie):
            if question == b"I'd like a cookie, please!":
                return {"message": flag}
            else:
                return {"message": "That's a fine cookie but you'll have to ask more politely if you'd like to get a flag!"}
        else:
            return {"message": "No thanks, I don't want your stinky fish"}
    except:
        return {"message": "Go home, you're drunk"}


@app.get("/")
def main():
    return FileResponse('index.html')

@app.get("/src")
def src():
    return FileResponse('main.py')
