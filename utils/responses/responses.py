from fastapi.responses import JSONResponse 
from fastapi import HTTPException


def success_responses(status: int, message: str, data: dict = None):
    """
    Generate a success response with status, message, and optional data.
    """
    response = {
        "status": "success",
        "message": message,
        "data": data if data else {}
    }
    return JSONResponse(content=response, status_code=status)


def failure_responses(status: int, message: str, data: dict = None):
    """
    Generate a failure response with status, message, and optional data.
    """
    response = {
        "status": "failure",
        "message": message,
        "data": data if data else {}
    }

    raise HTTPException(status_code=status, detail=response)  

