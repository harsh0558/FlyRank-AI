from supabase import AsyncClient
from pydantic import EmailStr
from supabase_auth.errors import AuthApiError 
from supabase_auth.types import (
    User, 
    AuthResponse
)
from exception_handling import (
    LoginFailed,
    SignupFailed,
    EmailAlreadyRegistered,
    UserNotFound
)
class userService:
    async def signup(
            self,
            email:EmailStr,
            password:str,
            client:AsyncClient
    )-> User:
        try:
            response = await client.auth.sign_up({
                "email":email,
                "password":password
            })

            if response.user is None:
                raise SignupFailed()

            return response.user
        except AuthApiError as e:
            if e.code == "user_already_exists":
                raise EmailAlreadyRegistered()

            raise SignupFailed()

    async def login(
        self,
        email: EmailStr,
        password: str,
        client: AsyncClient
    )->AuthResponse:
        try:
            response = await client.auth.sign_in_with_password({
                    "email": str(email),
                    "password": password
                })

            return response
        
        except AuthApiError as e:
            raise LoginFailed()

    async def verify_access_token(
        self,
        token:str,
        client: AsyncClient
    ) -> str:
        try:
            response = await client.auth.get_user(token)
            if response is None:
                raise UserNotFound()

            return response.user.id
        
        except Exception as e:
            raise UserNotFound()
