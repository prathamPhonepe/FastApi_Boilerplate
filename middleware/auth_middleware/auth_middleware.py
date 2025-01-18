

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.routing import APIRouter
from utils.auth.auth_utils import validate_tokens
from utils.responses.responses import failure_responses

def authMiddleware(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return failure_responses(400 , "the auth token is not provided")    
    response = validate_tokens(request)
    if response is False :
        print("hey this is false")
        return failure_responses(400, "Bad Request: Not a valid token provided")
    return 

