import jwt
from fastapi import Request, HTTPException, Depends

SECRET_KEY = "somestrongkey"
ALGORITHM = "HS256"


def create_token(user_id: int, email: str) -> str:
    """
    Create a JWT token with user_id and email.
    """
    return jwt.encode({"user_id": user_id, "email": email}, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(req_header: dict) -> dict:
    """
    Decode a JWT token from the Authorization header.
    """
    token = req_header.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    token = token.split(" ")[1]  # Split 'Bearer <token>'
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def check_token(req_header: dict) -> bool:

    print(req_header)

    token = req_header.get("Authorization")
    if not token:
        return False

    token = token.split(" ")[1]
    
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False




def validate_tokens(request : Request) : 

    auth_header = request.headers.get("Authorization")
    
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized: Bearer token missing or invalid")
    
    bearer_token = auth_header[len("Bearer "):].strip()
    try:
        jwt.decode(bearer_token, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return False
    except jwt.InvalidTokenError:
        print("Invalid token.")
        return False
    










