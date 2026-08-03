from fastapi import Request
from fastapi.security import HTTPBearer
from exception_handling import AccessTokenNotProvided

class TokenBearer(HTTPBearer):
    
    def __init__(self,auto_error=False):
        super().__init__(auto_error=auto_error)

        
    async def __call__(self, request:Request):
        creds = await super().__call__(request)
        if creds is None:
            raise AccessTokenNotProvided

        return creds.credentials
        