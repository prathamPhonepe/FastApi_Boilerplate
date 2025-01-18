from fastapi import APIRouter, Request  , Depends
from controllers.controller import (echoServer , 
                                    generate_jwt_token   , 
                                    connectToDbController
                                    )
from controllers.controller import verifyToken
from middleware.auth_middleware.auth_middleware import authMiddleware


def init_routes(app):
    router = APIRouter()

    @router.get("/")
    async def root():
        return {"message": "Welcome to the API!"}

    @router.post("/echo")
    async def echo_data(request: Request):
        return await echoServer(request)
    
    @router.post('/generateToken')
    async def generateToken(request : Request):
        return await generate_jwt_token(request)
    

    @router.get('/testMiddleware')
    async def verify(request: Request, _: None = Depends(authMiddleware)):
        return {"message" : "hello this is the bes"}
    

    @router.get('/verifyToken')
    async def verify_token(request : Request):
        return await verifyToken(request)
    

    @router.get('/connectToDb')
    async def connectToDb():
        return await connectToDbController()
    
    

    app.include_router(router, prefix="/api/v1")
