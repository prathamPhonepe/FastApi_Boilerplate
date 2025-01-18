from fastapi import FastAPI, Request, Header, HTTPException, Depends
from fastapi.responses import JSONResponse
from utils.responses.responses import success_responses, failure_responses
from utils.auth.auth_utils import create_token   , validate_tokens
from config.config import getConnection , closeConnection

async def get_data():
    data = {"message": "Hello, this is a GET request!"}
    return success_responses(200 , "hey this is coprrected" , data)


async def base_request():
    something = {"some value": True, "another value": False}
    print("something", something)

    return success_responses(200, "Hello, this is a GET request!", something)



async def echoServer(request: Request):
    content = await request.json()
    print(content['email'])
    return success_responses(200 , "this is the post request and the data sent is" , content)




async def generate_jwt_token(request: Request):
    content = await request.json()

    print(content)

    try : 
        if not content or 'email' not in content or 'user_id' not in content:
            return failure_responses(400 , "please pass all the param")
        
        if content and "user_id" in content:
            token = create_token(content["user_id"] , content["email"])
            print(token)
            return success_responses(200, "Token generated", {"token": token})
        else:
            return failure_responses(400, "User ID is required")
    except : 
        return failure_responses(500 , "its the internal server error")



async def verifyToken(request : Request):

    auth_header = request.headers.get("Authorization")
    
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized: Bearer token missing or invalid")
    
    bearer_token = auth_header[len("Bearer "):].strip()

    if bearer_token is None : 
        return failure_responses(400  , "no token provided")
    
    response = validate_tokens(request)
    if response is False :
        return failure_responses(400 , "not a valid token provided")

    
    return success_responses(200 , "the verification is done")




async def connectToDbController():
    try:
        connection = getConnection()
        print("Performing operations on the database...")  
    except Exception as e:
        print(f"An error occurred: {e}")
        return failure_responses(500, "An error occurred while connecting to the database.")
    finally:
        if 'connection' in locals() and connection:
            closeConnection(connection)

    return success_responses(200, "The database connection was made successfully and closed.")
