from fastapi import APIRouter, status, Request, Depends
from fastapi.responses import JSONResponse
from supabase import AsyncClient
from models import (
    signupModel,
    loginModel
)
from auth import userService
from exception_handling import (
    LoginFailed,
    SignOutFailed
)
from dependencies import TokenBearer

router = APIRouter()

user_service_obj = userService()
def get_supabase(
    request: Request
) -> AsyncClient:
    return request.app.state.supabase


@router.post("/auth/signup")
async def supabase_auth_signup(
    credentials: signupModel,
    client: AsyncClient = Depends(get_supabase)
):
    user = await user_service_obj.signup(
        credentials.email,
        credentials.password,
        client
    )

    return JSONResponse(
        status_code = status.HTTP_201_CREATED,
        content= {
            "message":"user succesfully created",
            "details":{
                "user_id":user.id,
                "email":user.email
            }
        }
    )


@router.post("/auth/login")
async def login(
    credentials:loginModel,
    client:AsyncClient = Depends(get_supabase),
):
    response = await user_service_obj.login(
        credentials.email, 
        credentials.password, 
        client
    )

    if response.session is None or response.user is None:
        raise LoginFailed()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "email" : response.user.email,
            "user_id": response.user.id,
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }
    )

@router.get("/public/info")
async def get_info():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "welcome stranger! This info is public"
        }
    )

@router.get("/protected/profile")
async def get_protected_profile(userDetails:dict = Depends(TokenBearer())):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "details":userDetails
        }
    )

@router.post("/auth/logout")
async def logout(token: str = Depends(TokenBearer()), client:AsyncClient = Depends(get_supabase)):
    response = await user_service_obj.sign_out(client)

    if response is False:
        raise SignOutFailed
    
    return JSONResponse(
        status_code=204,
        content={
            "message":"log out successfull"
        }
    )