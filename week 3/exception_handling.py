from typing import Any, Callable

from fastapi import Request
from fastapi.responses import JSONResponse

class SignupFailed(Exception):
    pass

class EmailAlreadyRegistered(Exception):
    pass

class LoginFailed(Exception):
    pass

class AccessTokenNotProvided(Exception):
    pass

class UserNotFound(Exception):
    pass

class SignOutFailed(Exception):
    pass

def create_exception_handler(
        status_code:int,
        initial_detail:Any
) -> Callable:

    async def exception_handler(
        request:Request,
        exc:Exception
    )->JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content=initial_detail
        )

    return exception_handler
