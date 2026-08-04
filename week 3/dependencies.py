from fastapi import Request
from fastapi.security import HTTPBearer
from exception_handling import AccessTokenNotProvided
from auth import userService

user_service = userService()
class TokenBearer(HTTPBearer):
    
    def __init__(self,auto_error=False):
        super().__init__(auto_error=auto_error)

        
    async def __call__(self, request:Request):
        creds = await super().__call__(request)
        if creds is None:
            raise AccessTokenNotProvided()

        user_id = await user_service.verify_access_token(creds.credentials, request.app.state.supabase)
        return {
            "user_id":user_id,
            "access_token":creds.credentials
        }
        